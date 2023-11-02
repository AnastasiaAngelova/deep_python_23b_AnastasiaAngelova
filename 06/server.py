import socket
import threading
import queue
import re
import json
import argparse
from collections import Counter
import requests


class Server:
    def __init__(self, host, port, worker_count, word_count):
        if worker_count < 1:
            raise ValueError("-w must be 1 or more")
        if word_count < 1:
            raise ValueError("-k must be 1 or more")

        self.worker_count = worker_count
        self.word_count = word_count

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(self.worker_count + 1)

        self.lock = threading.Lock()
        self.url_count = 0
        self.que = queue.Queue()

        print(f"Сonnection to host {host} on port {port} established")

    def run(self):
        client = self.server.accept()[0]
        client.send('Client connected'.encode('utf-8'))
        client.close()

        master_thread = threading.Thread(
                target=self.master,
            )

        master_thread.start()
        master_thread.join()

        self.server.close()
        print("all urls have been successfully pumped")

    def master(self):
        worker_threads = [
            threading.Thread(
                target=self.worker,
                name=f"worker-{i}",
            )
            for i in range(self.worker_count)
        ]

        for thread in worker_threads:
            thread.start()

        while True:
            client = self.server.accept()[0]
            client.send('master'.encode('utf-8'))

            data = client.recv(1024)

            if len(data) != 0:
                url = data.decode('utf-8')[:-1]
                self.que.put(url)
            else:
                self.que.put(None)
                break

            client.close()
        client.close()

        for thread in worker_threads:
            thread.join()

    def worker(self):
        while True:
            try:
                url = self.que.get(timeout=1)
            except queue.Empty:
                continue

            if url is None:
                self.que.put(None)
                print(f'worker finished')
                break

            request = requests.get(url, timeout=10)
            if request.status_code != 200:
                print('Status code is not 200')

            url = request.url   # is needed in case of redirect by url
            http = request.text

            js_freq = self.get_words_count_json(http)

            with self.lock:
                self.sender(js_freq, url)
                print(f'By workers have been processed {self.url_count} urls')

    def get_words_count_json(self, text):
        text = re.sub("[^A-Za-z]", " ", text).lower().split()
        freq = Counter(text).most_common(self.word_count)
        js_freq = json.dumps(dict(freq))
        return js_freq

    def sender(self, json_str, url):
        client = self.server.accept()[0]
        msg = url + ' ' + json_str
        client.send('worker'.encode('utf-8'))
        if client.recv(1024).decode('utf-8') == "ready":
            self.url_count += 1
            client.send(msg.encode('utf-8'))
        client.close()

    def socket_close(self):
        self.server.shutdown(socket.SHUT_RDWR)
        self.server.close()


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8080

    parser = argparse.ArgumentParser(description="Server-main")
    parser.add_argument("-w", type=int, help="worker count")
    parser.add_argument("-k", type=int, help="words count")
    args = parser.parse_args()

    server = Server(host, port, args.w, args.k)
    server.run()
