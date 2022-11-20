import asyncio 
HOST = "localhost"
PORT = 54000
async def run_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    a = input('Number A:')
    b = input("NUmber B:")
    r = f"{a} {b}"
    writer.write(bytes(str(r)), encoding="UTF-8")
    await writer.drain()
    while True:
        data =  await reader.read(1024)
        if not data:
            raise Exception("socket closed")
        print(f"{data.decode()}")
if __name__ == "__main__":

    loop = asyncio.new_event_loop()
    loop.run_ until_complete(run_client())