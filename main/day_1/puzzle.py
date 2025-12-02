def solve_dial():
    position = 50               # dial starts at 50
    zero_count = 0              # how many times we land on 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]          # 'R' or 'L'
            amount = int(line[1:])       # number after R/L

            if direction == "R":
                position = (position + amount) % 100
            else:  # L
                position = (position - amount) % 100

            # Count every time we land on 0
            if position == 0:
                zero_count += 1

    print("Times ending on 0:", zero_count)


if __name__ == "__main__":
    solve_dial()
