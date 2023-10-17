import subprocess
import sys

def subir_archives(archives):
    if len(archives) == 0:
        print()
    command = 'curl -v -i'
    for archive in archives:
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
        print(url)
    return urls

if __name__ == "__main__":
    results = subir_archives(sys.argv[1:]) # skip script name
    print(results)
