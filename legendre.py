# legendre.py
from pow import pow_mod  # or built-in pow(a,b,m)

def legendre(a, p):
    """Compute the Legendre symbol (a/p) for odd prime p."""
    if a % p == 0:
        return 0
    # Euler criterion:
    ls = pow(a, (p - 1) // 2, p)
    if ls == p - 1:
        return -1
    return ls

def main():
    a = int(input("a = "))
    p = int(input("p (prime) = "))
    print(f"(a/p) = {legendre(a,p)}")

if __name__ == "__main__":
    main()
