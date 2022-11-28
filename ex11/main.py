def get_square_triangle(d: dict):
    return ((d['x'][1] - d['x'][0]) * (d['y'][2] - d['y'][0]) - (d['x'][2] - d['x'][0]) * (d['y'][1] - d['y'][0]))/2

def main():
    d = {'x':[0, 0.5, 2], 'y':[0, -0.5, 3]}
    print(get_square_triangle(d))

if __name__ == "__main__":
    main()