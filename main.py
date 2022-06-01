import webbrowser
from tkinter import *
from tkinter import messagebox
linkState=False
def validate():   #checks if there are any options that haven't been changed

    if clicked.get()!="Select month" and clicked2.get()!="Select day" and clicked3.get()!="Select type":
        return True   #if an option has been selected for each dropdown menu, it returns True. Otherwise it...
    else:    #...displays an error message and returns False 
        messagebox.showerror('Error','You must select a type, day and month first!')
        return False

def getLink():
        month=clicked.get()
        day=clicked2.get()     #receives selected inputs in dropdown menus
        pdfType=clicked3.get()

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
        return link   #returns the link

def hideLink():
        root.geometry("400x100")
        global linkState
        global T
        T["state"]=NORMAL
        T.delete("1.0","end")
        T["state"]=DISABLED
        
        linkState=False #changes to False, so next time it will show the link
        ToggleLinkButton.config(text="Show Link")
            
def showLink():
        global linkState
        global T
        
        link=getLink()  #gets the link with getLink() function
        T["state"]=NORMAL   #changing state to insert link into text box
        T.delete("1.0","end")
        root.geometry( "400x180" )
        T.insert(0.0, link)
        T["state"]=DISABLED
        linkState=True  #changes to True so next time, it hides the link
        ToggleLinkButton.config(text="Hide Link")

def toggleLink():
    if validate():  #if all inputs given then...
        if linkState: #this checks if a link is being shown currently. If True then...
            hideLink()   #...runs hideLink function which removes the link...
        else:      #...but if there is no link, then it runs the showLink function which shows the link based on given inputs
            showLink()  
            
def loadPDF():
    if validate():  #ensures all inputs are given
        link=getLink()   #gets the link
        webbrowser.open(link, new=2)  #loads the link on a new tab 
    
def callback(*args):
    hideLink()  #hides the link being shown when a selected input is changed
    
root=Tk()

root.title("Higher Plus 5-a-day")
root.geometry( "400x100" )
root.iconbitmap(r"C:\Users\viren\OneDrive\Desktop\Screenshot (2).ico")
root.resizable(False,False)   #makes the window un-resizable

#making lists with options for dropdown menus 

monthList = ["Jan", "Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]
dayList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
pdfTypeList= ["Questions","Answers"]

#defining the widgets and their configs 
                    
clicked = StringVar()
clicked2= StringVar()  
clicked3 = StringVar()
clicked.set( "Select month" )
clicked2.set( "Select day" )
clicked3.set( "Select type" )
clicked.trace("w", callback)    #
clicked2.trace("w", callback)   #when a change is detected in the variable, runs the callback function
clicked3.trace("w", callback)   #

#creating the dropdown menus and placing them in set coordinates
top=Frame(root)
top.pack(side=TOP)
top2=Frame(root)
top2.pack(side=TOP,ipady=20)
pdfTypes = OptionMenu( root , clicked3 , *pdfTypeList )
pdfTypes.config(width=12)
pdfTypes.pack(in_=top, side=LEFT)
days = OptionMenu( root, clicked2, *dayList ) 
days.config(width=12)
days.pack(in_=top, side=LEFT)
months= OptionMenu ( root, clicked, *monthList )
months.config(width=12)
months.pack(in_=top, side=LEFT)

loadPDFButton=Button(root, text="Open PDF", font=("Times", 12), width=12, command=loadPDF)
loadPDFButton.pack(in_=top2, side=LEFT)
ToggleLinkButton=Button(root, text="Show Link", font=("Times", 12), width=12, command=toggleLink)
ToggleLinkButton.pack(in_=top2, side=LEFT)

T = Text(root, height = 2, width = 46)
T["state"]=DISABLED   #makes it so nothing can be written into the text box 
T.pack() #places text widget



root.mainloop()


    
    



















