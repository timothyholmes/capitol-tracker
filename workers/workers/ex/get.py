import asyncio
import aiormq
import aiormq.types
import time


async def on_message(message: aiormq.types.DeliveredMessage):
    print(" [x] Received message %r" % (message,))
    print("     Message body is: %r" % (message.body.decode("utf-8"),))
    time.sleep(message.body.count(b"."))


async def main():
    # Perform connection
    connection = await aiormq.connect("amqp://guest:guest@localhost/")

    routing_key = "test-queue"

    # Creating a channel
    channel = await connection.channel()
    await channel.basic_qos(prefetch_count=1)

    # Declaring queue
    declare_ok = await channel.queue_declare(routing_key, durable=True)

    # Start listening the queue with name 'task_queue'
    await channel.basic_consume(declare_ok.queue, on_message, no_ack=True)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# we enter a never-ending loop that waits for data and runs
# callbacks whenever necessary.
print(" [*] Waiting for messages. To exit press CTRL+C")
loop.run_forever()
