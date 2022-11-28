def get_sum_maxAndMin(d: dict):
    return max(d.values()) + min(d.values())

def main():
    test = {1:1, 2:2, 3:3, 4:4, 5:67, 6:-167}
    print(get_sum_maxAndMin(test))
    
    
if __name__ == "__main__":
    main()