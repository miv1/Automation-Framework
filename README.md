Sorry, I would like to add some hooks and cucumber, but I had to do some errands.

# Selenium with Python

This is a repository will examples to use selenium with python

# Requirements
- Python 3.6 or higher
- Pip 3
- Selenium
- PyUnitReport
- Web Browser Driver

# Installation Python and pip (Linux)

First verify if your version of python and pip is the correct

### Python

Open an Terminal and verify the version of Python with the next command:

`python3 --version`

The output should will be next or higher:

`Python 3.6.9` 

### Pip

Open an Ternimal and verify the version of pip with the next command:

`pip3 --version`

The output should will be next or higher:

- `pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)`

If you don't have pip intall with the next command:

`sudo apt install python3-pip`

## How use the libraries on an Virtual Environment

Run the next commands on the Terminal:
1. `pip3 install virtualenv`
1. `sudo apt install python3.8-venv`
1. `python3 -m venv <name of folder for the libraries>`
1. `source <name of folder for the libraries>/bin/activate`
1. `pip3 install -r requirements.txt `

### Web Browser Driver
Follow the next links and download the WebDriver you will be use:
- [Firefox](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0)
- [Safari](https://developer.apple.com/documentation/webkit/about_webdriver_for_safari)
- [Opera](https://github.com/operasoftware/operachromiumdriver/releases)
- [Chrome](https://sites.google.com/a/chromium.org/chromedriver/)
- [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads)

# Execution

In the terminal go to the folder main and execute:

- `python3 <name of file execute>`

Examples:
- `python3 hello_world`
- `python3 search_test`