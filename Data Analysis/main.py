# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

data_dict = data.to_dict()
print(data_dict)

print(data.condition)

temp_list = data["temp"].to_list()
print(temp_list)

avg = sum(temp_list) / len(temp_list)
print(f"Avg temp is: {avg}")

print(f"Avg temp is: {data['temp'].mean()}")
print(f"The max temp is: {data['temp'].max()}")

print(data[data.day == "Monday"])

# The highest temperature row:
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday)
print(monday.temp)

# Monday's temperature in F.
print(monday.temp * 9 / 5 + 32)

# How to create DateFrame from data.
my_data_dict = {
    "students": ["Ahmet", "Mine", "Ayla"],
    "scores": [76, 56, 65]
}
the_data = pandas.DataFrame(my_data_dict)
print(the_data)
the_data.to_csv("students_data.csv")
