from tkinter import*
import pygame

pygame.init()
root = Tk()
root.title("Who Wants to be a Millionaire")
root.geometry('1352x652+0+0')
root.configure(background ='black')

ABC = Frame(root, bg='black')
ABC.grid()

ABC1 = Frame(root, bg='black',bd=20, width=900, height=600)
ABC1.grid(row=0,column =0)
ABC2 = Frame(root, bg='black',bd=20, width=452, height=600)
ABC2.grid(row=0,column=1)

ABC1a = Frame(ABC1, bg='black',bd=20, width=900,padx=110, height=200)
ABC1a.grid(row=0,column =0)
ABC1b = Frame(ABC1, bg='black',bd=20, width=900, height=200)
ABC1b.grid(row=1,column =0)
ABC1c = Frame(ABC1, bg='black',bd=20, width=900, height=200)
ABC1c.grid(row=2,column =0)
#==================================Changing=============================
def Change50_50():
     canvas = Canvas(ABC1a,bg='black', width=180, height=80)
     canvas.grid(row=0,column=0)
     canvas.delete("all")
     image1 = PhotoImage(file = 'Cover50b.png')
     canvas.create_image(90,40, image =image1)
     canvas.images = image1

     
def PeopleChange():
     canvas = Canvas(ABC1a,bg='black', width=180, height=80)
     canvas.grid(row=0,column=1)
     canvas.delete("all")
     image1 = PhotoImage(file = 'BPeople.png')
     canvas.create_image(90,40, image =image1)
     canvas.images = image1

def ChangePhone():
     canvas = Canvas(ABC1a,bg='black', width=180, height=80)
     canvas.grid(row=0,column=2)
     canvas.delete("all")
     image1 = PhotoImage(file = 'BPhone.png')
     canvas.create_image(90,40, image =image1)
     canvas.images = image1

def MillionPicture1():
    canvas = Canvas(ABC2,bg='black', width=430 , height=600)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1 = PhotoImage(file = 'Picture1.png')
    canvas.create_image(215 ,300,image =image1)
    canvas.images = image1

def MillionPicture2():
    canvas = Canvas(ABC2,bg='black', width=430 , height=600)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1 = PhotoImage(file = 'Picture2.png')
    canvas.create_image(215,300, image =image1)
    canvas.images = image1

def MillionPicture3():
    canvas = Canvas(ABC2,bg='black', width=430 , height=600)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1 = PhotoImage(file = 'Picture3.png')
    canvas.create_image(215,300, image =image1)
    canvas.images = image1

def MillionPicture4():
    canvas = Canvas(ABC2,bg='black', width=430 , height=600)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1 = PhotoImage(file = 'Picture4.png')
    canvas.create_image(215,300, image =image1)
    canvas.images = image1

def MillionPicture5():
    canvas = Canvas(ABC2,bg='black', width=430 , height=600)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1 = PhotoImage(file = 'Picture5.png')
    canvas.create_image(215,300, image =image1)
    canvas.images = image1

#===================================1step=============================
CentreImage = PhotoImage(file = 'Centre.png')
LogoCentre = Button(ABC1b, image = CentreImage, bg='black', width=300, height=200)
LogoCentre.grid()

Image50_50 = PhotoImage(file = 'Cover50a.png')
Live50_50 = Button(ABC1a, image = Image50_50, bg='black', width=180, height=80, command = Change50_50) 
Live50_50.grid(row=0,column=0)

ImagePeople = PhotoImage(file = 'APeople.png')
LivePeople = Button(ABC1a, image = ImagePeople, bg='black', width=180, height=80,command = PeopleChange )
LivePeople.grid(row=0,column=1)

ImagePhone = PhotoImage(file = 'APhone.png')
LivePhone = Button(ABC1a, image = ImagePhone, bg='black', width=180, height=80,command=ChangePhone)
LivePhone.grid(row=0,column=2)

MillionImage = PhotoImage(file = 'Picture0.png')
MillionIMG = Button(ABC2, image = MillionImage, bg='black', width=430 , height=600)
MillionIMG.grid(row=0,column=0)


#====================================All questions==================

Question1 = StringVar()
Question2 = StringVar()
Question3 = StringVar()
Question4 = StringVar()

Answer1 = StringVar()
Answer2 = StringVar()
Answer3 = StringVar()
Answer4 = StringVar()

Question1.set("What is the argument specifier for an integer? ")
Answer1.set("%f")
Answer2.set("%c")
Answer3.set("%")
Answer4.set("%d")

def Question2():
    Question1.set("What is the argument specifier for a string? ")
    Answer1.set("%")
    Answer2.set("%f")
    Answer3.set("%s")
    Answer4.set("%d")
    MillionPicture1()
    
def Question3():
    Question1.set("How two different types of Python loops called?")
    Answer1.set("if/then")
    Answer2.set("else/while")
    Answer3.set("for/while")
    Answer4.set("if/else")
    MillionPicture2()

def Question4():
    Question1.set("What is the function that used to create iterators?")
    Answer1.set("Serialization")
    Answer2.set("Loops")
    Answer3.set("Generators")
    Answer4.set("Conditional Arguments")
    MillionPicture3()

def Question5():
    Question1.set("By whom Pythom was developed?")
    Answer1.set("Ada Lovelace")
    Answer2.set("Guido van Rossum")
    Answer3.set("Donald Knuth")
    Answer4.set("Jeenbekov ")
    MillionPicture4()



#====================================2step====================================

txtQuestion = Entry(ABC1c, font=('arial', 18,'bold'),bg='blue', fg='white',bd=5, width =44,
                   justify =CENTER, textvariable = Question1)
txtQuestion.grid(row =0, column=0, columnspan=4, pady=4)

lblQuestA = Label(ABC1c, font=('arial', 14,'bold'),text="A: ",bg='black', fg='white',bd=5,
                   justify =CENTER)
lblQuestA.grid(row =1, column=0, pady=4,sticky=W)

txtQuestion1 = Button(ABC1c, font=('arial', 14,'bold'),bg='blue', fg='white',bd=1, width =17,height=2,
                   justify =CENTER,textvariable = Answer1, command=Question3)
txtQuestion1.grid(row =1, column=1, pady =4)

lblQuestB = Label(ABC1c, font=('arial', 14,'bold'),text="B: ",bg='black', fg='white',justify =LEFT)
lblQuestB.grid(row =1, column=2,sticky=W)

txtQuestion2 = Button(ABC1c, font=('arial', 14,'bold'),bg='blue', fg='white',bd=1,width=17,height=2,
                   justify =CENTER,textvariable = Answer2,command=Question5)
txtQuestion2.grid(row =1, column=3, pady=4)

lblQuestC = Label(ABC1c, font=('arial', 14,'bold'),text="C: ",bg='black', fg='white',
                   justify =LEFT)
lblQuestC.grid(row =2, column=0, sticky=W)

txtQuestion3 = Button(ABC1c, font=('arial', 14,'bold'),bg='blue', fg='white',bd=1,width=17,height=2,
                   justify =CENTER,textvariable = Answer3, command=Question4 )
txtQuestion3.grid(row=2, column=1, pady=4)

lblQuestD = Label(ABC1c, font=('arial', 14,'bold'),text="D: ",bg='black', fg='white',
                  justify =LEFT)
lblQuestD.grid(row =2, column=2, sticky=W)

txtQuestion4 = Button(ABC1c, font=('arial', 14,'bold'),bg='blue', fg='white',bd=1,width=17,height=2,
                   justify =CENTER,textvariable = Answer4,command=Question2)
txtQuestion4.grid(row=2, column=3, pady=4)
















root.mainloop() 
