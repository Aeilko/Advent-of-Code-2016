
def count_char_occurances(inp: str) -> dict:
    r = {}

    for c in inp:
        if c not in r:
            r[c] = 1
        else:
            r[c] = r[c] + 1

    return r
