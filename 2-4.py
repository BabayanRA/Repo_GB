a_str = "0123 012345678910 012345 012345678910111213"
wort = a_str.split()
for el, i in enumerate(wort, 1):
    if len(i) > 9:
        print(f"{el}) {i[:10]}")
    else:
        print(f"{el}) {i}")
