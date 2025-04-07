import click
from .github_api import trigger_workflow

# Mandatory inputs
@click.command()
@click.argument("repo", required=False)
@click.argument("workflow", required=False)
@click.argument("ref", required=False)
@click.option("--repo", "repo_opt", help="The repository to deploy.")
@click.option("--workflow", "workflow_opt", help="The workflow file to trigger.")
@click.option("--ref", "ref_opt", help="The Git ref (e.g., branch or tag) for the deployment.")

#optional flags
@click.option("--no-track", is_flag=True, help="Don't poll the workflow after triggering it.")



def deploy(repo, workflow, ref, repo_opt, workflow_opt, ref_opt):
    # Use flags if provided, otherwise fallback to positional args
    final_repo = repo_opt or repo
    final_workflow = workflow_opt or workflow
    final_ref = ref_opt or ref

    if not final_repo or not final_workflow or not final_ref:
        raise click.UsageError("You must provide repo, workflow, and ref either positionally or via flags.")

    trigger_workflow(final_repo, final_workflow, final_ref)

