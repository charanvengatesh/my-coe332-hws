import urllib.request
import redis
from flask import Flask, request
import json

url = "https://g-a8b222.dd271.03c0.data.globus.org/pub/databases/genenames/hgnc/json/hgnc_complete_set.json"



app = Flask(__name__)
r = redis.Redis(host='127.0.0.1', port=6379, db=0)


@app.route('/data', methods=['POST'])
def post_data():
    """
    Fetches all or a subset of data depending on query parameters 'limit' and 'offset'.
    """
    # read the data from the URL and store it in a variable in Redis
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8') 
    r.set('data', json.dumps(data))
    return "Data stored in Redis", 200

@app.route('/data', methods=['GET'])
def get_data():
    """
    Fetches all or a subset of data depending on query parameters 'limit' and 'offset'.
    """
    # read the data from Redis and return it
    try:
        data = json.loads(r.get('data'))
    except TypeError:
        return "Data not found in Redis", 404
        
    return data, 200

@app.route('/data', methods=['DELETE'])
def delete_data():
    """
    Fetches all or a subset of data depending on query parameters 'limit' and 'offset'.
    """
    # delete the data from Redis
    r.delete('data')
    return "Data deleted from Redis", 200

@app.route('/genes', methods=['GET'])
def get_genes():
    """
    Fetches all or a subset of genes depending on query parameters 'limit' and 'offset'.
    """
    # read the data from Redis and return it
    try:
        data = json.loads(r.get('data'))
    except TypeError:
        return "Data not found in Redis", 404

    # parse the data and return the genes
    genes = json.loads(data)['response']['docs']
    return genes, 200

@app.route('/genes/<gene_id>', methods=['GET'])
def get_gene(gene_id):
    """
    Fetches a single gene by its ID.
    """
    # read the data from Redis and return it
    try:
        data = json.loads(r.get('data'))
    except TypeError:
        return "Data not found in Redis", 404

    # parse the data and return the gene with the specified ID
    genes = json.loads(data)['response']['docs']
    for gene in genes:
        if gene['hgnc_id'] == gene_id:
            return gene, 200

    return "Gene not found", 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int("3000"))
