import webbrowser
from tkinter import *
from tkinter import messagebox
def show_text(title,text):
    messagebox.showerror(title, text)
def close():
    if clicked.get()!="Select month" and clicked2.get!="Select day" and clicked3.get!="Select type":
        return True
    else:
        show_text('Error','You must select a type, day and month!')
        return False

def task():
    if close():
        month=clicked.get()
        day=clicked2.get()
        Type=clicked3.get()

        if Type=="Answers":
            if month=="Dec":
                link='https://corbettmaths.com/wp-content/uploads/2021/09/Higher-Plus-Ans-Dec_Part'+day+'.pdf'
            elif month=="April" or month=="May":
                link='https://corbettmaths.com/wp-content/uploads/2021/08/HP-Ans-'+month+'-'+day+'.pdf'
            elif month=="March" or month=="June" or month=="July" or month=="Oct":
                link="https://corbettmaths.com/wp-content/uploads/2021/09/HP-Ans-"+month+"-"+day+".pdf"
            else:
                link='https://corbettmaths.com/wp-content/uploads/2021/08/Higher-Plus-Ans-'+month+'_Part'+day+'.pdf'
            



          
        elif Type=="Questions":
          link='https://corbettmaths.com/wp-content/uploads/2021/08/Higher-Plus-'+month+'_Part'+day+'.pdf'
    webbrowser.open(link, new=2)
        
    T["state"]=NORMAL
    T.delete("1.0","end")
    T.insert(0.0, "In case a new tab did not open, here is the link: \n\n"+link)
    T["state"]=DISABLED
         


        

root = Tk()
root.title("Higher Plus 5-a-day")
root.geometry( "400x220" )
options = [
	"Jan",
	"Feb",
	"March",
	"April",
	"May",
	"June",
	"July",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec"
]
options2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
options3= ["Questions","Answers"]

                    
clicked = StringVar()
clicked2= StringVar()
clicked3 = StringVar()


clicked.set( "Select month" )
clicked2.set( "Select day" )
clicked3.set( "Select type" )

drop = OptionMenu( root , clicked3 , *options3 )
drop.place(x=25,y=5)
drop2 = OptionMenu( root, clicked2, *options2 )
drop2.place(x=140,y=5)
drop3= OptionMenu ( root, clicked, *options )
drop3.place(x=255,y=5)
Button(root, text="Open PDF", font=("Times", 13), command=task).place(x=156,y=50)
drop.config(width=12)
drop2.config(width=12)
drop3.config(width=12)

T = Text(root, height = 6, width = 40)
T.place(x=40,y=100)
T.insert(0.0, "In case the PDF does not open, the link will appear here")
T["state"]=DISABLED

root.mainloop()


    
    



















