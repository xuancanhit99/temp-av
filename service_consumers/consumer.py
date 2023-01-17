import pika


def callback(channel, method, properties, body):
    print(f" [x] Received {body}")
    message = body.decode()

    if message == "hey":
        print("hey there")
    elif message == "hello":
        print("well hello there")
    else:
        print(f"sorry i did not understand {body}")

    print(" [x] Done")
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():
    print(" [*] Connecting to server ...")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="task_queue", durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="task_queue", on_message_callback=callback)

    try:
        print(" [*] Waiting for messages. To exit press Ctrl+C")
        channel.start_consuming()
    except KeyboardInterrupt:
        print(" [x] Done")


if __name__ == '__main__':
    main()
