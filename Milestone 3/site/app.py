from flask import Flask, render_template, request, jsonify
import requests
from sentence_transformers import SentenceTransformer


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '')
    solr_endpoint = 'http://localhost:8983/solr/#/books'
    collection = 'semantic_courses'
    embedding = text_to_embedding(query)

    try:
        results = solr_knn_query(solr_endpoint, collection, embedding)
        return jsonify(results.get('response', {}).get('docs', []))
    except requests.HTTPError as e:
        return jsonify({'error': f'Error {e.response.status_code}: {e.response.text}'})

def text_to_embedding(text):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(text, convert_to_tensor=False).tolist()
    return embedding

def solr_knn_query(endpoint, collection, embedding):
    url = f"{endpoint}/{collection}/select"

    data = {
        "q": f"{{!knn f=vector topK=10}}{embedding}",
        "fl": "id,title,score",
        "rows": 10,
        "wt": "json"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
