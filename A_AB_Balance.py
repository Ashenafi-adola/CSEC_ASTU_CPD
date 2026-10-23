t = int(input())
for _ in range(t):
    s = input()
    ab = s.count("ab")
    ba = s.count("ba")
    sl = list(map(str, s))
    if ab == ba:
        print(s)
    elif ab > ba:
        for i in range(ab-ba):
            a = sl.index("a")
            sl[a] = "b"
        print("".join(sl))
    else:
        for i in range(ba-ab):
            a = sl.index("b")
            sl[a] = "a"
        print("".join(sl))
    