from Manip import carveDemo
import tkinter
import cv2
import PIL.Image, PIL.ImageTk

from Manip.seamCarve import *
from tkinter import *
import PIL
import cv2

PATH = './Sample/pika.png'

# def consecutiveCarve(iterPeriod):
#     img = cv2.normalize(cv2.imread(PATH), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
#     while True:
#         for i in range(iterPeriod):
#             img = carve_column(carve_row(img))
#         cv2.imshow("sample", img)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#
# consecutiveCarve(1)

root = Tk()
frame = Frame(root)

# frame configs
frame.grid(row=0, column=0, sticky="nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.geometry("1280x720")
root.title("Seam Carving Demo")
frame.configure(background='#e6e9ef')

el = Label(frame, text="Width:", font=("Calibri", 12), bg="#e6e9ef").grid(padx=(35, 0), column=0, sticky=NW,
                                                                          pady=(10, 25))
e = Entry(frame, font=("Calibri", 17), width=29)
e.config(bg="#ddeaff")
e.focus_set()
e.grid(row=1, column=0, pady=(0, 40), padx=(35, 0), ipady=8)

el2 = Label(frame, text="Height:", font=("Calibri", 12), bg="#e6e9ef").grid(padx=(35, 0), column=0, sticky=NW,
                                                                            pady=(10, 25))
e2 = Entry(frame, font=("Calibri", 17), width=29)
e2.config(bg="#ddeaff")
e2.focus_set()
e2.grid(row=3, column=0, pady=(0, 40), padx=(35, 0), ipady=8)

cv_img = cv2.cvtColor(cv2.imread(PATH), cv2.COLOR_BGR2RGB)

photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
pLabel = Label(image=photo)
pLabel.grid(row=0, column=1)

el3 = Label(frame, text="Photo Width: " + str(photo.width()), font=("Calibri", 12), bg="#e6e9ef").grid(row=6, column=0,
                                                                                                      padx=(35, 0),
                                                                                                      pady=(35, 0),
                                                                                                      sticky=NW)

el4 = Label(frame, text="Photo Width: " + str(photo.height()), font=("Calibri", 12), bg="#e6e9ef").grid(row=7, column=0,
                                                                                                       padx=(35, 0),
                                                                                                       pady=(10, 0),
                                                                                                       sticky=NW)


def callback():
    global cv_img
    global photo

    width = e.get()
    height = e2.get()

    try:
        for i in range(min(int(width), int(height))):
            cv_img = carve_column(carve_row(cv_img))
            photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

        pLabel = Label(image=photo)
        pLabel.grid(row=0, column=1)

    except ValueError:
        pass


convertb = Button(frame, text="resize", font=("Calibri", 20), width=15, command=callback)
convertb.grid(row=4, column=0, pady=(15, 0), padx=(0, 0), sticky=N)
convertb.config(bg="#c1d8ff")

root.mainloop()

