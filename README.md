# AI Summariser

This is a simple AI Summariser that summariser the YouTube vide or Article. You need to provide the URL for the YouTube Video or Article you want to summarise

> **NOTICE**: I have refactored the code so there might be some bugs as I have not tested the refactored code yet. If you are facing any issue feel free to reach out to me [here](https://twitter.com/syedmuzamilm)

## How to use

Clone the repo locally

`git clone https://github.com/SyedMuzamilM/ai-summariser.git`

### Create Virtual Environemnt (Optional)

You can create virtual environment to install the dependencies

`python3 -m venv env`

Activate the environment

`source env/bin/activate`

Install the dependencies

`pip3 install -r requirements.txt`

## Run the program

There are two ways you can use this application

1. You can directly run the main file (cli based) using `python3 main.py -u "url of youtube video or article" -a(for article) -v(for video)`

2. This application used flask to create a simple UI where you can enter the URL and then get the summary for that. But this is only for the YouTube videos for now. For that you can run `flask run`
