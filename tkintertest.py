from tkinter import *

#makes a window
root=Tk()
#puts text in the window 
myLabel = Label(root, text="This was pretty easy")

#titles the window 
root.title("Thesis time baby")

#file has to be .ico for this to work 
#root.iconbitmap(r'C:\Users\mmboo\Downloads\naturegirl.png')

#makes the text appear in window
myLabel.pack()

#prevents window from closing 
root.mainloop()