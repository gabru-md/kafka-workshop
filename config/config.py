# contains the config for comsumer and producer groups

URL = 'localhost'
PORT = '9092'
TOPIC_DELIVERY_GUY = 'delivery-guy-topic'
TOPIC_ORDER = 'order-topic'
CONSUMER_GROUP_ORDER= 'cg_order'
CONSUMER_GROUP_DELIVERY = 'cg_delivery'

BROKERS = "{0}:{1}".format(URL, PORT)

ACCESS_TOKEN = 'your.mapbox.access.token'

KAFKA_CONFIG = {
	'BROKERS' : BROKERS,
	'CONSUMER_GROUP_DELIVERY' : CONSUMER_GROUP_DELIVERY,
	'CONSUMER_GROUP_ORDER' : CONSUMER_GROUP_ORDER,
	'TOPIC_ORDER' : TOPIC_ORDER,
	'TOPIC_DELIVERY_GUY' : TOPIC_DELIVERY_GUY
	}