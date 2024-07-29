import pandas
# declaration to find file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240729.csv")
# number of each color
grey_squirrels = len(data["Primary Fur Color"] == "Gray")
red_squirrels = len(data["Primary Fur Color"] == "Red")
black_squirrels = len(data["Primary Fur Color"] == "Black")
print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)
data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}
# change to new file
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")