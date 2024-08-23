import sys
import math

def read_circle_data(file_path):
    with open(file_path, "r") as file:
        center_coords = list(map(float, file.readline().strip().split()))
        radius = float(file.readline().strip())
    return center_coords, radius

def read_points_data(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            points.append(list(map(float, line.strip().split())))
    return points

def calculate_point_position(center, radius, point):
    distance = math.sqrt((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2)
    if distance == radius:
        return 0 
    elif distance < radius:
        return 1 
    else:   
        return 2 

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        return
    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    center, radius = read_circle_data(circle_file)
    points = read_points_data(points_file)

    for point in points:
        position = calculate_point_position(center, radius, point)
        print(position)

if __name__ == "__main__":
    main()
    