# This is the first time that I started to code.


# This is for defining function called 'tiger'.
# This function takes one argument called 'x'.
def tiger(x):

    # print is a function that display something in the console
    print(x)


# This is for defining function called 'sal'.
# This function takes one argument called 'x'.
def sal(x):

    # This function add 3 to x and stock the result in a variable called 'habu'
    habu = x+3

    # This function will 'give back' the value stocked in habu
    return habu


if __name__ == "__main__":

    wolf = [1, 2, 3]

    # i will have as value sequentially each element of wolf
    for i in wolf:

        # 'tiger' displays the value of i in the console
        tiger(i)

        #  'sal' add 3 to the value of i
        # What sal gives back is socked in dragon
        dragon = sal(i)
        print(dragon)


# Output in the console will be:
# 1
# 4
# 2
# 5
# 3
# 6


