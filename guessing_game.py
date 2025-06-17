import random


def main():
    while True:
        ans = random.randint(1, 1000)
        print(ans)
        break
    guessing_game(ans)

def guessing_game(ans):
    begin = 1
    end = 1000
    cnt = 1

    while cnt <= 10:
        i = input("Enter your guess from {} to {}: ".format(begin, end))
        num = int(i)

        if num != ans:
            print("Wrong! Guess count: {}".format(cnt))

            mid = (begin + end) // 2
            if ans <= mid:
                end = mid
            else:
                begin = mid
            cnt += 1
        else:
            print("You got it! The hidden number is {}".format(ans))
            print("It took you {} guess(es).".format(cnt))
            break

    if cnt == 11:
        print("Wrong guess!")

if __name__ == "__main__":
    main()