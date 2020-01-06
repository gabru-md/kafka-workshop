from kafka import KafkaProducer
from config.config import KAFKA_CONFIG as config


def debug(message):
	return "[>] {}".format(message)


def build_kafka_producer(delivery_guy=True):

	if not delivery_guy:
		return build_order_kafka_producer()

	return build_delivery_kafka_producer()


def build_order_kafka_producer():

	return Producer(
		brokers=config['BROKERS'],
		topic=config['TOPIC_ORDER']
		)


def build_delivery_kafka_producer():
	print(config)
	return Producer(
		brokers=config['BROKERS'],
		topic=config['TOPIC_DELIVERY_GUY']
		)


class Producer:

	brokers = ''
	topic = ''
	producer = None

	def __init__(self, brokers=None, topic=None):

		if not brokers:
			return None

		if not topic:
			return None


		self.brokers = brokers
		self.topic = topic

		self.producer = KafkaProducer(
			bootstrap_servers=brokers
			)


	def produce(self, message=None):

		if not message:
			return False

		try:
			self.producer.send(
				self.topic,
				str.encode(message)
				)
			self.producer.flush()

		except Exception as exp:
			debug(exp)
			return False

		return True
