import gradio as gr


def calculate_grade(name, english, maths, science, computer):
    total = english + maths + science + computer
    average = total / 4

    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 45:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade = "F"

    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"

    return f"""
Student Name: {name}

English: {english}
Mathematics: {maths}
Science: {science}
Computer: {computer}

Total Score: {total}
Average Score: {average:.2f}

Grade: {grade}
Result: {result}
"""


app = gr.Interface(
    fn=calculate_grade,
    inputs=[
        gr.Textbox(label="Student Name"),
        gr.Number(label="English Score"),
        gr.Number(label="Mathematics Score"),
        gr.Number(label="Science Score"),
        gr.Number(label="Computer Score"),
    ],
    outputs=gr.Textbox(label="Result"),
    title="Student Grade Calculator",
    description="Enter a student's scores to calculate total, average, grade, and result."
)

app.launch()