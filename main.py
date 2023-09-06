import math

import time


def round_float(val: float, precision: int) -> float:
    ratio = math.pow(10, float(precision))
    return round(val * ratio) / ratio


def secant(f, x0, x1, n):
    limit = 1000
    tolerance = 1e-6

    while n < limit:
        y0 = f(x0)  # initial value
        y1 = f(x1)  # next value
        dx = x1 - x0  # estimate difference
        dy = y1 - y0  # value difference

        if abs(dx) < tolerance:
            return x1

        h = -y1 * dx / dy  # step size
        x0 = x1  # new initial estimate
        x1 = x1 + h  # new next estimate
        n += 1

    return x1


def solve(f):
    # Initialize a container for roots
    roots = []
    # Set tolerance
    tolerance = 1e-8
    # Start, end, and step
    start = int(-100 * 10)
    end = int(100 * 10) + 1
    step = int(0.1 * 10)

    for guess in range(start, end, step):
        guess /= 10.0

        # Use the secant method to find a root for each initial guess
        root = secant(f, guess, guess + step, 0)

        # Check if the root is already found before appending
        found = False

        # Check if the root is NaN
        is_nan = math.isnan(root)

        # See if the root answer is at least 0 or up
        close_enough = f(root) < 1.0 or f(root) >= 0.0

        # If the root is already known, skip appending
        for r in roots:
            if abs(root - r) < tolerance:
                found = True
                break

        # Append the root to the container
        if not found and not is_nan and close_enough:
            roots.append(root)

    return roots


def main():
    # Define your function here
    def f(x):
        # return (6 * math.pow(x, 5)) + (3 * math.pow(x, 4)) + (3 * math.pow(x, 2)) + (5 * x) + 6 - 0
        # return math.pow(x, 2) - 2 * x - 24 - 0
        return math.pow(x, 2) + 1 / 3 * x + 5 / 6 - 0

    # timer starts
    start_time = time.time()

    # find the roots
    roots = solve(f)

    # print out the roots
    i = 0
    for r in roots:
        i += 1
        print(f"Root {i}: {round_float(r, 3):.3f}")

    # print time taken to find roots
    elapsed_time = time.time() - start_time
    print(f"Root finder took {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    main()
