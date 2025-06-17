def main():
    number = int(input("number?: "))
    n = int(input("digit?: "))
    nthdigit(number, n)

    # test(234455.34)
    # test(123456)


# main logic
def nthdigit(number: float, n: int) -> int:
    if isinstance(number, float) and n < 0:
        number *= 10 ** abs(n)
        n = 1
    r = number % (10**n)
    q = r // 10 ** (n - 1)
    print(int(q))
    return int(q)


# testcode
def test(number: float):
    reversed_number = str(number)[::-1]
    if isinstance(number, float):
        fractional_part, int_part = reversed_number.split(".")
        fractional_list, int_list = list(fractional_part[::-1]), list(int_part)

        for i in range(1, len(fractional_list) + 1):
            ans = fractional_list[i - 1]
            print(
                "nthdigit({}, {}) == {}: {}".format(
                    number, -i, ans, nthdigit(number, -i) == int(ans)
                )
            )
    else:
        int_list = list(reversed_number)

    for i in range(1, len(int_list) + 1):
        ans = int_list[i - 1]
        print(
            "nthdigit({}, {}) == {}: {}".format(
                number, i, ans, nthdigit(number, i) == int(ans)
            )
        )


if __name__ == "__main__":
    main()