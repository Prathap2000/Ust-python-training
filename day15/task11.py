from typing import List, Iterable, TypeVar

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

# Example usage:
user_ids = list(range(1, 10001))
chunk_size = 100

for chunk in chunk_data(user_ids, chunk_size):
    print(f"Processing chunk: {chunk[:3]}...{chunk[-3:]}")