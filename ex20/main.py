def get_dict(d: dict):
    dict = {}
    for i in d:
        if d[i] < 10:
            dict[i] = d[i]
    return dict
    
def main():
    test = {1:1, 2:2, 3:3, 4:4, 5:5, 9:90}
    d = get_dict(test)
    print(d.keys())
    
if __name__ == "__main__":
    main()