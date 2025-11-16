import tkinter as tk
from tkinter import ttk, messagebox
from database import Student, Session

session = Session()

def add_student():
    name = name_entry.get()
    major = major_entry.get()
    
    if not name or not major:
        messagebox.showerror("Error", "Both Name and Major fields must be filled in.")
        return
    
    new_student = Student(name=name, major=major)
    session.add(new_student)
    session.commit()
    messagebox.showinfo("Success", f"Student '{name}' has been added successfully!")
    name_entry.delete(0, tk.END)
    major_entry.delete(0, tk.END)
    view_students()

def view_students():
    for item in tree.get_children():
        tree.delete(item)
    
    students = session.query(Student).all()
    for student in students:
        tree.insert("", "end", values=(student.id, student.name, student.major))

def delete_student():
    selected_item = tree.selection()[0]
    item_values = tree.item(selected_item, "values")
    student_id = item_values[0]
    
    student = session.query(Student).filter_by(id=student_id).first()
    session.delete(student)
    session.commit()
    messagebox.showinfo("Success", "Student deleted!")
    view_students()

root = tk.Tk()
root.title("Student Record Manager")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Major:").grid(row=1, column=0, padx=10, pady=10)
major_entry = tk.Entry(root, width=30)
major_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Add Student", command=add_student).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="View Students", command=view_students).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Delete Selected", command=delete_student).grid(row=2, column=2, padx=10, pady=10)

tree = ttk.Treeview(root, columns=("ID", "Name", "Major"), show="headings", height=10)
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Major", text="Major")
tree.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
