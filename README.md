# IMPORTANT NOTE

This is just a draft of what eztransfer aims to be; the majority of functions are not yet implemented.

To try the early version of this application, you should do the following:

## Dependences

Create a python enviroment:

```bash
python3 -m venv eztransfer
```

Activate it

```bash
source eztransfer/bin/activate
```

Install the requirements

```bash
pip install -r requirements.txt
```

## Run

To upload files

```bash
python3 test_cli.py upload <filepath1> <filepath2> ...
```

Automatically prints the sqlite database table of your recent files uploaded.

## TODO

- [x] Upload files method
- [x] Create the data base design and write on it
- [x] Upload multiple files as a cli tool using `click` lib
- [x] Encrypt functionality
- [ ] Design the commands and subcommands hierarchy
- [ ] *List* command
- [ ] *Delete* command
- [ ] *Help* command
- [ ] Turn to python whl package
- [ ] Upload to PyPI repository
- [ ] Add more example usages
- [ ] Add some gif command-line example usages 

## MAYBE

- [ ] Desing MVC

# eztransfer - transfer.sh links managing

eztransfer is a python that allows you to create and manage links to files uploaded to [transfer.sh](https://trasfer.sh) cloud storage service. With this application, you can easily upload files to the cloud of transfer.sh with 14-day expiration time for free and conveniently store and manage the generated links.

# Key Features

- File Upload: **Easily upload files** to the cloud using transfer.sh directly from the terminal.
- Link Management: eztransfer allows you to **store and organize** the generated links for your cloud files. No more worrying about losing access to important files.
- Automatic Expiration: The generated links have a 14-day expiration, eztransfer **reminds you of the remaining days** before they are deleted from the cloud.
- Command Line Interface (CLI): Access all of eztransfer's features from the terminal, making it easy to integrate into your existing workflow.

# Requirements

- Python 3.6>=
- curl

# Installation

You can install eztransfer using **pip**:

```bash
pip install eztransfer
```

# Usage

## Upload

```bash
eztransfer upload all.txt files.png you.mp4 want.docx
```

You can encrypt your files using `--encrypt` or `-e` flag

```bash
eztransfer upload all.txt files.png you.mp4 want.docx --encrypt
```

## List

List all your recent uploads (date descending sort by default)

```bash
eztransfer list
```

## Delete

Delete a link from your register

```bash
eztransfer delete <id>
```

If you prefer, delete of trasfer.sh cloud too using `--cloud` `-c` flag

```bash
eztransfer delete <id> --cloud
```

## Help

Get more help, examples and tricks

```bash
eztransfer --help
```

# Contributions

If you'd like to contribute to the development of eztransfer, you are welcome to! Feel free to open issues, suggest improvements, or submit pull requests.

# License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgments

We'd like to thank [trasfer.sh](https://trasfer.sh) for providing a convenient and free cloud storage service.

We hope you enjoy using **eztransfer** to efficiently manage your cloud file links!
