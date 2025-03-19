#!/usr/bin/env python3
import os
import time

fifo_path = "./fifo"
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

with open(fifo_path, "w") as fifo:
    count = 0
    while True:
        message = f"Message {count}\n"
        fifo.write(message)
        fifo.flush()  # Ensure the message is sent immediately.
        print(f"Wrote: {message.strip()}")
        count += 1
        time.sleep(1)
