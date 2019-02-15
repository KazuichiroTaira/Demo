
def tiger(x):

    print(x)


def sal(x):

    habu = x * 10

    return habu


if __name__ == "__main__":

    wolf = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in wolf:

        tiger(i)

        dragon = sal(i)
        print(dragon)


# Output in the console will be:
# 1
# 4
# 2
# 5
# 3
# 6


