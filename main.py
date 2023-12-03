import typer
from upload import upload_file

def main(path_file: str, lastname: str = "", formal: bool = False):
    print(upload_file(path_file))

if __name__ == "__main__":
    typer.run(main)
