"""Example of a function that searches through a list."""


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))

# Define a function named 'contains'
# Two parameters:
#   1. needle - the string we're searching for
#   2. haystack - the list we're searching for


def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithim: 
    #   For each item in the haystack 
    #       Test if it is equal to the needle
    #           If so, return 'True'
    for item in haystack:
        if item == needle:
            return True
    #   After testing all items, return 'False' bc the needle was not found
    # Returns 'True' if needle in haystack, 'False' otherwise
    return False


if __name__ == "__main__":
    main()
