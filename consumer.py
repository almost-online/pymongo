import asyncio
import aiormq


async def on_message(message):
    """
    on_message doesn't necessarily have to be defined as async.
    Here it is to show that it's possible.
    """
    print(" [x] Received message", message)
    print("Message body is: %r" % message.body)


async def main():
    # Perform connection
    connection = await aiormq.connect("amqp://user:password@localhost/")

    # Creating a channel
    channel = await connection.channel()

    # Declaring queue
    deaclare_ok = await channel.queue_declare('hello')
    consume_ok = await channel.basic_consume(
        deaclare_ok.queue, on_message, no_ack=True
    )


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_forever()
