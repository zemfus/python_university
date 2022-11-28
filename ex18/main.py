def get_dict(n, c: list):
    new_c = [i*3 for i in c]
    new_n = [i*i for i in n]
    d = dict(zip(new_c, new_n))
    return d

def main():
    numb = [1, 2, 3, 4, 5, 6, 7, 8]
    cymbl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    print(get_dict(numb, cymbl))


if __name__ == "__main__":
    main()