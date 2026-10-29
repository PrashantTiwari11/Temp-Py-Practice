import time

def main():
    input("Press Enter to start...")
    start=time.perf_counter()
    input("Running. Press Enter to stop...")
    minutes, seconds=divmod(time.perf_counter()-start,60)
    print(f"Elapsed: {int(minutes)} min {seconds:.2f} sec")

if __name__ == "__main__": main()
