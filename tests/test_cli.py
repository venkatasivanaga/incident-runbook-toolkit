from typer.testing import CliRunner
from toolkit.cli import app

runner = CliRunner()

def test_app_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Incident Response & Diagnostic Bundler" in result.stdout