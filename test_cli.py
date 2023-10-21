import click
from subir import upload_archives
from escribir_db import write_db
from leer_db import read_by_file

@click.group()
def main():
    pass

@main.command() # define commands group
@click.argument('args', nargs=-1)
@click.option('--encrypt', '-e', is_flag=True, default=False)
def upload(args, encrypt):
    queries = upload_archives(*args)
    write_db(*queries)
    read_by_file()
    
    
# @main.command()
# @click.option('--name', prompt='Ingresa el nombre del usuario')
# @click.option('--password', '-p', prompt='Ingresa la contraseña del usuario', hide_input=True)
# @click.option('--email', '-e', default='')
# @click.option('--active', '-a', is_flag=True, default=True)
# def create_user(name, password, email, active):
#     print(name, password, email, active)

if __name__ == '__main__':
    main()
