# sqrt_mod_n.py
from sqrt_mod_p import sqrt_mod_prime
from cra import CRA

def sqrt_mod_n(a, p, q):
    """Compute the two 'essentially different' roots of a mod n = pq."""
    if p % 4 != 3 or q % 4 != 3:
        raise ValueError("Both p and q must be ≡ 3 (mod 4)")

    n = p * q

    rp1, rp2 = sqrt_mod_prime(a, p)
    rq1, rq2 = sqrt_mod_prime(a, q)

    # K0: (+rp , +rq)
    r0, _ = CRA([rp1, rq1], [p, q], verbose=False)

    # K2: (+rp , -rq)
    r1, _ = CRA([rp1, (-rq1) % q], [p, q], verbose=False)

    r0 %= n
    r1 %= n

    return r0, r1   # these are the 2 essentially different ones

def main():
    a = int(input("a = "))
    p = int(input("p = "))
    q = int(input("q = "))
    r0, r1 = sqrt_mod_n(a, p, q)
    print("Essential roots:", r0, r1)
    print("Full set:", {r0, (-r0)% (p*q), r1, (-r1)%(p*q)})

if __name__ == "__main__":
    main()
