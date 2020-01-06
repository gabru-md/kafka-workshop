import websockets
import asyncio
import json

async def Forward(message):
        url = 'ws://127.0.0.1:5678'
        async with websockets.connect(url) as websocket:
                await websocket.send(message)
                print('asda')
def xmit_Loop(message):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(Forward(message))


for _ in range(10):
	xmit_Loop(json.dumps({'change':'a', 'b':'b'}))
# import asyncio
# import ssl
# import websockets
# from concurrent.futures import ProcessPoolExecutor
# from mykafka.consumer import build_order_kafka_consumer, build_delivery_kafka_consumer

# tracker_consumer = build_order_kafka_consumer()
# rider_consumer = build_delivery_kafka_consumer()

# uri = "wss://127.0.0.1:5678"
# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

# def run_ws_consumer(message=None):
# 	try:
# 		with websockets.connect(uri, ssl=ssl_context) as websocket:
# 			websocket.send(message)
# 			print(message)
# 			return True
# 	except Exception as exp:
# 		print(exp)

# 	print('sdsa')
# 	return False

# def run_tracker_consumer():

# 	for message in tracker_consumer:
# 		"""
# 		here we hook up our different services!!
# 		"""
# 		print(message.value)
# 		print(run_ws_consumer(message.value))



# def run_rider_consumer():

# 	for message in rider_consumer:
# 		"""
# 		here we hook up our different services!!
# 		"""
# 		print(message.value)
# 		print(run_ws_consumer(message.value))


# executor = ProcessPoolExecutor(2)
# loop = asyncio.get_event_loop()

# rc_future = asyncio.ensure_future(loop.run_in_executor(executor, run_rider_consumer))
# tc_future = asyncio.ensure_future(loop.run_in_executor(executor, run_tracker_consumer))

# if __name__ == '__main__':

# 	loop.run_forever()