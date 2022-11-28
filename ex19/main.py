def get_dict(d: dict):
    dict = {}
    for i in d:
        if d[i]*d[i] > 50:
            dict[i] = d[i]
    return dict
    
def main():
    test = {1:1, 2:2, 3:3, 4:4, 5:5, 9:9}
    
    print(get_dict(test))
    
if __name__ == "__main__":
    main()