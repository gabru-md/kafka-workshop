from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from config import config
import uuid

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

from mykafka.producer import build_kafka_producer
rider_producer = build_kafka_producer()
order_producer = build_kafka_producer(False)

@app.route('/')
def index():
	return render_template('index.html', accessToken=config.ACCESS_TOKEN)


@app.route('/rider')
def rider():
	rider_id = str(uuid.uuid4())
	return render_template('rider.html', accessToken=config.ACCESS_TOKEN, rider_id=rider_id)


@app.route('/track')
def track():
	tracker_id = str(uuid.uuid4())
	return render_template('track.html', accessToken=config.ACCESS_TOKEN, tracker_id=tracker_id)


if __name__ == '__main__':
	app.run(debug=True)
