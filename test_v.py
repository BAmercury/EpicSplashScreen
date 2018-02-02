
from time import sleep
import Tkinter as tk
import threading
import random

# from www.sunjay-varma.com

class SplashScreen(Frame):
    def __init__(self, master=None, width=0.4, height=0.3, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws*width) or width
        h = (useFactor and ws*height) or height
        # calculate position x, y
        x = (ws/2) - (w/2) 
        y = (hs/2) - (h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        self.master.overrideredirect(True)
        self.lift()

root = tk.Tk()
sp  = SplashScreen(root)
label = tk.Label(sp, width=45)
label.pack(side=TOP, expand=YES)
label.config(bg="#3366ff", justify=CENTER, font=("calibri", 29))
Button(sp, text="Press this button to kill the program", bg='red', command=root.destroy).pack(side=BOTTOM, fill=X)

def strings_from_file():



def update_test():
    


def main():

    # start a thread that will update text

    root.mainloop()


if __name__ == '__main__':
    main()
    
