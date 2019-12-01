import pika
from pika import PlainCredentials, ConnectionParameters


credentials = PlainCredentials(username='hackaton', password='QtGcmpPm')
parameters = ConnectionParameters(host='185.143.172.238',
                                         port=5672,
                                         virtual_host='/',
                                         credentials=credentials)
connection = pika.BlockingConnection(
    parameters=parameters)
channel = connection.channel()
channel.exchange_declare(exchange='telemetry', exchange_type='topic')


channel.queue_declare(queue='hello')

channel.basic_publish(
    exchange='topic_logs', routing_key='telemetry')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()