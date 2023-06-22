from tkinter import *

# GUI function
def GUI():

    #inititalise the object
    gui = Tk()
    #give a title
    gui.title("Server Chat")
    #defining the dimensions of the window
    gui.geometry("380x430")

    #designing the components
    chatlog = Text(gui, bg='white')
    chatlog.config(state=DISABLED)

    
    sendbutton = Button(gui, bg='green', fg='white', text='SEND' )

    
    textbox = Text(gui, bg='white')

    #positioning the components
    chatlog.place(x=6, y=6, height=386, width=370)
    textbox.place(x=6, y=401, height=20, width=265)
    sendbutton.place(x=300, y=401, height=20, width=50)

    
    gui.mainloop()


if __name__ == '__main__':
    GUI()