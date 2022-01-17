import json
import random

from flask import Flask, render_template, request
import http_client

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/book')
def book():
    author = request.args.get("author")
    if author is None:
        return "No author parameter"
    client = http_client.HttpClient()
    base_url = "https://reststop.randomhouse.com/resources/works"
    url = f'{base_url}?start=0&max=0&expandLevel=0&search={author}'
    print(url)
    data = client.get(url)
    books = []
    book_obj = json.loads(data)['work']
    print(book_obj)
    random_int = random.randint(0, len(book_obj)-1)
    uri = book_obj[random_int]
    img_obj = client.get(uri['@uri'])
    print(img_obj)
    if img_obj:
        titles = json.loads(img_obj)['titles']['isbn']
        if type(titles) == list:
            isbn = titles[0]['$']
        else:
            isbn = titles['$']
        print(isbn)
    # for uri in json.loads(data)['work']:
    #     d = json.loads(client.get(uri['@uri']))
    #     print(d)
    #     code = d['titles']['isbn'][0]['$']
    #     t = f"https://covers.openlibrary.org/b/isbn/{code}-M.jpg"
    #     books.append(t)
    # print(books)
    return render_template('books.html', data=books, default_image_url='/static/images/default-placeholder.png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5556, debug=True)