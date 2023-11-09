import asyncio
import sys
import time
import argparse
from collections import Counter
import aiohttp


async def fetch_worker(session, que):
    while True:
        url = await que.get()
        try:
            async with session.get(url) as resp:
                text = await resp.read()
                assert resp.status == 200

                url = resp.url  # is needed in case of redirect by url

                print(f'{url} \t {Counter(text.lower().split()).most_common(5)}')
        finally:
            que.task_done()


async def fill_queue(que, filename):
    with open(filename, 'r', encoding='utf-8') as text:
        for line in text:
            await que.put(line)


async def main(workers_c, filename):
    t1 = time.time()

    que = asyncio.Queue(workers_c)
    que_task = asyncio.create_task(fill_queue(que, filename))

    async with aiohttp.ClientSession() as session:
        workers = [
            asyncio.create_task(fetch_worker(session, que))
            for _ in range(workers_c)
        ]

        await que_task
        await que.join()

        for worker in workers:
            worker.cancel()

    t2 = time.time()
    print(t2 - t1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", type=int, help="workers count")
    parser.add_argument("filename", type=str, help="file next")
    args = parser.parse_args(sys.argv[1:])

    asyncio.run(main(args.c, args.filename))
