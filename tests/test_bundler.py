import tarfile
from pathlib import Path
from toolkit.bundler import create_bundle, STAGING_DIR, clean_staging

def test_create_bundle():
    # Setup fake staging area
    STAGING_DIR.mkdir(exist_ok=True)
    test_file = STAGING_DIR / "test_artifact.txt"
    test_file.write_text("dummy diagnostic content")
    
    # Run the bundler
    archive_path = create_bundle()
    
    # Assertions
    assert archive_path.exists()
    assert archive_path.name.startswith("incident_bundle_")
    assert archive_path.name.endswith(".tar.gz")
    
    # Verify contents actually made it into the zip
    with tarfile.open(archive_path, "r:gz") as tar:
        names = tar.getnames()
        assert any("test_artifact.txt" in name for name in names)
        
    # Cleanup
    archive_path.unlink()
    clean_staging()