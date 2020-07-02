import asyncio
import aiormq


async def main():
    # Perform connection
    connection = await aiormq.connect("amqp://user:password@localhost//")

    # Creating a channel
    channel = await connection.channel()

    # Sending the message
    world = b'Hello World!'
    await channel.basic_publish(world, routing_key='hello')
    print(" [x] Sent %r" % world)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
