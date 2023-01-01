from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def getValue():
    if request.form['google']:
        keyword = request.form['google']
    elif request.form['bing']:
        keyword = request.form['bing']


    url = f"https://www.google.com/search?&q={keyword}"
    print(url)

    try:
        #get the text based on keyword in google
        source = requests.get(url)
        source.raise_for_status()

        soup = BeautifulSoup(source.text, 'lxml')

        items = soup.findAll('div')
        print(len(items))
        google_text = soup.find('div', jsname = "n760b").text
        print(google_text)

        #split text into the questions and answers


        # i = 0
        # while i<len(items):
        #     attr = items[i].get("class")
        #     item = attr
        #     if item:
        #         class_name = f"{item[0]}"
        #         #print(class_name)
        #         text_soup = soup.find('div', class_=class_name).text
        #         if text_soup == "People also ask":
        #             print(class_name)
        #             print(text_soup)
        #
        #     i += 1

    except Exception as e:
        print(e)

    return keyword



if __name__ == '__main__':
    app.run(debug=True)
