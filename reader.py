#!/usr/bin/env python3
import os

fifo_path = "./fifo"
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

with open(fifo_path, "r") as fifo:
    while True:
        line = fifo.readline()
        if line:
            print("Received:", line.strip())
        else:
            # If no data is available, continue waiting.
            continue
