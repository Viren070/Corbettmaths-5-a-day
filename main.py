from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import requests
import shutil

#taken from https://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal(num):
    # I'm checking for 10-20 because those are the digits that
    # don't follow the normal counting scheme. 
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        # the second parameter is a default.
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix
def help():
    messagebox.showinfo("Help","How to use: \n\nUsing the dropdown menus, select different dates and this program will produce the link to the questions or answers of the date you pick. This link can be copied or opened in a new tab. \n\nDifficulties: \n\nEach level is designed for different students depending on their aim\n\nNumeracy: Grades 1-3\nFoundation: Grades 3-4\nFoundation Plus: Grades 4-6\nHigher: Grades 6-7\nHigher Plus: Grades 8-9")
def credits():
    messagebox.showinfo("Credits","All questions and answers are from corbettmaths, I have only made a program to access these questions and answers.\nMade by Viren070 on Github.")
def validate():   #checks if there are any options that haven't been changed
    if clicked.get()!="Select month" and clicked2.get()!="Select day" and clicked3.get()!="Select type" and clicked4.get()!="Select Level":
        if (clicked.get()=="Feb" and int(clicked2.get()) > 29) or ((clicked.get()=="April" or clicked.get()=="June" or clicked.get() =="Sept" or clicked.get()=="Nov") and int(clicked2.get())>30):
            messagebox.showerror('Error', 'This day does not exist')
        else:
            return True   #if an option has been selected for each dropdown menu, it returns True. Otherwise it...
    else:    #...displays an error message and returns False 
        messagebox.showerror('Error','You must select a type, day and month first!')
        return False

def getLink():
        month=clicked.get()
        day=clicked2.get()     #receives selected inputs in dropdown menus
        pdfType=clicked3.get()
        difficulty=clicked4.get()
        
        if difficulty=="Higher Plus":
            if pdfType=="Answers":  #adjusts link format according to month and inserts given inputs into the format
                if month=="Dec":
                    link='https://corbettmaths.com/wp-content/uploads/2021/09/Higher-Plus-Ans-Dec_Part'+day+'.pdf'
                elif month=="April" or month=="May":
                    link='https://corbettmaths.com/wp-content/uploads/2021/08/HP-Ans-'+month+'-'+day+'.pdf'
                elif month=="March" or month=="June" or month=="July" or month=="Oct":
                    link="https://corbettmaths.com/wp-content/uploads/2021/09/HP-Ans-"+month+"-"+day+".pdf"
                else:
                    link='https://corbettmaths.com/wp-content/uploads/2021/08/Higher-Plus-Ans-'+month+'_Part'+day+'.pdf'
            elif pdfType=="Questions":
                  link='https://corbettmaths.com/wp-content/uploads/2021/08/Higher-Plus-'+month+'_Part'+day+'.pdf'

        elif difficulty=="Higher":
            if pdfType=="Questions":
                link='https://corbettmaths.com/wp-content/uploads/2021/08/Higher-'+month+'_Part'+day+'.pdf'
            elif pdfType=="Answers":
                link='https://corbettmaths.com/wp-content/uploads/2021/08/Higher-Ans-'+month+'_Part'+day+'.pdf'

        elif difficulty=="Foundation Plus":
            if pdfType=="Questions":
                link='https://corbettmaths.com/wp-content/uploads/2021/07/'+month+'-FP_Part'+day+'.pdf'
            elif pdfType=="Answers":
                if month=="Jan":
                    link='https://corbettmaths.com/wp-content/uploads/2022/01/Jan-FP-Answers.pdf#page='+day
                elif month=="December":
                    link='https://corbettmaths.com/wp-content/uploads/2021/08/FP-Ans-Dec.pdf#page='+day
                elif month=="March":
                    link='https://corbettmaths.com/wp-content/uploads/2021/07/March-FP-Ans.pdf#page='+day
                elif month=="Feb" or month=="April" or month=="May" or month=="June":
                    link='https://corbettmaths.com/wp-content/uploads/2021/07/'+month+'-FP-Answers.pdf#page='+day
                else:
                    link='https://corbettmaths.com/wp-content/uploads/2021/08/Nov-FP-Ans.pdf#page='+day





        elif difficulty=="Foundation":
            link=None
        elif difficulty=="Numeracy":
            link=None
        return link   #returns the link

def copyLink():
    global link
    if validate():
        link=getLink() #stores the link received from getLink() in a variable 
        root.clipboard_clear() #clears the clipboard
        root.clipboard_append(link) #adds the link to the clipboard
        root.update() # now it stays on the clipboard after the window is closed
        copyLinkButton.config(text="Copied!")
        run_periodically(linkCheck)

def loadPDF():
    if validate():  #ensures all inputs are given
        link=getLink()   #gets the link
        webbrowser.open(link, new=2)  #loads the link on a new tab

def linkCheck():
    if root.clipboard_get()!=link: #checks if the clipboard has changed 
        copyLinkButton.config(text="Copy Link") #if it has then, changes text to Copy Link

def run_periodically(func):  #function to run a function periodically 
    func() #runs the function
    root.after(1000, run_periodically, func) #after 1000ms it runs this function and the function to run creating a loop
    
def callback(*args):
    copyLinkButton.config(text="Copy Link")  #changes text from Copied to copy link
    if (clicked4.get()!="Select difficulty") and ((not (clicked4.get()=="Higher" or clicked4.get()=="Higher Plus" or clicked4.get()=="Foundation Plus"))):
        clicked4.set("Select difficulty")
        messagebox.showerror("Error","Only Higher Plus, Higher, and Foundation Plus are supported currently")
        
   

IconPath=os.getcwd()+"/icon.ico"

url='https://raw.githubusercontent.com/Viren070/Corbettmaths-5-a-day/main/icon.ico'

file_exists = os.path.exists('icon.ico')

if not file_exists:
    messagebox.showinfo("File missing","'icon.ico' file missing, downloading now")
    res = requests.get(url, stream = True)
    if res.status_code == 200:
        with open('icon.ico','wb') as f:
            shutil.copyfileobj(res.raw, f)
        messagebox.showinfo('Success!','Image sucessfully Downloaded:')
    else:
        messagebox.showerror('Error','Image Couldn\'t be retrieved')   


root=Tk()
root.title("Corbettmaths 5-a-day")
root.geometry( "400x150" )
try:
    root.iconbitmap(IconPath)
except TclError:
    messagebox.showerror("Error","'icon.ico' file missing")


 

root.resizable(False,False)   #makes the window un-resizable

#making lists with options for dropdown menus 
monthList = ["Jan", "Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]
dayList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
pdfTypeList= ["Questions","Answers"]
difficultyList=["Numeracy","Foundation","Foundation Plus","Higher","Higher Plus"]

#defining the widgets and their configs 
                    
clicked = StringVar()
clicked2= StringVar()  
clicked3 = StringVar()
clicked4 = StringVar()
clicked.set( "Select month" )
clicked2.set( "Select day" )
clicked3.set( "Select type" )
clicked4.set( "Select difficulty" )
clicked.trace("w", callback)    #
clicked2.trace("w", callback)   #when a change is detected in the variable, runs the callback function
clicked3.trace("w", callback)   #
clicked4.trace("w", callback)


#creating the dropdown menus and packing them into frames
Top=Frame(root)
top=Frame(root)
Top.pack(side=TOP,ipady=7)
top.pack(side=TOP)
top2=Frame(root)
top2.pack(side=TOP,ipady=17)


difficulty = OptionMenu(root, clicked4, *difficultyList)
difficulty.config(width=16)
pdfTypes = OptionMenu( root , clicked3 , *pdfTypeList )
pdfTypes.config(width=12)
days = OptionMenu( root, clicked2, *dayList ) 
days.config(width=12)
months= OptionMenu ( root, clicked, *monthList )
months.config(width=12)

Button(root,text="Help",width=6, font=("Times", 10),command=help).pack(in_=Top, side=LEFT)
difficulty.pack(in_=Top, side=LEFT)
Button(root,text="Credits",width=6, font=("Times", 10),command=credits).pack(in_=Top, side=LEFT)
pdfTypes.pack(in_=top, side=LEFT)
days.pack(in_=top, side=LEFT)
months.pack(in_=top, side=LEFT)
loadPDFButton=Button(root, text="Open PDF", font=("Times", 12), width=12, command=loadPDF)
copyLinkButton=Button(root, text="Copy Link", font=("Times", 12), width=12, command=copyLink)

loadPDFButton.pack(in_=top2, side=LEFT)
copyLinkButton.pack(in_=top2, side=LEFT)

root.mainloop()
