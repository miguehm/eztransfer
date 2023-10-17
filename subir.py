import subprocess
import sys
from datetime import datetime

def upload_archives(*args):
    command = 'curl -v -i' # partial, options
    
    day = datetime.now().strftime("%d")
    month = datetime.now().strftime("%m")
    year = datetime.now().strftime("%Y")
    hour = datetime.now().strftime("%H")
    minute = datetime.now().strftime("%M")
    second = datetime.now().strftime("%S")
    queries = []
    
    for archive in args:
        command += f' -F filedata=@{archive}'
    command += ' https://transfer.sh/'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    urls = []
    for line in result.stdout.split('\n'):
        if 'x-url-delete' in line:
            url = line.split(': ')[1]
            if url not in urls:
                urls.append(url)
    
    for url in urls:
        url_split = url.split('/')
        queries.append((url_split[3], url_split[4], url_split[5], day, month, year, hour, minute, second))

    return queries

if __name__ == "__main__":
    results = upload_archives(*sys.argv[1:]) # skip script name
    print(results)
