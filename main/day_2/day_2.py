def is_repeated_twice(n: int) -> bool:
    """
    Returns True if n consists of some digit sequence repeated twice.
    Examples: 11, 1212, 999999, 123123, 446446
    """
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]   # first half equals second half


def solve_ids():
    total_sum = 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # a line can contain multiple ranges separated by commas
            parts = line.split(",")

            for part in parts:
                part = part.strip()
                if not part:
                    continue

                start_str, end_str = part.split("-")
                start = int(start_str)
                end = int(end_str)

                # loop through the full range
                for n in range(start, end + 1):
                    if is_repeated_twice(n):
                        total_sum += n

    print("Sum of all invalid IDs:", total_sum)


if __name__ == "__main__":
    solve_ids()
