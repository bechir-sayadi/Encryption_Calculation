def square_and_multiply(a, b, m, verbose=True):
    """
    Square & Multiply algorithm (from Part 2.6 of the PDF)
    Computes a^b mod m and optionally prints the steps.
    """

    u = a % m     # base reduced modulo m
    v = b         # exponent
    z = 1         # accumulator (result)

    if verbose:
        print("\n--- Square & Multiply Detailed Steps ---")
        print(f"Initial values: u = {u}, v = {v}, z = {z}")
        print("-" * 50)
        print(f"{'Step':<6} {'v':<8} {'odd?':<8} {'z (after)':<12} {'u^2 (after)':<12}")
        print("-" * 50)

    step = 1

    # Main algorithm loop
    while v > 0:
        odd = (v % 2 == 1)

        if odd:
            z = (z * u) % m
        
        u = (u * u) % m
        v_next = v // 2

        if verbose:
            print(f"{step:<6} {v:<8} {str(odd):<8} {z:<12} {u:<12}")

        v = v_next
        step += 1

    if verbose:
        print("-" * 50)

    return z


def main():
    print("=== Square & Multiply (Modular Exponentiation) ===")

    # User input
    a = int(input("Enter base (a): "))
    b = int(input("Enter exponent (b): "))
    m = int(input("Enter modulus (m): "))

    # Compute using SMA
    result = square_and_multiply(a, b, m, verbose=True)

    print(f"\nResult:")
    print(f"{a}^{b} mod {m} = {result}")
    print("\nFinished!\n")


if __name__ == "__main__":
    main()
