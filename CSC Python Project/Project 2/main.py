from tkinter import *
from request import *

window = Tk()

# Project title
window.title('Youtube Finder')
window.config(padx=100, pady=50)

# minimum size of window
window.minsize(width=500, height=200)

# application logo
logo = Label(text='YOUTUBE Finder', font=('Roboto', 15, 'bold'))
logo.pack()

instruction = Label(text='Welcome to the Youtube category finder. '
                         'Enter a query to search for.',
                    font=('Arial', 10))
instruction.pack()

searching = Label(text='', font=('Arial', 12, 'bold'))
searching.pack()

video_query = Entry(width=80)
video_query.pack()


def getinfo():
    searching.config(text='searching...')
    return_category_from_name(video_query.get())
    video_query.delete(0, END)
    searching.config(text='')


search_button = Button(text='Find Category', command=getinfo)
search_button.pack()

window.mainloop()
