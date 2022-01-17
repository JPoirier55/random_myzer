import json

from flask import Flask, render_template, request
import http_client

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/book')
def book():
    author = request.args.get("author")
    client = http_client.HttpClient()
    base_url = "https://reststop.randomhouse.com/resources/works"
    start = 0
    max = 0
    expandLevel = 0
    url = f'{base_url}?start={start}&max={max}&expandLevel={expandLevel}&search={author}'
    data = client.get(url)
    books = []
    for uri in json.loads(data)['work']:
        d = json.loads(client.get(uri['@uri']))
        print(d)
        code = d['titles']['isbn'][0]['$']
        t = f"https://covers.openlibrary.org/b/isbn/{code}-M.jpg"
        books.append(t)
        print(books)
    # print(books)
    return render_template('books.html', data=books, default_image_url='/static/images/default-placeholder.png')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5556, debug=True)