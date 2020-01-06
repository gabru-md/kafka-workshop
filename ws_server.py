import json
import asyncio
import websockets
from mykafka.producer import build_kafka_producer

rider_producer = build_kafka_producer()
order_producer = build_kafka_producer(False)

ws_rider = None
ws_tracker = None

async def produce_to_rider_topic(message=None):
	message = json.dumps(message)
	if not rider_producer.produce(message):
		print('Error producing to rider-topic')


async def produce_to_tracker_topic(message=None):
	message = json.dumps(message)
	if not order_producer.produce(message):
		print('Error producing to order-topic')


async def serve_requests(websocket, path):
	
	global ws_tracker
	global ws_rider

	async for message in websocket:
		data = json.loads(message)
		print(data)
		if 'change' in data:

			response = {
				'update': data['change'],
				'position': data['position']
			}

			if data['change'] == 'rider':
				if not ws_rider:
					ws_rider = websocket

				await produce_to_rider_topic(data)

				if ws_tracker:
					await ws_tracker.send(json.dumps(response))

			if data['change'] == 'tracker':
				if not ws_tracker:
					ws_tracker = websocket

				await produce_to_tracker_topic(data)

				if ws_rider:
					await ws_rider.send(json.dumps(response))

		elif 'update' in data:

			if data['update'] == 'rider':
				ws_tracker.send(json.dumps(data))
			if data['update'] == 'tracker':
				ws_rider.send(json.dumps(data))


start_server = websockets.serve(serve_requests, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()