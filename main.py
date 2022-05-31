import webbrowser
from tkinter import *
from tkinter import messagebox
def show_text(title,text):
    messagebox.showerror(title, text)
def close():
    if clicked.get()!="Select month" and clicked2.get!="Select day" and clicked3.get!="Select type":
        root.destroy()
    else:
        show_text('Error','You must select a type, day and month!')

        

root = Tk()
root.title("Higher Plus 5-a-day")
root.geometry( "190x240" )
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
drop.pack()
drop2 = OptionMenu( root, clicked2, *options2 )
drop2.pack()
drop3= OptionMenu ( root, clicked, *options )
drop3.pack()


Button(
    root, 
    text="Open PDF", 
    font=("Times", 13),
    command=close
    ).pack()

root.mainloop()

month=clicked.get()
day=clicked2.get()
Type=clicked3.get()

if Type=="Answers":
  link='https://corbettmaths.com/wp-content/uploads/2021/08/HP-Ans-'+month+'-'+day+'.pdf'
  webbrowser.open(link, new=2)

  
elif Type=="Questions":
  link='https://corbettmaths.com/wp-content/uploads/2021/08/Higher-Plus-'+month+'_Part'+day+'.pdf'
  webbrowser.open(link, new=2)

print("In case a new tab did not open, here is the link: \n"+link)
    
    



















