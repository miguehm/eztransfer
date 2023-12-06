import requests
import typer
from datetime import datetime

def get_tokens(link):
    link = link.split('/')
    return link[3], link[5]

def get_date(upload_date):
    date = datetime.strptime(upload_date, '%a, %d %b %Y %H:%M:%S %Z')
    return date

def upload_file(file_path: str, headers: dict = {}):
    try:
        with open(file_path, 'rb') as f:
            response = requests.post('https://transfer.sh/', headers=headers, files={'file': f})
            # print(response.status_code)
        upload_date = get_date(response.headers['Date'])
        link = get_tokens(response.headers['X-Url-Delete'])

        d = dict()
        d['filename'] = file_path.split('/')[-1]
        d['download_token'] = link[0]
        d['delete_token'] = link[1]
        d['day'] = upload_date.strftime("%d")
        d['month'] = upload_date.strftime("%m")
        d['year'] = upload_date.strftime("%Y")
        d['hour'] = upload_date.strftime("%H")
        d['minute'] = upload_date.strftime("%M")
        d['second'] = upload_date.strftime("%S")
        d['max-days'] = headers['Max-Days']
        
        print("Upload successful")
        return d
        
    except FileNotFoundError as e:
        print(f"File not found: \"{file_path}\"")
        raise typer.Exit(code=1)

if __name__ == '__main__':
    print(upload_file('./README.md', {'Max-Downloads': '1'}))
