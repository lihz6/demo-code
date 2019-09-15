def input_count(string):
    dp = 0
    for i, c in enumerate(string):
        if i == 0:
            dp = 2 if c.isupper() else 1
        elif c.isupper() and string[i - 1].islower():
            dp += 2
        elif c.islower() and string[i - 2: i].isupper():
            dp += 2
        else:
            dp += 1
    return dp


def input_count_2(string):
    upper_status, count = False, 0
    for p, n in zip(string, string[1:]+string[0]):
        if p >= 'a': # p.islower()
            if upper_status:
                count += 1
                upper_status = n >= 'a' # n.islower()
            count += 1
        else:
            if not upper_status:
                count += 1
                upper_status = n <= 'Z' # n.isupper()
            count += 1
    return count


def input_count_3(string):
    upper_status, count = False, 0
    for p, n in zip(string, string[1:]):
        if p >= 'a': # p.islower()
            if upper_status:
                count += 1
                upper_status = n >= 'a' # n.islower()
            count += 1
        else:
            if not upper_status:
                count += 1
                upper_status = n <= 'Z' # n.isupper()
            count += 1
    if upper_status and string[-1] <= 'Z':
        count += 1
    elif not upper_status and string[-1] >= 'a':
        count += 1
    else:
        count += 2
    return count


if __name__ == "__main__":
    assert input_count("a") == 1
    assert input_count("B") == 2
    assert input_count("Ba") == 3
    assert input_count("BBBAa") == 7
