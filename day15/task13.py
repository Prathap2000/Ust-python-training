from typing import Iterable

def progress_tracker(total_steps: int) -> Iterable[str]:
    """
    Yields progress percentages as strings.

    Args:
        total_steps: The total number of steps in the process.

    Yields:
        A string representing the current progress percentage.
    """
    for step in range(1, total_steps + 1):
        percentage = (step / total_steps) * 100
        yield f"Progress: {int(percentage)}%"

# Example usage:
for p in progress_tracker(5):
    print(p)

print("\nAnother example with more steps:")
for p in progress_tracker(10):
    print(p)