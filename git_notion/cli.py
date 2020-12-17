"""Console script for git_notion."""
import sys
import click
import git_notion


@click.command()
@click.option('--path', default=".", help='The path to the repo you want to sync')
def main(path):
    """Console script for git_notion."""
    click.echo("running sync")
    git_notion.sync_to_notion(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
