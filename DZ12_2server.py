import asyncio
HOST = "localhost"
PORT = 54000
async def handle_echo(reader : asyncio.StreamReader, writer: asyncio.StreamWriter):
    data = None
    while True:
        data = await reader.read(1024)
        msg = data.decode()
        global list_of_numbers
        list_of_number = msg.split(" ")
        ioloop =  asyncio.get_event_loop()
        tasks = [
            ioloop.create_task(addition()),
            ioloop.create_task(substraction()),
            ioloop.create_task(multiplication())
        ]
        wait_tasks = asyncio.wait(tasks)
        ioloop.run_until_complete(wait_tasks)
        result = f"A+B={a}, A-B= {s},A*B={m}"
        writer.write(bytes(str(result), encoding="UTF-8"))
        await writer.drain()
        writer.close()
        await writer.wait_closed()
async def addition():
    global a
    a = int(list_of_numbers[0])+int(list_of_numbers[1])
    await asyncio.sleep(2)
    print(f"A+B={a}")
async def substraction():
    global s
    s = int(list_of_numbers[0]) - int(list_of_numbers[1])
    await asyncio.sleep(2)
    print(f"A-B={s}")
async def multiplication():
    global m
    m = int(list_of_numbers[0]) * int((list_of_numbers[1]))
    await asyncio.sleep(2)
    print(f"A*B={m}")
async def run_server():
    server = await asyncio.start_server(handle_echo,HOST,PORT)
    async with server:
        await server.serve_forever()
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(run_server())