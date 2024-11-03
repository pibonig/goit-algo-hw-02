import queue
import random
import time

request_queue = queue.Queue()


def generate_request():
    request_id = random.randint(1000, 9999)
    request_queue.put(request_id)
    print(f"✅ New request {request_id} added to the queue.")


def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"🛠️ Processing request {request_id}...")
        time.sleep(1)
        print(f"🎉 Request {request_id} successfully processed!")
    else:
        print("🚫 The queue is empty, no requests to process.")


if __name__ == "__main__":
    try:
        while True:
            generate_request()
            time.sleep(random.uniform(0.5, 2))
            process_request()
            time.sleep(random.uniform(0.5, 2))
    except KeyboardInterrupt:
        print("\n⚠️ Forced exit from the program.")
