import tarfile
import shutil
from datetime import datetime
from pathlib import Path
from toolkit.gatherer import STAGING_DIR

def create_bundle(output_dir: str = ".") -> Path:
    """Compresses the staging directory into a timestamped tar.gz archive."""
    if not STAGING_DIR.exists() or not any(STAGING_DIR.iterdir()):
        raise FileNotFoundError("Staging area is empty or does not exist. Run 'gather' first.")
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"incident_bundle_{timestamp}.tar.gz"
    output_path = Path(output_dir) / archive_name
    
    with tarfile.open(output_path, "w:gz") as tar:
        # arcname ensures the folder inside the tar is just named ".staging" 
        # instead of containing the full absolute path from your C: drive
        tar.add(STAGING_DIR, arcname=STAGING_DIR.name)
        
    return output_path

def clean_staging():
    """Removes the staging directory after bundling to clean up."""
    if STAGING_DIR.exists():
        shutil.rmtree(STAGING_DIR)