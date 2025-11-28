#!/usr/bin/env python3

def extended_euclid(a, b, verbose=True):
    """
    Extended Euclidean Algorithm (follows exactly the version from the PDF).
    Computes gcd(a,b) and finds integers s,t such that:
        gcd(a,b) = s*a + t*b
    """

    # Initialization (matches the PDF)
    a0, a1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    if verbose:
        print("\n--- Extended Euclidean Algorithm (EUKLID) ---")
        print(f"{'i':<3} {'a0':<10} {'a1':<10} {'q':<6} {'s0':<10} {'s1':<10} {'t0':<10} {'t1':<10}")
        print("-" * 80)
        i = 0
        print(f"{i:<3} {a0:<10} {a1:<10} {'-':<6} {s0:<10} {s1:<10} {t0:<10} {t1:<10}")

    # Main loop
    i = 1
    while a1 > 0:
        q = a0 // a1  # integer division

        # Perform the Euclidean step
        a0, a1 = a1, a0 - q * a1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1

        if verbose:
            print(f"{i:<3} {a0:<10} {a1:<10} {q:<6} {s0:<10} {s1:<10} {t0:<10} {t1:<10}")
            i += 1

    if verbose:
        print("-" * 80)
        print(f"Result: gcd = {a0}, s = {s0}, t = {t0}")
        print(f"Check: {s0}*{a} + {t0}*{b} = {s0*a + t0*b}")

    return a0, s0, t0   # gcd, s, t


def compute_inverse(x, m):
    """Return modular inverse of x mod m using extended Euclid."""
    g, s, _ = extended_euclid(x, m, verbose=False)
    if g != 1:
        return None
    return s % m


def main():
    print("=== Extended Euclidean Algorithm ===\n")

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    g, s, t = extended_euclid(a, b, verbose=True)

    print("\nFinal Result:")
    print(f"gcd({a}, {b}) = {g}")
    print(f"Cofactors: s = {s}, t = {t}")
    print(f"Verification: {s}*{a} + {t}*{b} = {s*a + t*b}")

    # ================================================================
    # NEW FEATURE: If gcd = 1, allow computing modular inverses
    # ================================================================
    if g == 1:
        print("\nSince gcd = 1, modular inverses exist.")
        print("What inverse do you want to compute?")
        print("1) a^(-1) mod b")
        print("2) b^(-1) mod a")
        print("3) Enter custom values")

        choice = input("Choose option (1/2/3): ").strip()

        if choice == "1":
            inv = compute_inverse(a, b)
            print(f"\nInverse of {a} mod {b} = {inv}")
            print(f"Check: ({a} * {inv}) mod {b} = {(a*inv) % b}")

        elif choice == "2":
            inv = compute_inverse(b, a)
            print(f"\nInverse of {b} mod {a} = {inv}")
            print(f"Check: ({b} * {inv}) mod {a} = {(b*inv) % a}")

        elif choice == "3":
            x = int(input("Enter number x: "))
            m = int(input("Enter modulus m: "))

            inv = compute_inverse(x, m)
            if inv is None:
                print(f"\nNo inverse exists because gcd({x}, {m}) ≠ 1.")
            else:
                print(f"\nInverse of {x} mod {m} = {inv}")
                print(f"Check: ({x} * {inv}) mod {m} = {(x*inv) % m}")

    else:
        print("\nSince gcd != 1, no modular inverse exists for a or b.\n")

    print("Finished!\n")


if __name__ == "__main__":
    main()
