def input_count(string):
    dp = 0
    for i, c in enumerate(string):
        if i == 0:
            dp = 2 if c.isupper() else 1
        elif c.isupper() and string[i - 1].islower():
            dp += 2
        elif c.islower() and string[i - 2 : i].isupper():
            dp += 2
        else:
            dp += 1
    return dp


if __name__ == "__main__":
    assert input_count("a") == 1
    assert input_count("B") == 2
    assert input_count("Ba") == 3
    assert input_count("BBBAa") == 7

