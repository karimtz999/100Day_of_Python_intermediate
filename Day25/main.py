import pandas as pd  # Import the pandas library

# Ensure the file path is correct. Adjust the path if necessary.
file_path = "2.1 weather_data.csv"

try:
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(file_path)

    # Convert the DataFrame to a dictionary and print it
    data_dict = data.to_dict()
    print("Data as dictionary:", data_dict)

    # Example operations (uncomment and use as needed)

    # Convert the 'temp' column to a list
    temp_list = data["temp"].to_list()
    print("Temperature list:", temp_list)

    # Calculate the average temperature
    average = sum(temp_list) / len(temp_list)
    print(f"Average temperature: {average}")

    # Calculate and print the mean temperature using pandas
    print(f"Mean temperature: {data['temp'].mean()}")

    # Print the maximum temperature
    print(f"Maximum temperature: {data['temp'].max()}")

    # Print the 'condition' column
    print("Weather conditions:")
    print(data["condition"])

    # Print the row where the day is 'Monday'
    print("Data for Monday:")
    print(data[data.day == 'Monday'])

    # Convert Monday's temperature from Celsius to Fahrenheit
    monday = data[data.day == "Monday"]
    monday_temp = int(monday["temp"])  # Convert temperature to integer
    monday_temp_f = monday_temp * 9 / 5 + 32  # Celsius to Fahrenheit conversion
    print(f"Monday's temperature in Fahrenheit: {monday_temp_f}")

    # Create a new DataFrame with student data
    data_dict = {
        "student": ["any", "james", "angela"],
        "score": [76, 80, 10]
    }
    new_data = pd.DataFrame(data_dict)

    # Save the new DataFrame to a CSV file
    new_data.to_csv("new_data.csv", index=False)

except FileNotFoundError as e:
    # Handle the case where the file is not found
    print(f"Error: {e}")

# Checking the current working directory
import os

print("Current working directory:", os.getcwd())
# Change the directory if needed
# os.chdir('path_to_your_directory')
