def DoWork():
    print("Doing work in a separate thread")
    # Simulate some work
    import time
    time.sleep(1)
    print("Work done")
    
def main():
    import threading
    
    print("Starting main thread")
    
    # Create a thread to run the DoWork function
    worker_thread_01 = threading.Thread(target=DoWork)
    worker_thread_02 = threading.Thread(target=DoWork)
    
    # Start the threads
    worker_thread_01.start()
    worker_thread_02.start()
    
    # Wait for the threads to finish
    worker_thread_01.join()
    worker_thread_02.join()
    
    print("All work done in separate threads")

if __name__ == "__main__":
    main()
    