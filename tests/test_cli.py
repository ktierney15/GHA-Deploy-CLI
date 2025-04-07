

def test_deploy_command():
    result = runner.invoke(cli.deploy, ['--repo', 'GHA-Deploy-CLI', '--workflow', 'Unit-Test.yml', '--ref', 'main'])
    assert result.exit_code == 0
