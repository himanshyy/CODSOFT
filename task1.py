import tkinter
from tkinter import messagebox
import random

root = tkinter.Tk()

root.configure(bg="white")

root.title("to do list")

root.geometry("325x275")


tasks=[]

#tasks=["call mom", "buy a guitar", "eat shushi"]

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")        

def add_task():
    task=txt_input.get()
    if task!="":
      tasks.append(task)
      update_listbox()
    else:
        lbl_display["text"]  = "please enter the task"
    txt_input.delete(0,"end")    

def del_all():
    confirmed = messagebox.askyesno("Confirmation", "Please confirm! Do you want to delete all?")
    if confirmed == True:
      global tasks
      tasks=[]
      update_listbox()

def del_one():
    task=lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()    

def del_sort():
   pass
    


def sort_asc():
     tasks.sort()
     update_listbox()

def sort_desc():
     tasks.sort()
     tasks.reverse()
     update_listbox()


def choose_random():
    task= random.choice(tasks)
    lbl_display["text"]=task

def exit():
    pass

def show_number_of_tasks():
    number_of_tasks= len(tasks)
    msg="number of tasks: %s" %number_of_tasks

lbl_title = tkinter.Label(root, text="to-do-list", bg="white")
lbl_title.grid(row=0, column=0)

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=0, column=1)

txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=1, column=1)

btn_add_task=tkinter.Button(root, text="Add task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=1, column=0)

btn_del_all =tkinter.Button(root, text="Delete all", fg="green", bg="white", command=del_all)
btn_del_all.grid(row=2, column=0)

btn_del_one =tkinter.Button(root, text="delete", fg="green", bg="white", command=del_one)
btn_del_one.grid(row=3, column=0)

btn_sort_asc =tkinter.Button(root, text="sort (ASC)", fg="green", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4, column=0)

btn_sort_desc =tkinter.Button(root, text="sort (DESC)", fg="green", bg="white", command=sort_desc)
btn_sort_desc.grid(row=5, column=0)

btn_choose_random =tkinter.Button(root, text="choose random", fg="green", bg="white", command=choose_random)
btn_choose_random.grid(row=6, column=0)

btn_number_of_tasks =tkinter.Button(root, text="number of task", fg="green", bg="white", command=show_number_of_tasks)
btn_number_of_tasks.grid(row=7, column=0)

btn_exit =tkinter.Button(root, text="EXIT", fg="green", bg="white", command=exit)
btn_exit.grid(row=8, column=0)

lb_tasks= tkinter.Listbox(root)
lb_tasks.grid(row=2, column=1, rowspan=7)
root.mainloop()
