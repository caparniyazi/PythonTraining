import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)

passed_students = {key: value for (key, value) in students_scores.items() if value > 60}
# print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
# print(words)
result = {word: len(word) for word in words}
# print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key: int(val * 9 / 5) + 32 for (key, val) in weather_c.items()}
# print(weather_f)

student_dic = {
    "student": ["Ali", "Jale", "Leyla"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
# for (key, val) in student_dic.items():
#     print(val)

import pandas

student_df = pandas.DataFrame(student_dic)
# print(student_df)

# Looping through data frame.
# for (key, val) in student_df.items():
#     print(val)

# Loop through the rows
# for (index, row) in student_df.iterrows():
#     if row.student == "Ali":
#         print(row.score)

# Create a list of the phonetic code words from a word that the user inputs.
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


def generate_phonetic():
    entered_word = input("Enter a word: ").upper()
    try:
        phonetics = [new_dict[letter] for letter in entered_word]
    except KeyError:
        print("Sorry, only only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetics)

generate_phonetic()