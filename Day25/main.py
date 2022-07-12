from numpy import average
import pandas

#data = pandas.read_csv("weather_data.csv")
# # # print(type(data))
# # print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# print(len(temp_list))

# print(data["temp"].mean())

# print(data["temp"].max())

#Get Data in Columns
# print(data["condition"])
# ########OR#############
# print(data.condition)

# #Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# #Monday Condition
# monday = data[data.day == "Monday"]
# print(monday.condition)

# #Coverting Monday temp from C to F
# monday_temp = int(monday.temp) 
# monday_temp_F = monday_temp * (9 / 5) + 32
# print(monday_temp_F)

# #Create a dataframe from scratch
# data_dict ={
#     "students": ["Amy", "Bob", "Max"],
#     "score": [75, 56, 65]
# }
# data_dict_table = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])

red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])



data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"], 
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = data_dict_table = pandas.DataFrame(data_dict)
df.to_csv("squirrel.count.csv")