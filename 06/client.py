import argparse
import socket
import threading
import queue


class Client:
    def __init__(self, host, port, thread_count, file):
        if thread_count < 1:
            raise ValueError("M - threads count must be 1 or more")

        self.host = host
        self.port = port
        self.file = file
        self.thread_count = thread_count

        self.que = queue.Queue(self.thread_count * 2)

    def connect(self):
        ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ser.connect((self.host, self.port))

        msg = ser.recv(1024).decode('utf-8')

        if msg == 'Client connected':
            print(msg)
            threads = [
                threading.Thread(
                    target=self.listen,
                )
                for _ in range(self.thread_count)
            ]

            for thread in threads:
                thread.start()

            self.queue_gen()

            for thread in threads:
                thread.join()
        else:
            print("Wrong connection message from Server")
        ser.close()

    def queue_gen(self):
        with open(self.file, 'r', encoding='utf-8') as text:
            for line in text:
                self.que.put(line)
        self.que.put(None)

    def listen(self):
        while True:
            try:
                ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ser.connect((self.host, self.port))
                msg = ser.recv(1024).decode('utf-8')
            except (ConnectionResetError, ConnectionRefusedError):
                ser.close()
                break

            if msg == 'master':
                url = self.que.get(timeout=1)
                if url is None:
                    self.que.put(None)
                    break
                ser.send(url.encode('utf-8'))

            elif msg == 'worker':
                ser.send('ready'.encode('utf-8'))
                url, json_str = ser.recv(1024).decode('utf-8').split(" ", 1)
                print(f'{url}: {json_str}')

            ser.close()


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8080

    parser = argparse.ArgumentParser(description="Client-main")
    parser.add_argument("M", type=int, help="threads count")
    parser.add_argument("filename", type=str, help="filename.txt")
    args = parser.parse_args()

    if not args.filename.endswith(".txt"):
        raise ValueError("filename must ends with '.txt'")

    client = Client(host, port, args.M, args.filename)
    client.connect()
