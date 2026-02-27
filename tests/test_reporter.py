import json
from pathlib import Path
from toolkit.reporter import generate_report

def test_generate_report_markdown():
    data = {"lead": "Jane Doe", "severity": "SEV-1", "summary": "DB down", 
            "impact_details": "No logins", "timeline": "10:00 AM", 
            "cause": "Bad query", "actions": "Killed query", "date": "Today"}
    
    path = generate_report(data, output_format="markdown")
    
    assert path.exists()
    assert path.suffix == ".md"
    content = path.read_text(encoding="utf-8")
    assert "Jane Doe" in content
    assert "SEV-1" in content
    
    # Cleanup
    path.unlink()

def test_generate_report_json():
    data = {"lead": "John Doe", "severity": "SEV-2"}
    
    path = generate_report(data, output_format="json")
    
    assert path.exists()
    assert path.suffix == ".json"
    
    with open(path, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
        assert loaded_data["lead"] == "John Doe"
        assert loaded_data["severity"] == "SEV-2"
        
    # Cleanup
    path.unlink()