import sys
import os
def read_numbers(file_path):
    with open(file_path, "r") as file:
        return [int(line.strip()) for line in file]
    
def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

def main():
    if len(sys.argv) != 2:
        print("Error")
        return
    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    nums = read_numbers(input_file)
    result = min_moves(nums)
    print(result)

if __name__ == "__main__":
    main()