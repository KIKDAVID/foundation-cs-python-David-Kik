import json

def sumTuples(tup1, tup2):
    return tuple(a + b for a, b in zip(tup1, tup2))

def exportToJson(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def importFromJson(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def main():
    while True:
        print("- - - - - - - - - - - - - - -")
        print("1. Sum Tuples")
        print("2. Export JSON")
        print("3. Import JSON")
        print("4. Exit")
        print("- - - - - - - - - - - - - - -")

        choice = input("Enter a choice: ")

        if choice == '1':
            try:
                tup1 = tuple(map(int, input("Enter the first tuple elements separated by spaces: ").split()))
                tup2 = tuple(map(int, input("Enter the second tuple elements separated by spaces: ").split()))
                if len(tup1) != len(tup2):
                    print("Error: Tuples should be of the same length.")
                else:
                    result = sumTuples(tup1, tup2)
                    print("Output:", result)
            except ValueError:
                print("Error: Please enter valid integer values for the tuples.")
        
        elif choice == '2':
            data = {'name': 'David', 'age': 42, 'city': 'Beirut', 'email':  'davidelkik@gmail.com', 'height':'177cm'}
            filename = "info.json"
            exportToJson(data, filename)
            print(f"Data exported to {filename} successfully.")
        
        elif choice == '3':
            try:
                filename = input("Enter the JSON file name to import data: ")
                result = importFromJson(filename)
                print("Data imported successfully:")
                print(result)
            except FileNotFoundError:
                print("Error: File not found. Please make sure the file exists and try again.")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option (1, 2, 3, or 4).")

if __name__ == "__main__":
    main()