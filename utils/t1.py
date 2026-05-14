import matplotlib.pyplot as plt
import pandas as pd

students = ["ram", "shyam", "mukesh", "vikas"]
marks = [80, 90, 89, 85]
plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks") 
plt.title("Student Marks")
plt.show()