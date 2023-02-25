import openpyxl
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

class seat():
    def __init__(self, sourceOfCopy, destination, cell):
        self.sourceOfCopy = sourceOfCopy
        self.destination = destination
        self.cell = cell
        

    

def sourceOfCopy_clicked():
    file_name = filedialog.askopenfilename(initialdir='~/')
    if file_name:
        v1.set(file_name)




if __name__ == "__main__":
    root = Tk()
    root.title('Dialogs')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    frame = ttk.Frame(root, padding=100)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.grid(sticky=(N, W, S, E))


    # Open File
    sourceOfCopy = ttk.Button(
        frame, text='コピー元', width=15,
        command=sourceOfCopy_clicked)
    sourceOfCopy.grid(row=0, column=0, sticky=(W))
    v1 = StringVar()
    l1 = ttk.Label(frame, textvariable=v1)
    l1.grid(row=0, column=1)
    


    root.mainloop()
