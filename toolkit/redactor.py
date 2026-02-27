import re
import os
from pathlib import Path

# Dictionary of regex patterns for sensitive data
PATTERNS = {
    "IPV4": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "EMAIL": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+",
    # Added 'bearer' to the list of keywords to catch Authorization headers
    "API_KEY": r"(?i)(?:api[_-]?key|secret|token|password|bearer)[\s:=]+[\"']?[a-zA-Z0-9\-_]{16,}[\"']?"
}

def redact_text(text: str) -> str:
    """Applies all regex patterns to replace sensitive data in a string."""
    for key, pattern in PATTERNS.items():
        text = re.sub(pattern, f"[REDACTED {key}]", text)
    return text

def redact_file(file_path: Path):
    """Reads a file line-by-line, redacts data, and overwrites safely."""
    temp_path = file_path.with_suffix('.tmp')
    try:
        # Process line-by-line to avoid high memory usage on large log files
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile, \
             open(temp_path, 'w', encoding='utf-8') as outfile:
            for line in infile:
                outfile.write(redact_text(line))
        
        # Replace the original file with the redacted temporary file
        os.replace(temp_path, file_path)
    except Exception as e:
        if temp_path.exists():
            temp_path.unlink()
        print(f"Failed to redact {file_path.name}: {e}")

def redact_directory(dir_path: Path):
    """Recursively redacts all files in a directory."""
    for file_path in dir_path.rglob("*"):
        if file_path.is_file():
            redact_file(file_path)