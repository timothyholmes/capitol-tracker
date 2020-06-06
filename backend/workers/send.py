import asyncio
import aiormq


async def main():
    # Perform connection
    connection = await aiormq.connect("amqp://guest:guest@localhost//")

    # Creating a channel
    channel = await connection.channel()

    # Sending the message
    await channel.basic_publish(b'Hello World!', routing_key='task_queue')
    print(" [x] Sent 'Hello World!'")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())