import json
import sys

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent = 4)

def fill_values(tests, values_dict):
    for test in tests:
        test_id = test["id"]
        if test_id in values_dict:
            test["value"] = values_dict[test_id]
        if "values" in test:
            fill_values(test["values"], values_dict)

def main(tests_file, values_file, report_file):
    tests_data = load_json(tests_file)
    values_data = load_json(values_file)
    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    fill_values(tests_data["tests"], values_dict)
    save_json(tests_data, report_file)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <tests_file> <values_file> <report_file>")
        sys.exit(1)

    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    report_file = sys.argv[3]
    main(tests_file, values_file, report_file)


    