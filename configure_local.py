"""Write a disabled local template. Does not connect or authorize orders."""
import json,os
from project_paths import HOME,PRIVATE,STATE
from synthetic_fixture import synthetic_profile
if __name__=='__main__':
 PRIVATE.mkdir(mode=0o700,parents=True,exist_ok=True);STATE.mkdir(mode=0o700,parents=True,exist_ok=True)
 path=PRIVATE/'private_config.yaml'
 if path.exists():raise SystemExit('Existing private configuration preserved; edit it locally if needed.')
 with path.open('x') as f:json.dump(synthetic_profile(HOME),f,indent=2)
 os.chmod(path,0o600)
 (STATE/'STOP').write_text('Entry disabled. See OPERATIONS.md before any intentional paper exercise.\n')
 print('Disabled private template and STOP marker created outside the repository. No connection made.')
