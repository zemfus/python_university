def get_dictionary(a_r, a_n: dict):
    dict = {}
    for key in a_r.keys():
        if key in a_n.keys():
            dict[a_r[key]] = a_n[key]
            
    return dict

def main():
    a_r = {"Hello":"Привет", "Bye":"Пока", "One":"Один"}
    a_n = {"Hello":"Hallo", "One":"eines"}
    print(get_dictionary(a_r, a_n))

if __name__ == "__main__":
    main()