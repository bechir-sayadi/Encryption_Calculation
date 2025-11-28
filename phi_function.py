#!/usr/bin/env python3
import math

def prime_factors(n):
    """Return prime factorization as a dict {prime: exponent}."""
    factors = {}
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors


def phi(n):
    """Compute Euler's totient function φ(n)."""
    factors = prime_factors(n)
    result = n
    for p in factors:
        result = result * (p - 1) // p
    return result, factors


def units_mod_n(n):
    """Return the list of integers 1 <= a < n that are coprime to n."""
    return [a for a in range(1, n) if math.gcd(a, n) == 1]


def main():
    print("=== Euler Phi Function and Units of Z_n ===\n")

    n = int(input("Enter n: "))

    # Compute phi
    phi_n, factors = phi(n)

    print("\n--- Prime Factorization ---")
    if factors:
        print("n =", n, "=", " * ".join([f"{p}^{e}" for p, e in factors.items()]))
    else:
        print("n =", n, "has no prime factors? (n <= 1?)")

    print("\n--- Euler Phi ---")
    print(f"phi({n}) = {phi_n}")

    print("\n--- Units of Z_n (prime residue system) ---")
    units = units_mod_n(n)
    print(f"Z_*({n}) = {units}")
    print(f"Number of units: {len(units)}")

    print("\nFinished!\n")


if __name__ == "__main__":
    main()
