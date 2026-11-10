import sys
from pathlib import Path

# Ensure JobFit_AI's parent directory is in sys.path so `import JobFit_AI` works from any working directory
jobfit_dir = Path(__file__).resolve().parent.parent
parent_dir = jobfit_dir.parent

if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))
if str(jobfit_dir) not in sys.path:
    sys.path.insert(0, str(jobfit_dir))
