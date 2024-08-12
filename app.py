from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_news', methods=['POST'])
def get_news():
    query = request.form['query']
    url = f"https://newsapi.org/v2/everything?q={query}&from=2024-06-25&sortBy=publishedAt&apiKey=[YOUR_API]"

    r = requests.get(url)
    news = json.loads(r.text)

    if 'articles' in news:
        return jsonify(news["articles"])
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)

# Create your account in NewsAPI and use your own API
