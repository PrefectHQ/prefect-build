import typer
from build import build_deployment

app = typer.Typer()


@app.command()
def build(yaml_path: str, dry_run: bool = False):
    typer.echo("Hello World")


if __name__ == "__main__":
    app()
