import typer
from typing import Optional
from pathlib import Path
from toolkit.gatherer import (
    capture_process_snapshot, 
    capture_health_signals, 
    parse_config, 
    gather_files_from_config,
    STAGING_DIR
)
from toolkit.redactor import redact_directory

app = typer.Typer(help="Incident Response & Diagnostic Bundler")

@app.command()
def gather(
    config: Optional[str] = typer.Option(None, "--config", "-c", help="Path to YAML config file."),
    no_redact: bool = typer.Option(False, "--no-redact", help="Disable automatic redaction of sensitive data.")
):
    """Gather system health signals and log files."""
    typer.echo("Creating staging area...")
    
    typer.echo("Gathering process snapshot...")
    capture_process_snapshot()
    
    typer.echo("Gathering disk and memory health signals...")
    capture_health_signals()
    
    if config:
        try:
            typer.echo(f"Parsing config file: {config}...")
            parsed_config = parse_config(config)
            if parsed_config:
                typer.echo("Gathering logs and artifacts from config...")
                gather_files_from_config(parsed_config)
        except Exception as e:
            typer.secho(f"Error processing config: {e}", fg=typer.colors.RED)
            raise typer.Exit(1)
            
    # Redaction Step
    if not no_redact:
        typer.echo("Applying safeguards: Redacting sensitive data...")
        redact_directory(STAGING_DIR)
    else:
        typer.secho("Warning: Redaction disabled. Artifacts may contain sensitive data.", fg=typer.colors.YELLOW)
        
    typer.secho("Success: Artifacts gathered and secured in .staging/ directory.", fg=typer.colors.GREEN)

@app.command()
def redact():
    """Manually trigger redaction on the staging directory."""
    typer.echo("Applying safeguards: Redacting sensitive data...")
    redact_directory(STAGING_DIR)
    typer.secho("Success: Manual redaction complete.", fg=typer.colors.GREEN)

@app.command()
def bundle():
    """Bundle artifacts into a shareable archive."""
    typer.echo("Bundling artifacts...")

@app.command()
def report():
    """Generate a standardized post-incident report."""
    typer.echo("Generating post-incident report...")

if __name__ == "__main__":
    app()