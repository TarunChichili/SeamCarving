from tkinter import *

from PIL import Image, ImageTk

class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)

        edit.add_command(label="Show Img", command=self.showImg)

        menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        load = Image.open("chat.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def client_exit(self):
        exit()

root = Tk()

root.geometry("400x300")

app = Window(root)

root.mainloop()