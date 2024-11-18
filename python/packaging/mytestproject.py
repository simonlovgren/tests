import click
import datetime
import os
from git import Repo, InvalidGitRepositoryError
from rich.text import Text
from rich.console import Console


# Custom log time format
def render_time(log_time: datetime) -> Text:
    return Text(log_time.strftime("[%Y-%m-%d %H:%M:%S.%f]"))


# Create a console object
console = Console(log_time_format=render_time)


# Main function
@click.command()
@click.option("--name", prompt="Your name", help="Your name, please.")
def main(name):
    """
    A simple CLI test project.
    """
    console.log(f"Hello [bold magenta]{name}[/bold magenta] :wave:!")

    console.log(f"You're currently in: [yellow]{os.getcwd()}[/yellow]")

    # Check if the current directory is a git repository
    # and if so, get the repo root
    try:
        repo = Repo(os.getcwd(), search_parent_directories=True)
        if repo:
            repo_root = repo.git.rev_parse("--show-toplevel")
            console.log(f"Which is a repository [cyan]({repo_root})[/cyan].")
    except InvalidGitRepositoryError:
        console.log("Which is [red][u]not[/u][/red] a git repository.")

