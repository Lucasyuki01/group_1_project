def main():
    number = int(input("number?: "))
    n = int(input("digit?: "))
    nthdigit(number, n)


# main logic
def nthdigit(number: float, n: int) -> int:
    if isinstance(number, float) and n < 0:
        number *= 10 ** abs(n)
        n = 1
    r = number % (10**n)
    q = r // 10 ** (n - 1)
    print(int(q))
    return int(q)


if __name__ == "__main__":
    main()