def solve_dial_method_click():
    position = 50          # starting position
    zero_count = 0         # count every click that lands at 0

    with open("./day_1/input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            amount = int(line[1:])

            # Simulate each individual click
            for _ in range(amount):
                if direction == "R":
                    position = (position + 1) % 100
                else:  # L
                    position = (position - 1) % 100

                # Count EVERY time a click lands on 0
                if position == 0:
                    zero_count += 1

    print("Clicks landing on 0:", zero_count)


if __name__ == "__main__":
    solve_dial_method_click()
