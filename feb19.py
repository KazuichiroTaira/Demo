# def is_tasty(fish, tasty):
#
#     if tasty:
#         print(f"{fish} is good")
#
#     else:
#         print(f"{fish} is a nightmare")


def is_tasty_according_to_me(fish):

    # if fish in ["salmon", "tuna"]:
    #
    #     print(f"{fish} is good")
    # comment above is same as below.

    good_fishes = ["salmon", "tuna", "fugu"]

    if fish in good_fishes:
        print(f"{fish} is good")

    else:
        print(f"{fish} is a nightmare")


def picky(fish):

    if fish == "salmon":

        print(f"{fish} is good")

    else:
        print("I want salmon!!")


if __name__ == "__main__":

    # # The different types of variable
    # tasty = 3  # Integer
    # tasty = 3.4 # Float
    # tasty = "3" # String
    # tasty = True # Boolean
    # tasty = [1, 2] # List
    # tasty = (1, 2)  # Tuple

    # is_tasty("cat fish", False)
    # is_tasty_according_to_me("tuna")

    kyounosakana = ["shark", "fugu", "uni", "tako", "ikura", "irabuchar", "tuna"]

    # for shiro in kyounosakana:
    #
    #     is_tasty_according_to_me(shiro)
    #
    for guu in kyounosakana:

        print(guu)

        picky(guu)
