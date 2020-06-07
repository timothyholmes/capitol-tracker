import sys
import asyncio
import aiormq


async def main():
    # Perform connection
    connection = await aiormq.connect("amqp://guest:guest@localhost//")

    routing_key = "test-queue"

    # Creating a channel
    channel = await connection.channel()

    message = " ".join(sys.argv[1:]) or "Hello World!"
    await channel.basic_publish(
        exchange="", routing_key=routing_key, body=bytes(message, "utf8")
    )
    print(" [x] Sent %r" % message)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
