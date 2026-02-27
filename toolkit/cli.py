import typer
from toolkit.gatherer import capture_process_snapshot, capture_health_signals

app = typer.Typer(help="Incident Response & Diagnostic Bundler")

@app.command()
def gather():
    """Gather system health signals and log files."""
    typer.echo("Creating staging area...")
    
    typer.echo("Gathering process snapshot...")
    capture_process_snapshot()
    
    typer.echo("Gathering disk and memory health signals...")
    capture_health_signals()
    
    typer.secho("Success: Health signals gathered in .staging/ directory.", fg=typer.colors.GREEN)

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