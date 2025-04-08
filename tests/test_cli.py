from click.testing import CliRunner
from unittest.mock import patch

from gha_deploy.cli import deploy

def test_deploy_cli():
    runner = CliRunner()
    result = runner.invoke(deploy, ["GHA-Deploy-CLI", "Unit-Test.yml", "main"])

    assert result.exit_code == 0
    assert "GitHub Action triggered successfully!" in result.output
    assert "Waiting for Job to finish..." in result.output
    assert "Workflow completed successfully! ✅" in result.output