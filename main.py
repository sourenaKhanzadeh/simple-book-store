from tkinter import *
from database import *
from functools import partial

window = Tk()
window.title("BookStore")

def createLabel(t, r, c):
    label = Label(window, text=t)
    label.grid(row=r, column=c)
    return label

def createEntry(r, c):
    text  = Entry(window)
    text.grid(row=r, column=c)
    return text

def listBox(h ,w, r, c, ro, co):
    list1 = Listbox(window, height=h, width=w)
    list1.grid(row=r, column=c, rowspan=ro, columnspan=co)
    return list1

def createButton(text, w, r , c, command=None, **args):
    btn = Button(text=text, width=w, command=command)
    btn.grid(row=r, column=c)
    return btn

def viewAll(li):
    li.delete(0, END)
    for row in connect(view):
        li.insert(END, row)

def searchAll(li, aut, tit, year, isbn):
    li.delete(0, END)
    print(aut.get(), tit.get(), year.get(), isbn.get())
    for row in connect(search,
    title=tit.get(), author=aut.get(), year=year.get(), isbn=isbn.get()):
        li.insert(END, row)

def clearAll(li):
    li.delete(0, END)

createLabel("Title", 0, 0)
title = createEntry(0, 1)

createLabel("Year", 1, 0)
year = createEntry(1, 1)

createLabel("Author", 0, 2)
author = createEntry(0, 3)

createLabel("ISBN", 1, 2)
isbn = createEntry(1, 3)

list1 = listBox(6, 35, 2, 0, 6, 2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

createButton("View all", 12, 2,3, partial(viewAll, list1))
createButton("Search Entry", 12, 3,3,
             partial(searchAll,
                     list1,
                     author,
                     title,
                     year,
                     isbn))
createButton("Add Entry", 12, 4,3)
createButton("Update Selected", 12, 5,3)
createButton("Delete Selected", 12, 6,3)
createButton("Clear", 12, 7,3, partial(clearAll, list1))


window.mainloop()