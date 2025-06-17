def main():
    try:
        n = int(input("# rows: "))
        print_star(n)
    except ValueError:
        print("Please input a number")
    except:
        print("Occur some input error")


# mein logic
def print_star(n):
    # nested loops example
    # # The value of i increases with the outer loop, starting from 1.
    # for i in range(1, n + 1):
    # # prints a line of stars repeated i times.
    #     for j in range(i):
    #         print("*", end="")
    # # print an empty line
    #     print()

    # pattern 1
    print("pattern 1")
    emp_cnt = n - 1
    star_cnt = 1
    for _ in range(n):
        for _ in range(emp_cnt):
            print(" ", end="")
        for _ in range(star_cnt):
            print("*", end="")
        emp_cnt -= 1
        star_cnt += 2
        print()

    # pattern 2
    print("pattern 2")
    star_cnt = n
    for _ in range(n):
        for _ in range(star_cnt):
            print("*", end="")
        star_cnt -= 1
        print()

    # pattern 3
    print("pattern 3")
    star_cnt = 0
    for _ in range(n // 2):
        star_cnt += 1
        for _ in range(star_cnt):
            print("*", end="")
        print()

    if n % 2 == 1:
        for _ in range(star_cnt + 1):
            print("*", end="")
        print()

    for _ in range(n // 2):
        for _ in range(star_cnt):
            print("*", end="")
        star_cnt -= 1
        print()

    # pattern 4
    print("pattern 4")
    emp_cnt = -1
    star_cnt = n + 2
    for _ in range(n // 2):
        emp_cnt += 1
        star_cnt -= 2
        for _ in range(emp_cnt):
            print(" ", end="")
        for _ in range(star_cnt):
            print("*", end="")
        print()

    if n % 2 == 1:
        for _ in range(emp_cnt + 1):
            print(" ", end="")
        for _ in range(star_cnt - 2):
            print("*", end="")
        print()

    for _ in range(n // 2):
        for _ in range(emp_cnt):
            print(" ", end="")
        for _ in range(star_cnt):
            print("*", end="")
        emp_cnt -= 1
        star_cnt += 2
        print()

    # pattern 5
    print("pattern 5")
    emp_cnt = n // 2 + 1
    star_cnt = -1
    for _ in range(n // 2):
        emp_cnt -= 1
        star_cnt += 2
        for _ in range(emp_cnt):
            print(" ", end="")
        for _ in range(star_cnt):
            print("*", end="")
        print()

    if n % 2 == 1:
        for _ in range(emp_cnt - 1):
            print(" ", end="")
        for _ in range(star_cnt + 2):
            print("*", end="")
        print()

    for _ in range(n // 2):
        for _ in range(emp_cnt):
            print(" ", end="")
        for _ in range(star_cnt):
            print("*", end="")
        emp_cnt += 1
        star_cnt -= 2
        print()


if __name__ == "__main__":
    main()