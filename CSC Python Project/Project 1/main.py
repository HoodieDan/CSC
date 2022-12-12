from tkinter import *
import pandas

# THEME_COLOUR = "#375362"
window = Tk()
window.title("Class Manager?")
window.config(padx=60, pady=60)

mean_score_label = Label()
max_score_label = Label()
min_score_label = Label()
best_student_label = Label()
sabi_student_label = Label()
non_sabi_student_label = Label()

image = PhotoImage(file="images.png")
picture = Canvas(width=440, height=244)
picture.create_image(220, 122, image=image)
picture.grid(row=0, column=3, columnspan=3)


def display_stats():
    data = pandas.read_csv("students_data.csv")
    scores = data["score"]
    mean_score = round(scores.mean(), 2)
    max_score = scores.max()
    min_score = scores.min()

    mean_score_label.config(text=f"MEAN SCORE: {mean_score}")
    max_score_label.config(text=f"MAXIMUM SCORE: {max_score}")
    min_score_label.config(text=f"MINIMUM SCORE: {min_score}")

    if max_score_label:  # The check is for when there is no data in the file
        max_score_label.grid(row=3, column=4)
    if min_score_label:  # This check too is for when there is no data in the file
        min_score_label.grid(row=4, column=4)
    if mean_score_label:  # Same here
        mean_score_label.grid(row=5, column=4)
    best_student = data[data.score == max_score]  # This is still a dataframe
    the_first_name = best_student["first_name"].tolist()[0]
    the_last_name = best_student["last_name"].tolist()[0]
    the_score = best_student["score"].tolist()[0]
    # So I got a list of highest scoring students (if they are more than one) and displayed only the first.

    best_student_label.config(
        text=f"Best student is {the_first_name.upper()} {the_last_name.upper()}. He scored {the_score}")
    best_student_label.grid(row=6, column=4)

    sabi_students = data[data.score > 70]
    names_of_sabi = sabi_students["last_name"].tolist()
    names_to_display = ""
    for name in names_of_sabi:
        names_to_display += f"\n{name}"
    sabi_student_label.config(text=f"Names of students who scored above 70: {names_to_display}")
    if names_of_sabi:
        sabi_student_label.grid(row=7, column=4)

    non_sabi_students = data[data.score < 40]
    names_of_non_sabi = non_sabi_students["last_name"].tolist()
    other_names_to_display = ""
    for names in names_of_non_sabi:
        other_names_to_display += f"\n{names}"
    non_sabi_student_label.config(text=f"Names of students who scored less than 40: {other_names_to_display}")
    if names_of_non_sabi:
        non_sabi_student_label.grid(row=8, column=4)


def submit_info():
    first_name = first_name_input.get()
    last_name = last_name_input.get()
    matric_no = matric_no_input.get()
    score = score_input.get()

    data = pandas.read_csv("students_data.csv")
    matic_nos = data["matric_no"].tolist()
    # print(matic_nos)
    # Put checks to make sure the user actually inputs correct  stuff like check to make sure matric no does not exist
    # Also make sure the score entry receives a number

    first_name_input.delete(0, END)
    last_name_input.delete(0, END)
    matric_no_input.delete(0, END)
    score_input.delete(0, END)
    # If all checks are soft you should clear inputs

    with open("students_data.csv", mode="a") as file:
        file.write(f"\n{first_name},{last_name},{matric_no},{score}")
        display_stats()


first_name_input = Entry(width=20)
first_name_input.grid(column=1, row=1)
first_name_label = Label(text="First name?")
first_name_label.grid(column=0, row=1)
# first_name_label.config(padx=20)

last_name_input = Entry(width=20)
last_name_input.grid(column=3, row=1)
last_name_label = Label(text="Surname?")
last_name_label.grid(column=2, row=1)

matric_no_input = Entry(width=20)
matric_no_input.grid(column=5, row=1)
matric_no_label = Label(text="Matric no?")
matric_no_label.grid(column=4, row=1)

score_input = Entry(width=20)
score_input.grid(column=7, row=1)
score_label = Label(text="Score: ")
score_label.grid(column=6, row=1)

submit_button = Button(text="Submit", command=submit_info)
submit_button.grid(row=1, column=8)

display_stats()

window.mainloop()
