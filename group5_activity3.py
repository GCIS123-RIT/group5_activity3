import csv

def load_data():
    """
    Function to load data from a CSV file.
    
    Returns:
        list: Data loaded from the CSV file.
    """
    file_path = input("Enter the path to the CSV file: ")
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        # Print columns and ask user to choose one
        print("Columns in the CSV file:")
        idx = 1
        for column in data[0]:
            print(f"{idx}. {column}")
            idx += 1
        
        while True:
            column_choice = int(input("Choose the column to process: ")) - 1
            if column_choice >= 0 and column_choice < len(data[0]):
                break
            else:
                print("Invalid column number. Please choose a valid column.")
        
        # Checking if the chosen column contains numerical data
        while not all(row[column_choice].replace('.', '').isdigit() for row in data[1:]):
            print("Chosen column must contain numerical data.")
            column_choice = int(input("Choose the column to process: ")) - 1
            
        # Save the chosen column as an array of strings
        column_data = [row[column_choice] for row in data[1:]]
        
        print("Data loaded successfully.")
        return column_data
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")
        return load_data()

def clean_and_prepare_data(data):
    """
    The purpose of this function is to clean and prepare the loaded data.

    Args:
        data (list): Data to be cleaned.

    Returns:
        list: Cleaned data.
    """
    empty_value = input("Enter the replacement value for empty cells (min/max/avg): ")
    if empty_value == "min":
        replacement = find_minimum(data)
    elif empty_value == "max":
        replacement = find_maximum(data)
    elif empty_value == "avg":
        replacement = calculate_average(data)
    else:
        print("Invalid choice. Using default value (min).")
        replacement = find_minimum(data)
    # Replace empty values with the chosen replacement
    cleaned_data = []
    for value in data:
        if value == '':
            cleaned_data.append(replacement)
    else:
        cleaned_data.append(float(value))

    print("Data cleaned and prepared successfully.")
    return cleaned_data

def find_minimum(column):
    """
    The purpose of this function is to find the minimum value in a column.

    Args:
        column (list): Data column.

    Returns:
        float: Minimum value.
    """
    min_value = float('inf')
    for value in column:
        if value and float(value) < min_value:
            min_value = float(value)
    return min_value

def find_maximum(column):
    """
    The purpose of this function is to find the maximum value in a column.

    Args:
        column (list): Data column.

    Returns:
        float: Maximum value.
    """
    max_value = float('-inf')
    for value in column:
        if value and float(value) > max_value:
            max_value = float(value)
    return max_value

def calculate_average(column):
    """
    The purpose of this function is to calculate the average value of a column.

    Args:
        column (list): Data column.

    Returns:
        float: Average value.
    """
    sum_values = 0
    count = 0
    for value in column:
        if value:
            sum_values += float(value)
            count += 1
    return sum_values / count if count else 0

def insertion_sort(arr, ascending=True):
    """
    The purpose of this function is to sort the data using the Insertion Sort algorithm.

    Args:
        arr (list): Data to be sorted.
        ascending (bool): Sorting order, True for ascending, False for descending.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j] > key) if ascending else (arr[j] < key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def analyze_data(data):
    """
    The purpose of this function is to analyze the data.

    Args:
        data (list): Data to be analyzed.

    Returns:
        list: Analyzed data.
    """
    try:
        sort_order = input("Choose sorting order (ascending/descending): ").lower()
        if sort_order not in ["ascending", "descending"]:
            raise ValueError("Invalid sorting order. Please choose 'ascending' or 'descending'.")
        ascending = True if sort_order == "ascending" else False
        insertion_sort(data, ascending)
        print("Data analyzed successfully.")
        return data
    except Exception as e:
        print("Error during data analysis:", e)

def visualize_data(data):
    """
    The purpose of this function is to visualize the data.

    Args:
        data (list): Data to be visualized.
    """
    try:
        print("Visualizing the data:")
        idx = 0
        for value in data:
            num_stars = min(int(float(value) / 5), 20)
            print('*' * num_stars)
            idx += 1
    except Exception as e:
        print("Error during data visualization:", e)


def main():
    """
    Main function to run the CLI Data Analysis Tool.

    This function serves as the entry point for the program. It displays a menu to the user and allows them
    to interactively choose different data analysis functionalities.

    The user is presented with the following options:
    1. Load Data: Allows the user to load data from a CSV file.
    2. Clean and Prepare Data: Cleans and prepares the loaded data for analysis.
    3. Analyze Data: Performs analysis on the loaded and prepared data.
    4. Visualize Data: Visualizes the analyzed data.

    The function repeatedly prompts the user for input until they choose to exit the program.

    """

    data = [] # Initialize an empty list to store data
    
    while True:
        print("Welcome to the CLI Data Analysis Tool")
        print("1. Load Data")
        print("2. Clean and Prepare Data")
        print("3. Analyze Data")
        print("4. Visualize Data")
        choice = input("Enter your choice (1/2/3/4): ") # Prompt user for choice

        if choice == "1": # Load data option
            data = load_data()
        elif choice == "2": # Clean and prepare data option
            if not data:
                print("Please load the data first.")
            else:
                data = clean_and_prepare_data(data)
        elif choice == "3": # Analyze data option
            if not data:
                print("Please load and clean the data first.")
            else:
                data = analyze_data(data)
        elif choice == "4": # Visualize data option
            if not data:
                print("Please load, clean, and analyze the data first.")
            else:
                visualize_data(data)
        else: # Invalid choice
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
