# unix-fifo-demo

Minimal demonstration of a Unix FIFO (named pipe) using two Python programs:

- `reader.py` opens a FIFO for reading and prints each line it receives.
- `writer.py` opens the same FIFO for writing and sends `Message N` once per second.

This is meant to make FIFO behavior concrete (blocking, buffering, and how it differs from a regular file).

## Requirements

- Linux/macOS (or WSL)
- Python 3 (`python3`)

## Run It

Use two terminals in the repo directory:

```bash
python3 reader.py
```

```bash
python3 writer.py
```

You should see the writer printing `Wrote: Message N` and the reader printing `Received: Message N`.

## What To Notice

- The FIFO path is `./fifo`.
- The FIFO is created on-demand via `os.mkfifo("./fifo")` if it doesn't exist.
- `open("./fifo", "r")` and `open("./fifo", "w")` can block:
  - opening for read blocks until some process opens for write
  - opening for write blocks until some process opens for read
- `writer.py` calls `flush()` so each line is delivered immediately rather than sitting in a user-space buffer.

## Reset / Cleanup

If you want to start fresh:

```bash
rm -f fifo
```

Then re-run `reader.py` / `writer.py` and the FIFO will be recreated.

## Quick Experiments

- Replace `reader.py` with `cat`:

```bash
cat fifo
```

- Or replace `writer.py` with a shell loop:

```bash
while true; do echo "hi $(date)"; sleep 1; done > fifo
```
