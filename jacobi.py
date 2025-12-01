# jacobi.py
def jacobi(a, n):
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be odd positive.")
    a %= n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0

def main():
    a = int(input("a = "))
    m = int(input("m (odd) = "))
    print(f"(a/m) = {jacobi(a,m)}")

if __name__ == "__main__":
    main()
