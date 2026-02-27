import os
from pathlib import Path
from toolkit.gatherer import capture_process_snapshot, capture_health_signals, STAGING_DIR

def test_capture_process_snapshot():
    file_path = capture_process_snapshot()
    assert file_path.exists()
    assert file_path.parent.name == ".staging"
    assert os.path.getsize(file_path) > 0

def test_capture_health_signals():
    file_path = capture_health_signals()
    assert file_path.exists()
    assert "health" in file_path.name.lower()
    assert os.path.getsize(file_path) > 0