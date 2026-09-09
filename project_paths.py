"""Portable paths. Runtime data and private configuration stay outside the repository."""
import os
from pathlib import Path
HOME=Path(os.environ.get('PAPER_PROJECT_HOME',Path.home()/'.local/share/autonomous-trading-research')).expanduser().resolve()
DATA=HOME/'data'
PRIVATE=HOME/'private'
STATE=HOME/'paper'/'operation'
UPSTREAM=HOME/'upstream'
