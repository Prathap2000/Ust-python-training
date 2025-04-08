from typing import List, Iterable, TypeVar
import concurrent.futures
import time

T = TypeVar('T')

def chunk_data(data: List[T], chunk_size: int) -> Iterable[List[T]]:
    """
    Yields chunks of a list with a specified size using a generator.

    Args:
        data: The list of items to be chunked.
        chunk_size: The desired size of each chunk.

    Yields:
        A list representing a chunk of the input data.
    """
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def process_chunk(chunk: List[int]):
    """
    Simulates processing a chunk of data.
    """
    partial_chunk_str = f"{chunk[:3]}...{chunk[-3:]}"
    print(f"Processing chunk: {partial_chunk_str} - Started")
    # Simulate some CPU-intensive work
    time.sleep(0.1)
    print(f"Processing chunk: {partial_chunk_str} - Done")

if __name__ == "__main__":
    user_ids = list(range(1, 10001))
    chunk_size = 100

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_chunk, chunk) for chunk in chunk_data(user_ids, chunk_size)]
        concurrent.futures.wait(futures)

    print("All chunks processed.")