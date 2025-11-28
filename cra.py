# ----------------------------------------------
# Extended Euclidean Algorithm
# Computes gcd(a,b) and Bezout coefficients
# ----------------------------------------------
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, s1, t1 = egcd(b, a % b)
    s = t1
    t = s1 - (a // b) * t1
    return g, s, t


# ----------------------------------------------
# Modular inverse using Extended Euclid
# ----------------------------------------------
def modinv(a, m):
    g, s, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f"No inverse for {a} modulo {m} (not coprime)")
    return s % m


# ----------------------------------------------
# Chinese Remainder Algorithm (CRA)
# matches exactly the algorithm in the PDF
# ----------------------------------------------
def CRA(r_list, m_list, verbose=True):
    """
    r_list = [r1, r2, ..., rk]
    m_list = [m1, m2, ..., mk] (pairwise coprime)

    Returns (x, M) such that:
        x ≡ r_i (mod m_i)
        M = product of all moduli
    """

    k = len(r_list)
    if k != len(m_list):
        raise ValueError("Lists r_list and m_list must have the same length")

    # Step 1
    M = m_list[0]
    x = r_list[0] % M

    if verbose:
        print("=== Chinese Remainder Algorithm ===\n")
        print(f"Initial: x = {x}, M = {M}\n")

    # Step 2
    for i in range(1, k):
        mi = m_list[i]
        ri = r_list[i]

        if verbose:
            print(f"--- Step {i} ---")
            print(f"Current x = {x}")
            print(f"Current M = {M}")
            print(f"Next congruence: x ≡ {ri} (mod {mi})")

        h = ((ri - x) * modinv(M % mi, mi)) % mi

        if verbose:
            print(f"M^-1 mod {mi} = {modinv(M % mi, mi)}")
            print(f"h = (ri - x) * M^-1 mod mi = {h}")

        x = x + h * M
        M = M * mi

        if verbose:
            print(f"Updated x = {x}")
            print(f"Updated M = {M}\n")

    x = x % M
    return x, M



# ----------------------------------------------
# Simple main function (optional)
# ----------------------------------------------
def main():
    print("=== CRA Demo ===")
    k = int(input("How many congruences? "))

    r_list = []
    m_list = []

    for i in range(k):
        r = int(input(f"Enter r_{i+1}: "))
        m = int(input(f"Enter m_{i+1}: "))
        r_list.append(r)
        m_list.append(m)

    x, M = CRA(r_list, m_list, verbose=True)

    print("\n=== Final Result ===")
    print(f"x = {x}  (mod {M})")



if __name__ == "__main__":
    main()
