def is_repeated_at_least_twice(n: int) -> bool:
    """
    Returns True if n consists of some digit sequence repeated at least twice.
    Examples (True): 11, 22, 99, 111, 1212, 123123123, 1010, 565656, 2121212121
    """
    s = str(n)
    length = len(s)

    # Try all possible substring lengths for the repeating block
    for sub_len in range(1, length // 2 + 1):
        if length % sub_len != 0:
            continue  # substring must divide the whole length

        repeat_count = length // sub_len
        if repeat_count < 2:
            continue  # must repeat at least twice

        block = s[:sub_len]
        if block * repeat_count == s:
            return True

    return False


def solve_ids_part2():
    total_sum = 0

    with open("../../main/day_2/input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # each line may contain multiple ranges separated by commas
            parts = line.split(",")

            for part in parts:
                part = part.strip()
                if not part:
                    continue

                start_str, end_str = part.split("-")
                start = int(start_str)
                end = int(end_str)

                # check every ID in the range
                for n in range(start, end + 1):
                    if is_repeated_at_least_twice(n):
                        total_sum += n

    print("Sum of all invalid IDs:", total_sum)


if __name__ == "__main__":
    solve_ids_part2()
