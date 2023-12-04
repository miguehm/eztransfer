import typer
from upload import upload_file

def main(path_file: str,
         max_downloads: int = typer.Option(
            None,
            help="Max downloads allowed for the file",
            rich_help_panel="Upload Options"),
         max_days: int = typer.Option(
            None,
            help="Max days for dowload (transfer.sh allow: 14)",
            rich_help_panel="Upload Options")
         ):
    
    return path_file

    headers = {}
    
    if max_downloads:
        headers['Max-Downloads'] = str(max_downloads)
    if max_days and max_days <= 14:
        headers['Max-Days'] = str(max_days)
    else:
        print("Max days allowed: 14")
        raise typer.Exit(code=1)
    
    print(upload_file(path_file, headers))

if __name__ == "__main__":
    typer.run(main)
