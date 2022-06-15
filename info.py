with open("brute.py") as fp:
    for i, line in enumerate(fp):
        if "\xd0" in line:
            print i, repr(line)
