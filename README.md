![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/6vz/examyoinker)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/6vz/examyoinker)
![GitHub Repo stars](https://img.shields.io/github/stars/6vz/examyoinker)
![GitHub License](https://img.shields.io/github/license/6vz/examyoinker)



# examyoinker
Simple python script that downloads INF.03 exam questions to JSON and SQlite3.

## how it works?
It uses bs4 package to scrape the website, to get publicly available questions to the code-friendly format.

## how to run it
1. `pip3 install -r requirements.txt`
2. `python3 main.py`

(`pip3` as well as `python3` might be named differently in your OS)

## legal
Questions are scraped from [https://www.praktycznyegzamin.pl](https://www.praktycznyegzamin.pl), they made a "pretty overlay" for publicly available data provided by [Centralna Komisja Egzaminacyjna](https://cke.gov.pl). All rights belongs to CKE.

If you're using my project, please do follow guidelines in LICENSE
