from kafka import KafkaConsumer
from config.config import KAFKA_CONFIG as config

def build_kafka_consumer(delivery_guy=True):

	if not delivery_guy:
		return build_order_kafka_consumer()

	return build_delivery_kafka_consumer()


def build_order_kafka_consumer():

	consumer = KafkaConsumer(
		config['TOPIC_ORDER'],
		bootstrap_servers=config['BROKERS'],
		group_id=config['CONSUMER_GROUP_ORDER']
		)

	return consumer

def build_delivery_kafka_consumer():

	consumer = KafkaConsumer(
		config['TOPIC_DELIVERY_GUY'],
		bootstrap_servers=config['BROKERS'],
		group_id=config['CONSUMER_GROUP_DELIVERY']
		)

	return consumer
