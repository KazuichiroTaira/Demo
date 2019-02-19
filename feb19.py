def is_tasty(fish, tasty):

    if fish is tasty:
        print(f"{fish} is good")

    else:
        print(f"{fish} is a nightmare")


def is_tasty_according_to_me(fish):

    if fish in ["salmon", "tuna"]:
        print(f"{fish} is good")

    else:
        print(f"{fish} is a nightmare")


if __name__ == "__main__":

    # # The different types of variable
    # tasty = 3  # Integer
    # tasty = 3.4 # Float
    # tasty = "3" # String
    # tasty = True # Boolean
    # tasty = [1, 2] # List
    # tasty = (1, 2)  # Tuple

    # is_tasty("cat fish", False)
    is_tasty_according_to_me("tuna")
