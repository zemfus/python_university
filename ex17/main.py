import math

def get_square_triangle(d: dict):
    a = []
    a.append(math.sqrt(math.pow((d['x'][1] - d['x'][0]), 2) + math.pow((d['y'][1] - d['y'][0]), 2)))
    a.append(math.sqrt(math.pow((d['x'][2] - d['x'][0]), 2) + math.pow((d['y'][2] - d['y'][0]), 2))) 
    a.append(math.sqrt(math.pow((d['x'][2] - d['x'][1]), 2) + math.pow((d['y'][2] - d['y'][1]), 2)))
    return max(a)

def main():
    d = {'x':[0, 0.5, 2], 'y':[0, -0.5, 3]}
    print(get_square_triangle(d))

if __name__ == "__main__":
    main()