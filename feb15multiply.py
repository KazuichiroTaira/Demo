# def yankee(x):
#
#     print(x)


def candle(x):

    flame = 100 * x

    # return 100 * x
    return flame


if __name__ == "__main__":

    catchingrays = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # for i in range(11):
    for i in catchingrays:

        ribaiasan = candle(i)

        # yankee(ribaiasan) this is same as print and as a default it does not have meaning
        # unless you want to have custom

        print(i, ribaiasan)

