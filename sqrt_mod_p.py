# sqrt_mod_p.py
# Compute a square root of a modulo p (prime p)
# Complete standalone version using Tonelli–Shanks if needed.

def legendre(a, p):
    """Compute the Legendre symbol (a/p) using Euler's criterion."""
    a %= p
    if a == 0:
        return 0
    ls = pow(a, (p - 1) // 2, p)
    if ls == p - 1:
        return -1
    return ls


def sqrt_mod_p(a, p):
    """
    Compute a square root r of 'a' modulo prime p.
    Returns None if no solution exists.
    """

    a %= p

    # Check if a is a quadratic residue
    if legendre(a, p) != 1:
        return None

    # Easy case: p % 4 == 3
    if p % 4 == 3:
        r = pow(a, (p + 1) // 4, p)
        return r

    # -------------------------
    # Tonelli–Shanks algorithm
    # -------------------------

    # Write p-1 = q * 2^s, where q is odd
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    # Find a z which is a quadratic non-residue
    z = 2
    while legendre(z, p) != -1:
        z += 1

    # Initialize variables
    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)

    # Main Tonelli–Shanks loop
    while t != 1:
        # Find smallest i such that t^(2^i) ≡ 1 mod p
        i = 1
        t2i = pow(t, 2, p)
        while t2i != 1:
            i += 1
            t2i = pow(t2i, 2, p)

        # Update
        b = pow(c, 2 ** (m - i - 1), p)
        r = (r * b) % p
        t = (t * pow(b, 2, p)) % p
        c = pow(b, 2, p)
        m = i

    return r


def main():
    a = int(input("a = "))
    p = int(input("p (prime) = "))
    r = sqrt_mod_p(a, p)

    if r is None:
        print("No square root exists.")
    else:
        print(f"One root is r = {r}")
        print(f"The other root is p - r = {p - r}")


if __name__ == "__main__":
    main()
