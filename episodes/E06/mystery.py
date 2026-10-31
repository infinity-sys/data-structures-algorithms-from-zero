def mystery(s):
    if s == "":
        return ""
    return mystery(s[1:]) + s[0]

print(mystery("abc"))
print(mystery("recursion"))
print(mystery("level"))
