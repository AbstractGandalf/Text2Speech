from tkinter import *
import pyttsx3
engine = pyttsx3.init()


headFont= ('Courier', 28 , 'bold')

class Speaker:
    def __init__(self, master):
        #Tkinter GUI Window related properties
        master.title("Text 2 Speech !")   
        master.resizable(False, False) 
        master.geometry("495x440")

        # UI Widgets start from below
        headLabel = Label(master, 
                          text="Text 2 Speech Program",
                          bd=5,
                          relief='solid',
                          height=2,
                          width=22,
                          bg='yellow'

                          )
        headLabel.configure(font=headFont)
        headLabel.grid(columnspan=3,row=0,rowspan=2)
        
        title= Label(master, text="Type something below !", font=("Courier",18,'bold'),fg='red')
        title.grid(pady=10,row=3,columnspan=3,rowspan=2)

        textBox = Text (master, bg="white",fg="black",height=10,width=50,bd=4)
        textBox.grid(pady=10,padx=60)

        talkButton= Button(master,command=lambda: Speakboi(textBox.get("1.0",END)),bg="yellow", text="Speak it !",font=('Helvetica',20),bd=5)
        talkButton.grid(pady=3,padx=60)

        credit= Label(master, text="Made by Shreyas BS :)")
        credit.grid(pady=30)
        #End of Widgets

        #Main Text to speech function below 
        def Speakboi(inp):
            engine.say(inp)
            engine.runAndWait()



        

root = Tk()

mainProgram = Speaker(root)

root.mainloop()