def code(s: str, d: dict):
    for i in s:
        if i in d.keys():
            s = s.replace(i, d[i])
    return s
    
def decode(s: str, d: dict):
    rev_d = dict(zip(d.values(), d.keys()))
    for i in s:
        if i in rev_d.keys():
            s = s.replace(i, rev_d[i])
    return s

def main():
    str = "hi how are you"
    dict = {"h":"0", "a": "6"}
    s = code(s=str, d=dict)
    print(s)
    print(decode(s=s, d=dict))

if __name__ == "__main__":
    main()