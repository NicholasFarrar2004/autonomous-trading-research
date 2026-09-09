"""Fetch pinned upstream source and apply reviewed patches. Never starts a broker."""
import argparse,json,subprocess,sys,shutil,venv
from pathlib import Path
from project_paths import HOME,UPSTREAM
ROOT=Path(__file__).resolve().parent

def run(args,cwd=None):subprocess.run([str(x) for x in args],cwd=cwd,check=True)

def prepare(name,install=False):
 spec=json.loads((ROOT/'upstreams.json').read_text())[name];dest=UPSTREAM/name
 UPSTREAM.mkdir(parents=True,exist_ok=True)
 if not dest.exists():
  run(['git','clone','--no-checkout',spec['url'],dest]);run(['git','checkout','--detach',spec['commit']],dest)
 head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=dest,text=True).strip()
 if head!=spec['commit']:raise SystemExit('Existing checkout differs from pinned revision; preserved without changes.')
 patch=ROOT/spec['patch']
 applied=subprocess.run(['git','apply','--reverse','--check',str(patch)],cwd=dest,capture_output=True).returncode==0
 if not applied:
  run(['git','apply','--check',patch],dest);run(['git','apply',patch],dest)
 if name=='pysystemtrade':
  target=dest/'sysbrokers/IB/paper_guard.py'
  if target.exists() and target.read_bytes()!=(ROOT/'paper_guard.py').read_bytes():raise SystemExit('Existing guard differs; preserved.')
  shutil.copyfile(ROOT/'paper_guard.py',target)
 if install:
  if sys.version_info[:2]!=(3,12):raise SystemExit('Dependency snapshot was verified on Python 3.12; use python3.12.')
  env=HOME/('venv-'+name)
  if not env.exists():venv.EnvBuilder(with_pip=True).create(env)
  python=env/'bin/python'
  run([python,'-m','pip','install','-r',ROOT/('requirements-'+name+'.txt')])
  run([python,'-m','pip','install','--no-deps','-e',dest])
 print('Pinned source prepared:',name,'(no broker process or trade started)')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('project',choices=['pysystemtrade','passivbot']);p.add_argument('--install',action='store_true');a=p.parse_args();prepare(a.project,a.install)
