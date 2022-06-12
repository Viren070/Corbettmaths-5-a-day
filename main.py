from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from os.path import exists
import webbrowser
import os
import requests
import shutil
paperState=False
fiveState=False
PREFERENCE=None
ocrexamboard=False
if exists("options.txt"):
    with open("options.txt","r")as f:
        contents=f.read()
        if contents=="":
            PREFERENCE=None
        else:
            PREFERENCE=contents.replace("preference: ","")
else:
    with open("options.txt","w+") as f:
        PREFERENCE=None
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.option_add('*tearOff', False)

        menu = Menu(self.master)
        self.master.config(menu=menu)


        optionMenu = Menu(menu)
        optionMenu.add_command(label="Toggle Dark Mode", command=self.toggledark)
        optionMenu.add_command(label="Download Missing Files", command=self.downloadmissingfiles)
        menu.add_cascade(label="Options", menu=optionMenu)
        helpMenu = Menu(menu)
        helpMenu.add_command(label="Help for Papers", command=self.paperHelp)
        helpMenu.add_command(label="Help for 5-a-day", command=self.fiveHelp)
        helpMenu.add_command(label="Credits", command=self.credits)
        helpMenu.add_command(label="Open GitHub Page", command=self.loadgithub)
        menu.add_cascade(label="More", menu=helpMenu)

    def loadgithub(self):
        webbrowser.open('https://github.com/Viren070/Corbettmaths-Program', new=2)
    def downloadmissingfiles(self):
        if exists('icon.ico') and exists('Corbettmaths.png') and exists('Corbettmaths-dark.png'):
            messagebox.showinfo("Corbettmaths Program","No missing files detected")
        else:
            if not(exists('icon.ico')):
                messagebox.showinfo("Found missing file","'icon.ico' file missing - downloading now")
                downloadimage('https://raw.githubusercontent.com/Viren070/Corbettmaths-Program/main/icon.ico','icon.ico')
            if not(exists('Corbettmaths.png')):
                messagebox.showinfo("Found missing file","'Corbettmaths.png' file missing - downloading now")
                downloadimage('https://raw.githubusercontent.com/Viren070/Corbettmaths-Program/main/Corbettmaths.png','Corbettmaths.png')
            if not(exists('Corbettmaths-dark.png')):
                downloadimage('https://raw.githubusercontent.com/Viren070/Corbettmaths-Program/main/Corbettmaths-dark.png','Corbettmaths-dark.png')
        

 

    def toggledark(self):
        global DARK
        global lightlabel
        global darklabel
        global PREFERENCE
        if DARK:
            if PREFERENCE!="LIGHT":
                if messagebox.askyesno("Theme preference","Would you like to save your preference and always start with light mode?"):
                    with open("options.txt","w") as f:
                        f.write("preference: LIGHT")
                    PREFERENCE="LIGHT"
            DARK=False
            darklabel.pack_forget()
            lightlabel.pack()
            root['bg']='SystemButtonFace'
            imageframe['bg']='black'
            a['bg']='SystemButtonFace'
            a['fg']='SystemButtonFace'
            row1['bg']='SystemButtonFace'
            PAPERS['bg']='SystemButtonFace'
            PAPERS['fg']='black'
            toprow['bg']='SystemButtonFace'
            secondrow['bg']='SystemButtonFace'
            bottomrow['bg']='SystemButtonFace'
            predictedSet['bg']='SystemButtonFace'
            predictedSet['fg']='SystemButtonFace'
            Examboard['bg']='SystemButtonFace'
            Examboard['fg']='black'
            Paper['fg']='black'
            Paper['bg']='SystemButtonFace'
            OCRPapers['fg']='black'
            OCRPapers['bg']='SystemButtonFace'
            Tier['bg']='SystemButtonFace'
            Tier['fg']='black'
            Set['bg']='SystemButtonFace'
            Set['fg']='black'
            predictedSet['fg']='black'
            predictedSet['bg']='SystemButtonFace'
            Type['fg']='black'
            Type['bg']='SystemButtonFace'
            pAPER['bg']='SystemButtonFace'
            pAPER['fg']='black'
            Open['bg']='SystemButtonFace'
            Open['fg']='black'
            CopyLink['bg']='SystemButtonFace'
            CopyLink['fg']='black'
            togglePaper['bg']='SystemButtonFace'
            togglePaper['fg']='black'
            
            topframe['bg']='SystemButtonFace'
            topframe['fg']='black'
            Top['bg']='SystemButtonFace'
            top['bg']='SystemButtonFace'
            top2['bg']='SystemButtonFace'
            difficulty['bg']='SystemButtonFace'
            difficulty['fg']='black'
            pdfTypes['bg']='SystemButtonFace'
            pdfTypes['fg']='black'
            days['bg']='SystemButtonFace'
            days['fg']='black'
            months['bg']='SystemButtonFace'
            months['fg']='black'
            loadPDFButton['bg']='SystemButtonFace'
            loadPDFButton['fg']='black'
            copyLinkButton['bg']='SystemButtonFace'
            copyLinkButton['fg']='black'
            toggleFive['bg']='SystemButtonFace'
            toggleFive['fg']='black'
            
            
        else:
            if PREFERENCE!="DARK":
                if messagebox.askyesno("Theme preference","Would you like to save your preference and always start with dark mode?"):
                    with open("options.txt","w") as f:
                        f.write("preference: DARK")
                    PREFERENCE="DARK"
            DARK=True
            lightlabel.pack_forget()
            darklabel.pack()
            root['bg']='#3d3d3d'
            a['bg']='#3d3d3d'
            a['fg']='#3d3d3d'
            row1['bg']='#3d3d3d'
            PAPERS['bg']='#3d3d3d'
            PAPERS['fg']='white'
            toprow['bg']='#3d3d3d'
            secondrow['bg']='#3d3d3d'
            bottomrow['bg']='#3d3d3d'
            predictedSet['bg']='#3d3d3d'
            predictedSet['fg']='#3d3d3d'
            Examboard['bg']='#3d3d3d'
            Examboard['fg']='white'
            Paper['fg']='white'
            Paper['bg']='#3d3d3d'
            OCRPapers['fg']='white'
            OCRPapers['bg']='#3d3d3d'
            Tier['bg']='#3d3d3d'
            Tier['fg']='white'
            Set['bg']='#3d3d3d'
            Set['fg']='white'
            predictedSet['fg']='white'
            predictedSet['bg']='#3d3d3d'
            Type['fg']='white'
            Type['bg']='#3d3d3d'
            pAPER['bg']='#3d3d3d'
            pAPER['fg']='white'
            Open['bg']='#3d3d3d'
            Open['fg']='white'
            CopyLink['bg']='#3d3d3d'
            CopyLink['fg']='white'
            togglePaper['bg']='#3d3d3d'
            togglePaper['fg']='white'

            topframe['bg']='#3d3d3d'
            topframe['fg']='white'
            Top['bg']='#3d3d3d'
            top['bg']='#3d3d3d'
            top2['bg']='#3d3d3d'
            difficulty['bg']='#3d3d3d'
            difficulty['fg']='white'
            pdfTypes['bg']='#3d3d3d'
            pdfTypes['fg']='white'
            days['bg']='#3d3d3d'
            days['fg']='white'
            months['bg']='#3d3d3d'
            months['fg']='white'
            loadPDFButton['bg']='#3d3d3d'
            loadPDFButton['fg']='white'
            copyLinkButton['bg']='#3d3d3d'
            copyLinkButton['fg']='white'
            toggleFive['bg']='#3d3d3d'
            toggleFive['fg']='white'
            
        
    def paperHelp(self):
        messagebox.showinfo("Help","This resource provides either: \n- 4 sets of practice papers (each set with 3 papers)\n- Predicted papers for all exam boards (for 2022)")
    
    def fiveHelp(self):
        messagebox.showinfo("Help","How to use: \n\nUsing the dropdown menus, select different dates and this program will produce the link to the questions or answers of the date you pick. This link can be copied or opened in a new tab. \n\nDifficulties: \n\nEach level is designed for different students depending on their aim\n\nNumeracy: Grades 1-3\nFoundation: Grades 3-4\nFoundation Plus: Grades 4-6\nHigher: Grades 6-7\nHigher Plus: Grades 8-9")
    def credits(self):
        messagebox.showinfo("Credits","All questions and answers are from corbettmaths, I have only made a program to access these questions and answers.\nMade by Viren070 on Github.")
def FiveValidate():   #checks if there are any options that haven't been changed
    if clicked.get()!="Select month" and clicked2.get()!="Select day" and clicked3.get()!="Select type" and clicked4.get()!="Select difficulty":
        if (clicked.get()=="Feb" and int(clicked2.get()) > 29) or ((clicked.get()=="April" or clicked.get()=="June" or clicked.get() =="Sept" or clicked.get()=="Nov") and int(clicked2.get())>30):
            messagebox.showerror('Error', 'This day does not exist')
        else:
            return True   #if an option has been selected for each dropdown menu, it returns True. Otherwise it...
    else:    #...displays an error message and returns False 
        messagebox.showerror('Error','You must select a difficulty, type, day and month first!')
        return False

def FiveGetLink():
    
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

def FiveCopyLink():
    if FiveValidate():
        if copyLinkButton.cget('text')=='Copy Link':
            global link
            link=FiveGetLink() #stores the link received from getLink() in a variable 
            root.clipboard_clear() #clears the clipboard
            root.clipboard_append(link) #adds the link to the clipboard
            root.update() # now it stays on the clipboard after the window is closed
            copyLinkButton.config(text="Copied!")
            run_periodically(linkCheck)
        else:
            messagebox.showinfo("Corbettmaths 5 a day","The link has already been copied")

def FiveLoadPDF():
    if FiveValidate():  #ensures all inputs are given
        link=FiveGetLink()   #gets the link
        webbrowser.open(link, new=2)  #loads the link on a new tab

def linkCheck():
    if root.clipboard_get()!=link: #checks if the clipboard has changed 
        copyLinkButton.config(text="Copy Link") #if it has then, changes text to Copy Link
        CopyLink.config(text="Copy Link")

def run_periodically(func):  #function to run a function periodically 
    func() #runs the function
    root.after(1000, run_periodically, func) #after 1000ms it runs this function and the function to run creating a loop
    
def FiveCallback(*args):
    copyLinkButton.config(text="Copy Link")  #changes text from Copied to copy link
    if (clicked4.get()!="Select difficulty") and ((not (clicked4.get()=="Higher" or clicked4.get()=="Higher Plus" or clicked4.get()=="Foundation Plus"))):
        clicked4.set("Select difficulty")
        messagebox.showinfo("Feature coming soon","Only Higher Plus, Higher, and Foundation Plus are supported currently")
def topmost():
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
def on_closing():
    global fiveaday
    if messagebox.askokcancel("Quit", "Are you sure you want to exit?"):
        fiveaday=False
        root.destroy()
#------------
def resetVar():
    examboard.set("Select exam board")
    SET.set("Select set")
    tier.set("Select tier")
    OCRpapers.set("Select paper")
    PAPER.set("Select paper")
    predictedSET.set("Select set")
    TYPE.set("Select type")
def PaperCallback(*args):
    global paperTYPE
    global ocrexamboard
    CopyLink.config(text="Copy Link")
    
        
    if paper.get()=="Predicted Papers" and paperTYPE=="Practice":
        Examboard.pack(side=LEFT)
        pAPER.pack_forget()
        Set.pack_forget()
        predictedSet.pack(side=LEFT)
        pAPER.pack(side=LEFT)
        paperTYPE="Predicted"
        resetVar()
    elif examboard.get()=="OCR" and ocrexamboard==False:
        pAPER.pack_forget()
        Set.pack_forget()
        OCRPapers.pack(side=LEFT)
        predictedSet.pack(side=LEFT)
        ocrexamboard=True
        PAPER.set("Select paper")
    elif examboard.get()!="OCR" and ocrexamboard==True:
        ocrexamboard=False
        OCRpapers.set("Select paper")
        OCRPapers.pack_forget()
        pAPER.pack(side=LEFT)
    elif paper.get()=="Practice Papers" and paperTYPE=="Predicted":
        Examboard.pack_forget()
        pAPER.pack_forget()
        OCRPapers.pack_forget()
        resetVar()
        predictedSet.pack_forget()
        Set.pack(side=LEFT)
        pAPER.pack(side=LEFT)
        paperTYPE="Practice"
    
        
    

def PaperValidate():
    if (paper.get()=="Predicted Papers" and ((examboard.get()=="OCR" and OCRpapers.get()=="Select paper") or (examboard.get()!="OCR" and PAPER.get()=="Select paper") or predictedSET.get()=="Select set" or examboard.get()=="Select exam board")) or (paper.get()=="Practice Papers" and (SET.get()=="Select set" or PAPER.get()=="Select paper")) or TYPE.get()=="Select type" or tier.get()=="Select tier" or paper.get()=="Select paper type":
        messagebox.showerror("Error","Please ensure you have chosen an option from each menu first")
        return False
    else:
        return True
def PaperGetLink():
    TIER=tier.get()
    
    

    if paper.get()=="Practice Papers":
        setletter=SET.get().replace("Set ","")
        paperno=PAPER.get().replace("Paper ","")
        if TYPE.get()=="Questions":
            
            link="https://corbettmaths.com/wp-content/uploads/2019/04/"+tier.get()+"-Set-"+setletter+"-Paper-"+paperno+".pdf"
        elif TYPE.get()=="Answers":
        
            

            if ( (tier.get()=="Higher") and ( (SET.get()=="Set A" and PAPER.get()=="Paper 1") or (SET.get()=="Set B" and PAPER.get()=="Paper 1") or ((SET.get()=="Set C") and (PAPER.get()=="Paper 2" or PAPER.get()=="Paper 3")) or (SET.get()=="Set D" and PAPER.get()=="Paper 3"))) or ((tier.get()=="Foundation") and  ((SET.get()=="Set D") or ((SET.get()=="Set A") and  (PAPER.get()=="Paper 2" or PAPER.get()=="Paper 3")) or ((SET.get()=="Set B") and (PAPER.get()=="Paper 1" or PAPER.get()=="Paper 3")))):
                time="2019/04/"                                                                                                                                                                                                                                                                                                            
            elif ( (tier.get()=="Higher") and ( ((SET.get()=="Set A") and (PAPER.get()=="Paper 2")) or (SET.get()=="Set B" and PAPER.get()=="Paper 2") or (SET.get()=="Set C" and PAPER.get()=="Paper 1") or (SET.get()=="Set D" and PAPER.get()=="Paper 1"))):
                time="2019/05/"
            elif ( (tier.get()=="Higher" and SET.get()=="Set A" and PAPER.get()=="Paper 3") or (tier.get()=="Foundation" and SET.get()=="Set B" and PAPER.get()=="Paper 2")):
                time="2020/10/"
            elif ((tier.get()=="Foundation" and SET.get()=="Set C") and (PAPER.get()=="Paper 1" or PAPER.get()=="Paper 2")):
                time="2021/09/"
            elif tier.get()=="Higher" and SET.get()=="Set B" and PAPER.get()=="Paper 3":
                time="2019/09/"
            elif tier.get()=="Foundation" and SET.get()=="Set C" and PAPER.get()=="Paper 3":
                time="2020/02/"
            elif tier.get()=="Foundation" and SET.get()=="Set A" and PAPER.get()=="Paper 1":
                time="2020/11/"
            elif tier.get()=="Higher" and SET.get()=="Set D" and PAPER.get()=="Paper 2":
                time="2021/03/"
            else:
                messagebox.showerror("Error","Unable to find date for link")
                return None
                

            if ((((tier.get()=="Higher") and ((SET.get()=="Set A" and PAPER.get()=="Paper 3") or ((SET.get()=="Set B") and (PAPER.get()=="Paper 2" or PAPER.get()=="Paper 3")) or ((SET.get()=="Set C") and (PAPER.get()=="Paper 3" or PAPER.get()=="Paper 3"))))) or ((tier.get()=="Foundation") and ((SET.get()=="Set A" and PAPER.get()=="Paper 2") or (SET.get()=="Set B") or (SET.get()=="Set D") or ((SET.get()=="Set C") and (PAPER.get()=="Paper 2" or PAPER.get()=="Paper 3")) ))):
                linkFormat=TIER+"-"+setletter+"-"+paperno+"-Answers.pdf"
            elif tier.get()=="Higher" and SET.get()=="Set D":
                linkFormat=TIER+"-"+setletter+"-"+paperno+"-Answers-1.pdf"
            elif tier.get()=="Higher" and SET.get()=="Set A" and PAPER.get()=="Paper 2":
                linkFormat=TIER+"-"+setletter+paperno+"-Answers.pdf"
            elif tier.get()=="Higher" and SET.get()=="Set A" and PAPER.get()=="Paper 1":
                linkFormat=TIER+"-"+setletter+"-"+paperno+"-Answers-2-1.pdf"
            elif tier.get()=="Higher" and SET.get()=="Set B" and PAPER.get()=="Paper 1":
                linkFormat="Higher-B-1-Answers-1-1.pdf"
            elif tier.get()=="Higher" and SET.get()=="Set C" and PAPER.get()=="Paper 1":
                linkFormat="Higher-C1-Answers-2.pdf"
            elif tier.get()=="Foundation" and SET.get()=="Set A" and PAPER.get()=="Paper 3":
                linkFormat="Foundation-A-3-Answers-2.pdf"
            elif tier.get()=="Foundation" and SET.get()=="Set A" and PAPER.get()=="Paper 1":
                linkFormat="Foundation-A-1-Answers-1.pdf"
            elif tier.get()=="Foundation" and SET.get()=="Set C" and PAPER.get()=="Paper 1":
                linkFormat="Foundation-C1-Answers-.pdf"
            else:
                messagebox.showerror("Error","Unable to find link format")
                return None
            link="https://corbettmaths.com/wp-content/uploads/"+time+linkFormat
            

    elif paper.get()=="Predicted Papers":
        setletter=predictedSET.get().replace("Set ","")
        if examboard.get()=="OCR":
            paperno=OCRpapers.get().replace("Paper ","")
        else:
            paperno=PAPER.get().replace("Paper ","")
        if TYPE.get()=="Questions":
          #https://corbettmaths.com/wp-content/uploads/2022/03/2022-Edexcel-Higher-1A-Answers-1.pdf
          #https://corbettmaths.com/wp-content/uploads/2022/02/2022-Edexcel-Higher-Paper-3-Set-B.pdf
            link='https://corbettmaths.com/wp-content/uploads/2022/02/2022-'+examboard.get()+'-'+tier.get()+'-Paper-'+paperno+'-Set-'+setletter+'.pdf'
        elif TYPE.get()=="Answers":
            if (examboard.get()!="OCR") or ():
                link='https://corbettmaths.com/wp-content/uploads/2022/03/2022-'+examboard.get()+'-'+tier.get()+'-'+paperno+setletter+'-Answers.pdf'
            
    return link

def PaperOpen():
    if PaperValidate():  #ensures all inputs are given
        link=PaperGetLink()   #gets the link
        webbrowser.open(link, new=2)  #loads the link on a new tab
def PaperCopyLink():
    if PaperValidate():
        global link
      
        link=PaperGetLink()
        root.clipboard_clear() #clears the clipboard
        root.clipboard_append(link) #adds the link to the clipboard
        root.update() # now it stays on the clipboard after the window is closed
        CopyLink.config(text="Copied!")
        run_periodically(linkCheck)
        
def togglePAPERS():
    global paperState
    if paperState:
        toprow.pack_forget()
        secondrow.pack_forget()
        bottomrow.pack_forget()
        paperState=False
        togglePaper.config(text="Show")
    else:
        toprow.pack()
        secondrow.pack(pady=7)
        bottomrow.pack(pady=2)
        paperState=True
        togglePaper.config(text="Hide")
def toggleFive():
    global fiveState
    if fiveState:
        Top.pack_forget()
        top.pack_forget()
        top2.pack_forget()
        fiveState=False
        toggleFive.config(text="Show")
    else:
        Top.pack(side=TOP)
        top.pack(side=TOP, pady=15)
        top2.pack(side=TOP,pady=10)
        fiveState=True
        toggleFive.config(text="Hide")
def downloadimage(url, file_name):
    res = requests.get(url, stream = True)
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        
    else:
        if messagebox.askretrycancel('Error','Missing image file couldn\'t be downloaded. Do you want to try again? \n(you can try downloading the image files from the Github page)'):
            downloadimage(url, file_name)
    
        
if not(exists('icon.ico')):
    downloadimage('https://raw.githubusercontent.com/Viren070/Corbettmaths-Program/main/icon.ico','icon.ico')
if not(exists('Corbettmaths.png')):
    downloadimage('https://raw.githubusercontent.com/Viren070/Corbettmaths-Program/main/Corbettmaths.png','Corbettmaths.png')
if not(exists('Corbettmaths-dark.png')):
    downloadimage('https://raw.githubusercontent.com/Viren070/Corbettmaths-Program/main/Corbettmaths-dark.png','Corbettmaths-dark.png')
           
root=Tk()
app=Window(root)
root.title("Corbettmaths Program")
root.minsize(600,300)
root.resizable(False,False)
imageframe=Frame(root)
imageframe.pack()
try:
    root.iconbitmap('icon.ico')
    light = Image.open("Corbettmaths.png")
    light=light.resize((500,100))
    light = ImageTk.PhotoImage(light)
    lightlabel=Label(imageframe, image=light, padx=5)
    darkphoto = Image.open("Corbettmaths-dark.png")
    darkphoto=darkphoto.resize((500,100))
    darkphoto = ImageTk.PhotoImage(darkphoto)
    darklabel=Label(imageframe, image=darkphoto, padx=5)
    if PREFERENCE==None:
        
        lightlabel.pack()


   
except:
    pass




Topmost = Frame(root)
Topmost.pack()

a=Label(Topmost, text="Available Resources", font=("Times", 20), padx=20)
a.pack(side=LEFT)


row1=Frame(root)
row1.pack()
#-----------------------------PAPERS--------------------------------------
paperTYPE="Practice"
PAPERS=LabelFrame(row1, text="PAPERS",font=("Times", 13))
PAPERS.pack(side=LEFT)
toprow=Frame(PAPERS)
secondrow=Frame(PAPERS)
bottomrow=Frame(PAPERS)

ExamBoardList=["Edexcel","AQA","OCR"]
paperType=["Practice Papers","Predicted Papers"]
tierList=["Higher", "Foundation"]
setList=["Set A","Set B","Set C","Set D"]
typeList=["Questions","Answers"]
paperList=["Paper 1", "Paper 2", "Paper 3"]

OCRpaperList=["Paper 4","Paper 5", "Paper 6"]
OCRpapers=StringVar()
OCRpapers.set("Select paper")
OCRpapers.trace("w", PaperCallback)
OCRPapers=OptionMenu(secondrow, OCRpapers, *OCRpaperList)
OCRPapers.config(width=14)

predictedSetList=["Set A", "Set B"]
predictedSET=StringVar()
predictedSET.set("Select set")
predictedSET.trace("w", PaperCallback)
predictedSet=OptionMenu(secondrow, predictedSET, *predictedSetList)
predictedSet.config(width=14)



examboard=StringVar()
paper=StringVar()
tier=StringVar()
SET=StringVar()
TYPE=StringVar()
PAPER=StringVar()
examboard.set("Select exam board")
paper.set("Select paper type")
tier.set("Select tier")
SET.set("Select set")
TYPE.set("Select type")
PAPER.set("Select paper")
examboard.trace("w", PaperCallback)
paper.trace("w", PaperCallback)
tier.trace("w", PaperCallback)
SET.trace("w", PaperCallback)
TYPE.trace("w", PaperCallback)
PAPER.trace("w", PaperCallback)

Examboard=OptionMenu(toprow, examboard, *ExamBoardList)
Examboard.config(width=14)
Paper=OptionMenu(toprow, paper, *paperType)
Paper.config(width=14)
Tier=OptionMenu(secondrow, tier, *tierList)
Tier.config(width=14)
Set=OptionMenu(secondrow, SET, *setList)
Set.config(width=14)
Type=OptionMenu(secondrow, TYPE, *typeList)
Type.config(width=14)
pAPER=OptionMenu(secondrow, PAPER, *paperList)
pAPER.config(width=14)

Paper.pack(side=LEFT)
Type.pack(side=LEFT)
Tier.pack(side=LEFT)
Set.pack(side=LEFT)
pAPER.pack(side=LEFT)


Open=Button(bottomrow, text="Open", font=("Times", 12), width=12, command=PaperOpen)
CopyLink=Button(bottomrow, text="Copy Link", font=("Times", 12), width=12, command=PaperCopyLink)

Open.pack(side=LEFT)
CopyLink.pack(side=LEFT)


togglePaper=Button(PAPERS, text="Show", width=6, command=togglePAPERS)
togglePaper.pack(side=BOTTOM, pady=5)













#---------------------------5 A DAY----------------------------------------------
topframe=LabelFrame(row1, text="5 A DAY", font=("Times", 13))
topframe.pack(side=LEFT)




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
clicked.trace("w", FiveCallback)    #
clicked2.trace("w", FiveCallback)   #when a change is detected in the variable, runs the callback function
clicked3.trace("w", FiveCallback)   #
clicked4.trace("w", FiveCallback)


#creating the dropdown menus and packing them into frames
Top=Frame(topframe)
top=Frame(topframe)

top2=Frame(topframe)



difficulty = OptionMenu(topframe, clicked4, *difficultyList)
difficulty.config(width=16)
pdfTypes = OptionMenu( topframe , clicked3 , *pdfTypeList )
pdfTypes.config(width=12)
days = OptionMenu( topframe, clicked2, *dayList ) 
days.config(width=12)
months= OptionMenu ( topframe, clicked, *monthList )
months.config(width=12)


difficulty.pack(in_=top, side=LEFT)

pdfTypes.pack(in_=top, side=LEFT)
days.pack(in_=top, side=LEFT)
months.pack(in_=top, side=LEFT)
loadPDFButton=Button(topframe, text="Open", font=("Times", 12), width=12, command=FiveLoadPDF)
copyLinkButton=Button(topframe, text="Copy Link", font=("Times", 12), width=12, command=FiveCopyLink)

loadPDFButton.pack(in_=top2, side=LEFT)
copyLinkButton.pack(in_=top2, side=LEFT)

toggleFive=Button(topframe, text="Show", width=6, command=toggleFive)
toggleFive.pack(side=BOTTOM, pady=5)


#-------------------------------------------------------------------------








root.protocol("WM_DELETE_WINDOW", on_closing)
topmost()
if PREFERENCE=="DARK":
    DARK=False
    app.toggledark()
elif PREFERENCE=="LIGHT":
    DARK=True
    app.toggledark()
else:
    DARK=False
root.mainloop()
