import typer
from typing import Optional
from toolkit.gatherer import (
    capture_process_snapshot, 
    capture_health_signals, 
    parse_config, 
    gather_files_from_config
)

app = typer.Typer(help="Incident Response & Diagnostic Bundler")

@app.command()
def gather(config: Optional[str] = typer.Option(None, "--config", "-c", help="Path to YAML config file.")):
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
                
        except FileNotFoundError as e:
            typer.secho(f"Error: {e}", fg=typer.colors.RED)
            raise typer.Exit(1)
        except Exception as e:
            typer.secho(f"Unexpected error parsing config: {e}", fg=typer.colors.RED)
            raise typer.Exit(1)
            
    typer.secho("Success: Artifacts gathered in .staging/ directory.", fg=typer.colors.GREEN)

@app.command()
def redact():
    """Redact sensitive information from gathered logs."""
    typer.echo("Redacting sensitive data...")

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