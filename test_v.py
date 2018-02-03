
from time import sleep
from Tkinter import *
import threading
import random
import ttk

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

root = Tk()
sp  = SplashScreen(root)
sp.config(bg="#3366ff")
label = Label(sp, width=45)
label.pack(side=TOP, expand=YES)
label.config(bg="#3366ff", justify=CENTER, font=("calibri", 29))
Button(sp, text="Press this button to kill the program", bg='red', command=root.destroy).pack(side=BOTTOM, fill=X)




strings = []


# Thanks to https://github.com/livibetter for the ttk progress bar example
ft = ttk.Frame()
fb = ttk.Frame()
ft.pack(expand=True, fill=BOTH,side=TOP)
fb.pack(expand=True,fill=BOTH,side=TOP)
pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate')
pb_hD = ttk.Progressbar(ft, orient='horizontal', mode='indeterminate')
pb_vd = ttk.Progressbar(fb, orient='vertical', mode='determinate')
pb_vD = ttk.Progressbar(fb, orient='vertical', mode='indeterminate')

pb_hd.pack(expand=True, fill=BOTH, side=TOP)
pb_hD.pack(expand=True, fill=BOTH, side=TOP)
pb_vd.pack(expand=True, fill=BOTH, side=LEFT)
pb_vD.pack(expand=True, fill=BOTH, side=LEFT)

pb_hd.start(50)
pb_hD.start(50)
pb_vd.start(50)
pb_vD.start(50)


def strings_from_file():
    global strings
    #foo = ['a', 'b', 'c', 'd', 'e']
    with open('Phrases.txt','r') as myfile:
        strings = myfile.read().splitlines()


def update_test():
    strings_from_file()

    while True:
        #print('here')
        sleep(0.5)
        string = random.choice(strings)
        label.config(text=string)
        label.pack(side=TOP, expand=YES)
        label.config(bg="#3366ff", justify=CENTER, font=("calibri", 29))


def main():

    # start a thread that will update text
    string_thread = threading.Thread(target=lambda:update_test())
    string_thread.start()

    root.mainloop()


if __name__ == '__main__':
    main()
    
