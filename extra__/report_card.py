from tkinter import *
from tkinter import messagebox

def generate_report():
    try:
        name = entry_name.get()

        m1 = float(entry1.get())
        m2 = float(entry2.get())
        m3 = float(entry3.get())
        m4 = float(entry4.get())
        m5 = float(entry5.get())

        total = m1 + m2 + m3 + m4 + m5
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        result = f"""
Student Name : {name}

Marks:
Subject 1 : {m1}
Subject 2 : {m2}
Subject 3 : {m3}
Subject 4 : {m4}
Subject 5 : {m5}

Total Marks : {total}/500
Percentage : {percentage:.2f}%

Grade : {grade}
"""

        output.config(text=result)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid marks!")

# GUI Window
root = Tk()
root.title("Student Report Card Generator")
root.geometry("500x600")

Label(root, text="Student Report Card", font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="Student Name").pack()
entry_name = Entry(root, width=30)
entry_name.pack()

Label(root, text="Subject 1 Marks").pack()
entry1 = Entry(root)
entry1.pack()

Label(root, text="Subject 2 Marks").pack()
entry2 = Entry(root)
entry2.pack()

Label(root, text="Subject 3 Marks").pack()
entry3 = Entry(root)
entry3.pack()

Label(root, text="Subject 4 Marks").pack()
entry4 = Entry(root)
entry4.pack()

Label(root, text="Subject 5 Marks").pack()
entry5 = Entry(root)
entry5.pack()

Button(root, text="Generate Report Card",
       command=generate_report,
       bg="green",
       fg="white").pack(pady=15)

output = Label(root, text="", justify=LEFT,
               font=("Courier", 11))
output.pack(pady=10)

root.mainloop()