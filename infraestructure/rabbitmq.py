import pika
import time
import os

class RabbitMQ:
    host = os.getenv('RABBITMQ_HOST')
    print("cccc",host)
    def __init__(self, host = host):
        self.host = host
        self.connection = None
        self.channel = None
        self.connect()

    def connect(self):
        while True:
            try:
                self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
                self.channel = self.connection.channel()
                break
            except pika.exceptions.AMQPConnectionError as e:
                print(f"Connection error: {e}, retrying in 5 seconds...")
                time.sleep(5)

    def send_message(self, queue, message):
        self.channel.queue_declare(queue=queue)
        self.channel.basic_publish(exchange='', routing_key=queue, body=message)

    def receive_message(self, queue, callback):
        self.channel.queue_declare(queue=queue)
        self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()
