# is_qr.py
from jacobi import jacobi

def is_quadratic_residue(a, m):
    # If m is prime → Legendre gives full answer
    # If m composite → Jacobi(a/m)=1 is necessary but NOT sufficient!
    return jacobi(a, m) == 1

def main():
    a = int(input("a = "))
    m = int(input("m = "))
    print("Quadratic residue?" , is_quadratic_residue(a,m))

if __name__ == "__main__":
    main()
