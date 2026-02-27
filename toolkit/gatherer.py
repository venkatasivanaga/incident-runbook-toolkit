import psutil
from datetime import datetime
from pathlib import Path
import yaml
import shutil

# We will store all collected artifacts here before bundling
STAGING_DIR = Path(".staging")

def ensure_staging_dir():
    STAGING_DIR.mkdir(exist_ok=True)

def capture_process_snapshot():
    """Captures a snapshot of currently running processes."""
    ensure_staging_dir()
    snapshot_file = STAGING_DIR / "process_snapshot.txt"
    
    with open(snapshot_file, "w", encoding="utf-8") as f:
        f.write(f"--- Process Snapshot at {datetime.now().isoformat()} ---\n")
        f.write(f"{'PID':<10} {'NAME':<30} {'STATUS':<15}\n")
        f.write("-" * 55 + "\n")
        
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                f.write(f"{proc.info['pid']:<10} {proc.info['name']:<30} {proc.info['status']:<15}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
                
    return snapshot_file

def capture_health_signals():
    """Captures disk and memory usage statistics."""
    ensure_staging_dir()
    health_file = STAGING_DIR / "health_signals.txt"
    
    with open(health_file, "w", encoding="utf-8") as f:
        f.write(f"--- System Health Signals at {datetime.now().isoformat()} ---\n\n")
        
        # Memory Stats
        mem = psutil.virtual_memory()
        f.write("[Memory]\n")
        f.write(f"Total: {mem.total / (1024**3):.2f} GB\n")
        f.write(f"Available: {mem.available / (1024**3):.2f} GB\n")
        f.write(f"Percent Used: {mem.percent}%\n\n")

        # Disk Stats (Checking the root/C: drive)
        disk = psutil.disk_usage(str(Path.home().anchor)) 
        f.write(f"[Disk Usage ({Path.home().anchor})]\n")
        f.write(f"Total: {disk.total / (1024**3):.2f} GB\n")
        f.write(f"Free: {disk.free / (1024**3):.2f} GB\n")
        f.write(f"Percent Used: {disk.percent}%\n")
        
    return health_file

def tail_log_file(filepath: str, lines: int = 100):
    """Reads the last N lines of a specified log file."""
    ensure_staging_dir()
    target_path = Path(filepath)
    
    if not target_path.exists() or not target_path.is_file():
        return None
        
    output_file = STAGING_DIR / f"tail_{target_path.name}"
    
    # Read the file and grab the last N lines
    with open(target_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.readlines()
        
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"--- Tail of {target_path.name} (Last {lines} lines) ---\n")
        f.writelines(content[-lines:])
        
    return output_file

def parse_config(config_path: str):
    """Parses the YAML configuration file."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def gather_files_from_config(config: dict):
    """Tails logs and copies config files based on YAML."""
    ensure_staging_dir()
    
    # 1. Tail logs
    logs = config.get("logs", [])
    for log_file in logs:
        try:
            path = log_file.get("path")
            lines = log_file.get("lines", 100)
            if path:
                tail_log_file(path, lines)
        except Exception as e:
            print(f"Warning: Could not tail {log_file.get('path')}: {e}")

    # 2. Copy static config artifacts
    artifacts = config.get("artifacts", [])
    for artifact in artifacts:
        try:
            src = Path(artifact)
            if src.exists() and src.is_file():
                shutil.copy2(src, STAGING_DIR / src.name)
            else:
                print(f"Warning: Artifact not found or not a file: {artifact}")
        except Exception as e:
            print(f"Warning: Could not copy {artifact}: {e}")