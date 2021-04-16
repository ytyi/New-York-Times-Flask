from flask import Flask, render_template
import requests
from secrets import api_key

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)

@app.route('/headlines/<nm>')
def headlines(nm):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {'api-key': api_key}
    response = requests.get(base_url, params)
    res = response.json()['results'][:5]
    titles=[]
    for x in res:
        titles.append(x['title'])
    return render_template('headlines.html', name=nm, titles=titles)

@app.route('/links/<nm>')
def ex1(nm):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {'api-key': api_key}
    response = requests.get(base_url, params)
    res = response.json()['results'][:5]
    titles_urls = []
    for x in res:
        titles_urls.append([x['title'],x['url']])

    return render_template('ex1.html', name=nm, titles_urls=titles_urls)

@app.route('/images/<nm>')
def ex2(nm):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {'api-key': api_key}
    response = requests.get(base_url, params)
    res = response.json()['results'][:5]
    total = []
    for x in res:
        total.append([x['title'], x['url'],x['multimedia'][1]['url']])

    return render_template('ex2.html', name=nm, total=total)

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)




