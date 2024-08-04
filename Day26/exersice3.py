
with open("file1.txt") as file1:
    file_1_data = file1.readline()
with open("file2.txt") as file2:
    file_2_data = file2.readline()
result = [int(num) for num in file_1_data if num in file_2_data]
# Write your code above 👆

print(result)

