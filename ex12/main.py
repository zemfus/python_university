def create_dict(key, val: slice):
    return dict(zip(key, val))

def main():
    key = [1, 2, 3, 4, 5, 6, 7, 8]
    val = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
    
    print(create_dict(key=key, val=val))

if __name__ == "__main__":
    main()