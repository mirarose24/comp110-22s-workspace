"""Some examples of tender, loving function definitons."""


def love(name: str) -> str:
    """Given a name as a paramter, returns a loving string."""
    return f"I love you {name} !"


def spread_love(to: str, n: int) -> str:
    love_note: str = ""
    i: int = 0
    while i < n: 
        love_note += love(to) + "\n" 
        i += 1
    return love_note 
