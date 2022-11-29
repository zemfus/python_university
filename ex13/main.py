from collections import Counter
from functools import reduce

def top_l(d: dict):
    return Counter(reduce((lambda x, y: x + y), d.values())).most_common(1)[0][0], list(set(reduce((lambda x, y: x + y), d.values())))
# удачи в разборе этого говна, но оно работает


def main():
    dict = {
        "Nevolina":["Russia", "English"], 
        "Levin":["Russia", "English", "French"], 
        "Konic":["Ukranian"]
        }
    
    print(top_l(dict))

if __name__ == "__main__":
    main()