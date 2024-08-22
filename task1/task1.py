import sys

def circular_array_path(n, m):
    path = []
    position = 0
    
    while True:
        path.append(position + 1)
        position = (position + m - 1) % n
        if position == 0:
            break
    
    return path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py n m")
        sys.exit(1)
    
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
    path = circular_array_path(n, m)
    
    print(''.join(map(str, path)))

    