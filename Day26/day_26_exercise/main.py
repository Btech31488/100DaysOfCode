# with  open("file1.txt") as file:
#       file1 = file.readlines()



# with  open("file2.txt") as file:
#       file2 = file.readlines()



# result = [int(num.strip()) for num in file1 if num in file2]

# # Write your code above 👆

# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆

# # Write your code below:
# sentence_list = sentence.split()

# result1 = {word:len(word) for word in sentence_list}

# # word_amount = {word:}



# print(result1)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆


# # Write your code 👇 below:
# weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}


# print(weather_f)

student_dict = {
    "student": ["Alex", "Beth", "Caroline"],
    "score": [56, 76, 98]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through data frame
# for (key, value) in student_data_frame.items():
#     print(value)

#Loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Alex":
        print(row.score)

