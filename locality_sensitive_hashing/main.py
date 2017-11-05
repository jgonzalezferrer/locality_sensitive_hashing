from locality_sensitive_hashing.minhashing import MinHashing
from locality_sensitive_hashing.shingling import Shingling


def main():
    text = "The hash, then, is only stable if you don't restart the Python process or set PYTHONHASHSEED to a fixed " \
               "decimal number "

    editorial = "editorial"
    factorial = "factorial"

    editorial_shingle = Shingling(editorial, 5)
    factorial_shingle = Shingling(factorial, 5)

    min1 = MinHashing(editorial_shingle.shingles, 100)
    min2 = MinHashing(factorial_shingle.shingles, 100)

    print(min1.signature)
    print(min2.signature)
    print(len([i for i, j in zip(min1.signature, min2.signature) if i == j]) / len(min1.signature))


if __name__ == "__main__":
    main()
