from flask import Flask, jsonify, request
from datetime import datetime
from iss_tracker import *

app = Flask(__name__)

@app.route('/epochs', methods=['GET'])
def get_all_epochs():
    """
    Fetches all or a subset of epochs depending on query parameters 'limit' and 'offset'.
    """
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    state_vectors = get_epochs()

    if limit is not None and offset is not None:
        try:
            limit = int(limit)
            offset = int(offset)
            return jsonify(state_vectors[offset:offset+limit])
        except ValueError:
            return "Invalid limit or offset", 400
    return jsonify(state_vectors)


@app.route('/epochs/<epoch>', methods=['GET'])
def get_epoch(epoch):
    """
    Fetches the state vector for a specific epoch.
    """
    state_vectors = get_epochs()
    for sv in state_vectors:
        if sv['EPOCH'] == epoch:
            return jsonify(sv)
    return "Epoch not found", 404


@app.route('/epochs/<epoch>/speed', methods=['GET'])
def get_epoch_speed(epoch):
    """
    Calculates and returns the instantaneous speed for a specific epoch.
    """
    state_vectors = get_epochs()
    for sv in state_vectors:
        if sv['EPOCH'] == epoch:
            speed = calculate_speed(float(sv['X_DOT']['#text']), float(
                sv['Y_DOT']['#text']), float(sv['Z_DOT']['#text']))
            return jsonify({"speed": speed})
    return "Epoch not found", 404


@app.route('/now', methods=['GET'])
def get_now():
    """
    Returns state vectors and instantaneous speed for the Epoch closest to the current time.
    """
    state_vectors = get_epochs()
    now = datetime.now()
    closest_epoch = find_closest_epoch(state_vectors, now)
    speed = calculate_speed(float(closest_epoch['X_DOT']['#text']), float(
        closest_epoch['Y_DOT']['#text']), float(closest_epoch['Z_DOT']['#text']))
    return jsonify({"closest_epoch": closest_epoch, "speed": speed})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int("3000"))
