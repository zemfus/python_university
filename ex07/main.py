def get_new_dict(d1, d2: dict):
    ans = {}
    for i in d1.keys():
        if i in d2.keys():
            ans[i] = d1[i]
    return ans
        


def main():
    d1 = {1:10, 2:342, 67:67, 23234:3244}
    d2 = {1:10, 3:567, 67:67, 54:24523}
    
    print(get_new_dict(d1=d1, d2=d2))


if __name__ == "__main__":
    main()