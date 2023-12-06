import typer
from upload import upload_file
from write import write_db
from leer_db import read_by_file, show_files

app = typer.Typer()

@app.command()
def upload(path_file: str,
         max_downloads: int = typer.Option(
            None,
            help="Max downloads allowed for the file",
            rich_help_panel="Upload Options"),
         max_days: int = typer.Option(
            14,
            help="Max days for dowload (transfer.sh allow: 14)",
            rich_help_panel="Upload Options")
         ):
    
    headers = {}
    
    if max_downloads:
        headers['Max-Downloads'] = str(max_downloads)
    if max_days <= 14:
        headers['Max-Days'] = str(max_days)
    else:
        print("Max days allowed: 14")
        raise typer.Exit(code=1)
    
    data = upload_file(path_file, headers)
    write_db(data)

@app.command()
def show():
    show_files()

@app.command()
def search():
    read_by_file()

if __name__ == "__main__":
    # typer.run(main)
    app()
