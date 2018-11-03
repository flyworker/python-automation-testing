def gass_sum(count=100):
    if type(count).__name__ != 'int':
        return "Error,type not supported"
    sum = 0
    for x in range(count):
        # tmp is the temperate value of th x+1.
        # e.g. when x = 0, tmp should be 1
        tmp = x + 1
        sum += tmp
    return sum


if __name__ == "__main__":
    gass_sum(100)
    gass_sum(-100)
