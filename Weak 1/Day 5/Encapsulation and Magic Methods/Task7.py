import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        elapsed = self.end - self.start
        print(f"Elapsed time: {elapsed:.6f} seconds")

with Timer():
    total = 0
    for i in range(1_000_000):
        total += i