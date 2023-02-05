import os
from pathlib import Path
import sys

import typer
from git import Repo
from invoke import Context


app = typer.Typer()


REPO_ROOT = Path(__file__).parent.parent.resolve()
MKDOKCS_MATERIAL_INSIDERS_REPO_URL = (
    "git@github.com:squidfunk/mkdocs-material-insiders.git"
)
MKDOCS_REQUIREMENTS_FILE_NAME = "mkdocs_requirements.txt"
MKDOCS_INSIDERS_CONFIG_FILE_NAME = "mkdocs.insiders.yml"


@app.command()
def install():
    """Install required packages.

    NOTE:
        Assumes that the env var `MKDOCS_MATERIAL_INSIDERS_DIR` is set. This env var
        must point to the repo location of the Material for MkDocs insiders github repo.
    """
    typer.echo("Installing required packages...")
    if sys.platform not in ("linux", "darwin"):
        typer.echo("This script only supports Linux and macOS.")
        typer.abort()
    # Install MkDocs Material related requirements
    mkdocs_requirements_file_path = (
        REPO_ROOT / MKDOCS_REQUIREMENTS_FILE_NAME
    ).resolve()
    context = Context()
    context.run(f"pip install -r {mkdocs_requirements_file_path}")
    try:
        MKDOCS_MATERIAL_INSIDERS_DIR = os.environ["MKDOCS_MATERIAL_INSIDERS_DIR"]
    except KeyError:
        typer.echo("The env var `MKDOCS_MATERIAL_INSIDERS_DIR` is not set.")
        typer.abort()
    # Install MkDocs Material Insiders
    repo_path = Path(MKDOCS_MATERIAL_INSIDERS_DIR).expanduser().resolve()
    if not repo_path.exists():
        Repo.clone_from(
            MKDOKCS_MATERIAL_INSIDERS_REPO_URL,
            MKDOCS_MATERIAL_INSIDERS_DIR,
        )
    with context.cd(str(repo_path)):
        context.run("pip install -e .")
    typer.echo("Finished installing required packages.")
    typer.echo("You are now ready to serve the docs.")


@app.command()
def serve(
    install_deps: bool = typer.Option(False, "-i", "--install", help="Install dependencies first.")
):
    """Serve the docs."""
    if install_deps:
        install()
    context = Context()
    with context.cd(str(REPO_ROOT)):
        context.run(f"mkdocs serve --config-file {MKDOCS_INSIDERS_CONFIG_FILE_NAME}")


@app.command()
def publish():
    """Publish the docs"""
    typer.echo("Publishing the docs...")
    # Ensure that you're on the main branch
    if Repo(REPO_ROOT).active_branch.name != "main":
        typer.echo("You must be on the main branch to publish the docs.")
        typer.Abort()
    context = Context()
    context.run("mkdocs gh-deploy")
