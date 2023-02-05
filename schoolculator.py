import tkinter as tk
from tkinter import messagebox
from tkinter import Entry
from tkinter import Scrollbar
from tkinter import Canvas
import math

HIGHLIGHTED_FONT=("Verdana", 12)
SMALL_FONT=("Verdana", 10)
AVERAGE_FONT=("Verdana", 11)


class Calculators(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container=tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}

        for F in (StartPage, NumberSystems, Binary, Hexadecimal, Pithagorean,
                  TwoSides, SideandHypotenuse, PlanfigCircumf, PlanfigTerr, Polygon, Gauss, NumsysExpl, CircumfTerrExpl,
                  PithagoreanExpl, DiagonalAngleExpl, GaussExpl):
            
            frame=F(container, self)

            self.frames[F]=frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
        
    def show_frame(self, cont, event=None):
        frame=self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Hey there! :)\n"
                                 "I'm very glad, you're here!\n"
                                 "In this program you will find different calculators that help you to practice several calculations that might be useful in school.\n"
                                 "I would like to call your attention to two important things:\n"
                                 "The program indicates exponents as:^^, e.g. 3^^2--> 3 in the 2nd power, and you will see squarecentimetres written as cm2.\n"
                                 "\n"
                                 "Don't forget: knowledge is power and if you have it, you will be able to do amazing things! Have fun! :)", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)
        label2=tk.Label(self, text="Main Menu", font=HIGHLIGHTED_FONT)
        label2.pack(padx=10,pady=10)
        button1=tk.Button(self, text="Number system converter (binary, hexadecimal)",font=AVERAGE_FONT, bg="white",
                          command=lambda: controller.show_frame(NumberSystems))     
        button1.config(height=2,width=40)
        button1.pack(padx=10,pady=10)
        button2=tk.Button(self, text="Pithagorean-triangle calculator",font=AVERAGE_FONT, bg="yellow",
                          command=lambda: controller.show_frame(Pithagorean))
        button2.config(height=2,width=40)
        button2.pack(padx=10,pady=10)
        button3=tk.Button(self, text="Circumference of plane figures",font=AVERAGE_FONT, bg="orange",
                          command=lambda: controller.show_frame(PlanfigCircumf))
        button3.config(height=2,width=40)
        button3.pack(padx=10,pady=10)
        button4=tk.Button(self, text="Territory of plane figures",font=AVERAGE_FONT, bg="red",
                          command=lambda: controller.show_frame(PlanfigTerr))
        button4.config(height=2,width=40)
        button4.pack(padx=10,pady=10)
        button5=tk.Button(self, text="Inner angles and diagonals of convex polygons",font=AVERAGE_FONT, bg='green',
                          command=lambda: controller.show_frame(Polygon))
        button5.config(height=2,width=40)
        button5.pack(padx=10,pady=10)
        
        button6=tk.Button(self, text="Sum and product of consecutive numbers",font=AVERAGE_FONT, bg="violet",
                          command=lambda: controller.show_frame(Gauss))
        button6.config(height=2,width=40)
        button6.pack(padx=10,pady=10)
        
        canvas=tk.Canvas(self,bg="white", height=200,width=1200)
        canvas.pack()
        
        canvas.create_polygon(100,50,200,50,200,150,100,150, fill="red")
        canvas.create_polygon(350,75,450,75,450,125,350,125, fill="blue")
        canvas.create_oval(600,50,700,150, fill="orange")
        canvas.create_polygon(900,50,850,150,950,150, fill="green")
        canvas.create_polygon(1150,50,1050,150,1150,150, fill="grey")
        canvas.create_text(600,20, fill="black", font="Verdana", text="Developed by: Andras Komjathy")

        
        
class NumberSystems(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Number system converter", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)

        

        button1=tk.Button(self, text="Convert to binary",font=AVERAGE_FONT, bg="#6daa2c",
                          command=lambda: controller.show_frame(Binary))
        button1.config(height=2,width=40)
        button1.pack(padx=30,pady=30)

        button2=tk.Button(self, text="Convert to hexadecimal",font=AVERAGE_FONT, bg="#6daa2c",
                          command=lambda: controller.show_frame(Hexadecimal))
        button2.config(height=2,width=40)
        button2.pack(padx=30,pady=30)
        button3=tk.Button(self, text="Number system examples",font=AVERAGE_FONT, bg="orange",
                          command=lambda: controller.show_frame(NumsysExpl))
        button3.config(height=2, width=40)

        button3.pack(padx=30,pady=30)
        button4=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button4.config(height=2,width=40)
        button4.pack(padx=30,pady=30)
class Binary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Convert to binary - Type in the number and click on the convert button!", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)
      
        self.entry = tk.Entry(self, width=40)
        self.entry.bind('<Return>', self.binary)
        self.entry.pack()      

        button1 = tk.Button(self, text="Convert",font=AVERAGE_FONT, bg="#8fd5ef", command=self.binary)
        button1.config(height=2, width=40)
        button1.bind('<Return>', self.binary)
        button1.pack(padx=10,pady=10)

        button2=tk.Button(self, text="Number system examples",font=AVERAGE_FONT, bg="orange",
                          command=lambda: controller.show_frame(NumsysExpl))
        button2.config(height=2, width=40)

        button2.pack(padx=30,pady=30)

        
        button3=tk.Button(self, text="Back to the number system converting menu",font=AVERAGE_FONT, bg="#c0c0c0",
                          command=lambda: controller.show_frame(NumberSystems))
        button3.config(height=2, width=40)
        button3.pack(padx=30,pady=30)

        button4=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button4.config(height=2, width=40)
        button4.pack(padx=30,pady=30)

    def binary(self, event=None):
        messagebox.showinfo("Answer",(bin(int(self.entry.get())).replace('0b','')))
    
class Hexadecimal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Convert to hexadecimal - Type in the number and then click on the convert button!", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)

        
        
        self.entry = tk.Entry(self, width=40)
        self.entry.bind('<Return>', self.hexadem)
        self.entry.pack()
        button1 = tk.Button(self, text="Convert", font=AVERAGE_FONT, bg="#8fd5ef", command=self.hexadem)
        button1.config(height=2, width=40)
        button1.bind('<Return>', self.hexadem)
        button1.pack(padx=30,pady=30)
        
        
        button2=tk.Button(self, text="Number system examples",font=AVERAGE_FONT, bg="orange",
                          command=lambda: controller.show_frame(NumsysExpl))
        button2.config(height=2, width=40)

        button2.pack(padx=30,pady=30)
        button3=tk.Button(self, text="Back to the number system converter menu",font=AVERAGE_FONT, bg="#c0c0c0",
                          command=lambda: controller.show_frame(NumberSystems))
        button3.config(height=2, width=40)
        button3.pack(padx=30,pady=30)
        button4=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button4.config(height=2, width=40)
        button4.pack(padx=30,pady=30)
    def hexadem(self, event=None):
        messagebox.showinfo("Answer",(hex(int(self.entry.get())).replace('0x','')))
        
    
class Pithagorean(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Pithagorean-triangle calculator", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)

        button1=tk.Button(self, text="Two sides are known",font=AVERAGE_FONT, bg="#6daa2c",
                          command=lambda: controller.show_frame(TwoSides))
        button1.config(height=2, width=40)
        button1.pack(padx=30, pady=30)

        button2=tk.Button(self, text="One side and the hypotenuse are known",font=AVERAGE_FONT, bg="#6daa2c",
                          command=lambda: controller.show_frame(SideandHypotenuse))
        button2.config(height=2, width=40)
        button2.pack(padx=30, pady=30)

        button3=tk.Button(self, text="Pithagorean-explanation",font=AVERAGE_FONT, bg="orange",
                          command=lambda: controller.show_frame(PithagoreanExpl))
        button3.config(height=2, width=40)
        button3.pack(padx=30, pady=30)
        
        button4=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button4.config(height=2, width=40)
        button4.pack(padx=30, pady=30)
        
class TwoSides(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Type in the lenght of the two sides and then click on the calculate button!", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)
      
        self.entry = tk.Entry(self, width=40)
        self.entry.bind('<Return>', self.TwoSides)
        self.entry.pack()
        
        self.entry2 = tk.Entry(self, width=40)
        self.entry2.bind('<Return>', self.TwoSides)
        self.entry2.pack()
        
        button1 = tk.Button(self, text="Calculate", font=AVERAGE_FONT, bg="#8fd5ef", command=self.TwoSides)
        button1.config(height=2, width=40)
        button1.bind('<Return>', self.TwoSides)
        button1.pack(padx=30, pady=30)
        

        button2=tk.Button(self, text="Back to the Pithagorean-triangle calculator menu",font=AVERAGE_FONT, bg="#c0c0c0",
                          command=lambda: controller.show_frame(Pithagorean))
        button2.config(height=2, width=40)
        button2.pack(padx=30, pady=30)
        
        button3=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button3.config(height=2, width=40)
        button3.pack(padx=30, pady=30)
        
    def TwoSides(self, event=None):
        convertable=self.entry.get()
        convertable2=self.entry2.get()
        answer_commadot=convertable.replace(",",".")
        answer_commadot2=convertable2.replace(",",".")
        answer=((math.sqrt(((float(answer_commadot))**2)+(float(answer_commadot2)**2))))
        answer_str=str(answer)
        answer_cdback=answer_str.replace(".",",")
        if answer_cdback.endswith(",0"):
            messagebox.showinfo("Hypotenuse",answer_cdback.replace(",0", ""))
        else:
            messagebox.showinfo("Hypotenuse",answer_cdback)

class SideandHypotenuse(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Type in the length of the hypotenuse in the upper, and the length of the other side in the lower entry.\n"
                                 "Note that the hypotenuse cannot be shorter (or equally short) than the other sides. However, if you type a number like this, the program will not calculate."
                       , font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)
             
        
        self.entry = tk.Entry(self, width=40)
        self.entry.bind('<Return>', self.SideandHypotenuse)
        self.entry.pack()
        
        self.entry2 = tk.Entry(self, width=40)
        self.entry2.bind('<Return>', self.SideandHypotenuse)
        self.entry2.pack()
        
        button1 = tk.Button(self, text="Calculate",font=AVERAGE_FONT, bg="#8fd5ef", command=self.SideandHypotenuse)
        button1.config(height=2, width=40)
        button1.bind('<Return>', self.SideandHypotenuse)
        button1.pack(padx=30, pady=30)
        
        button2=tk.Button(self, text="Back to the Pithagorean-triangle calculator menu",font=AVERAGE_FONT, bg="#c0c0c0",
                          command=lambda: controller.show_frame(Pithagorean))
        button2.config(height=2, width=40)
        button2.pack(padx=30, pady=30)
        
        button3=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button3.config(height=2, width=40)
        button3.pack(padx=30, pady=30)
    
    def SideandHypotenuse(self, event=None):
        convertable=self.entry.get()
        convertable2=self.entry2.get()
        answer_commadot=convertable.replace(",",".")
        answer_commadot2=convertable2.replace(",",".")
        answer=((math.sqrt((float(answer_commadot)**2)-(float(answer_commadot2)**2))))
        answer_str=str(answer)
        answer_cdback=answer_str.replace(".",",")
        if answer_cdback.endswith(",0"):
            messagebox.showinfo("Third side",answer_cdback.replace(",0", ""))
        else:
            messagebox.showinfo("Third side",answer_cdback)

class PlanfigCircumf(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1=tk.Label(self,text="Circumference of plane figures", font=HIGHLIGHTED_FONT)
        label1.pack(pady=10,padx=10)
        
        label2=tk.Label(self,text="Circumference of squares (Type in the lenght of the side of the square in cm.)", font=SMALL_FONT, anchor=tk.W, justify=tk.RIGHT)
        label2.pack()
        
        self.entry1 = tk.Entry(self, width=40)
        self.entry1.bind('<Return>', self.squarecircumference)
        self.entry1.pack()
        
        button1=tk.Button(self, text="Calculate",font=AVERAGE_FONT, bg="#8fd5ef", command=self.squarecircumference)
        button1.config(height=2, width=40)
        button1.bind('<Return>', self.squarecircumference)
        button1.pack(padx=30, pady=30)
        
        label3=tk.Label(self, text="Circumference of rectangles (Type in the lenght of the longer and the shorter sides of the rectangle in cm.)", font=SMALL_FONT)
        label3.pack()
        
        self.entry2=tk.Entry(self, width=40)
        self.entry2.bind('<Return>', self.rectanglecircumference)
        self.entry2.pack()
        
        self.entry3=tk.Entry(self, width=40)
        self.entry3.bind('<Return>', self.rectanglecircumference)
        self.entry3.pack()
        
        button2=tk.Button(self, text="Calculate",font=AVERAGE_FONT, bg="#8fd5ef", command=self.rectanglecircumference)
        button2.config(height=2, width=40)
        button2.bind('<Return>', self.rectanglecircumference)
        button2.pack(padx=30, pady=30)
        
        label4=tk.Label(self, text="Circumference of circles (Type in the radius of the circle in cm.)", font=SMALL_FONT)
        label4.pack()
        
        self.entry4=tk.Entry(self, width=40)
        self.entry4.bind('<Return>', self.circlecircumference)
        self.entry4.pack()
        
        button3=tk.Button(self, text="Calculate",font=AVERAGE_FONT, bg="#8fd5ef", command=self.circlecircumference)
        button3.config(height=2, width=40)
        button3.bind('<Return>', self.circlecircumference)
        button3.pack(padx=30, pady=30)

        button4=tk.Button(self, text="Formulas and explanations",font=AVERAGE_FONT, bg="orange", command=lambda: controller.show_frame(CircumfTerrExpl))
        button4.config(height=2, width=40)
        button4.pack(padx=30, pady=30)
        
        button5=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button5.config(height=2, width=40)
        button5.pack(padx=30, pady=30)
        
        
        

        
    def squarecircumference(self, event=None):
        convertable=self.entry1.get()
        answer_commadot=convertable.replace(",",".")
        answer=(((float(answer_commadot)*4)))
        answer_str=str(answer)
        answer_cdback=answer_str.replace(".",",")
        if answer_cdback.endswith(",0"):
            messagebox.showinfo("Answer",answer_cdback.replace(",0", ""))
        else:
            messagebox.showinfo("Answer",answer_cdback)
 
    def rectanglecircumference(self, event=None):
        convertable=self.entry2.get()
        convertable2=self.entry3.get()
        answer_commadot=convertable.replace(",",".")
        answer_commadot2=convertable2.replace(",",".")
        answer=((float(answer_commadot)*2)+(float(answer_commadot2)*2))
        answer_str=str(answer)
        answer_cdback=answer_str.replace(".",",")
        if answer_cdback.endswith(",0"):
            messagebox.showinfo("Answer",answer_cdback.replace(",0", ""))
        else:
            messagebox.showinfo("Answer",answer_cdback)
        
    def circlecircumference(self, event=None):
        convertable=self.entry4.get()
        answer_commadot=convertable.replace(",",".")
        answer=((float(answer_commadot)*2*3.14159265359))
        answer_str=str(answer)
        answer_cdback=answer_str.replace(".",",")
        if answer_cdback.endswith(",0"):
            messagebox.showinfo("Answer",answer_cdback.replace(",0", ""))
        else:
            messagebox.showinfo("Answer",answer_cdback)


class PlanfigTerr(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1=tk.Label(self,text="Territory of plane figures (The answers are in cm2.)", font=HIGHLIGHTED_FONT)
        label1.pack(pady=10,padx=10)
        
        label2=tk.Label(self,text="Territory of a square (Type in the length of the side of the square in cm.)", font=SMALL_FONT, anchor=tk.W, justify=tk.RIGHT)
        label2.pack()
        
        self.entry1 = tk.Entry(self, width=40)
        self.entry1.bind('<Return>', self.squareterritory)
        self.entry1.pack()
        
        button1=tk.Button(self, text="Calculate",font=AVERAGE_FONT, bg="#8fd5ef", command=self.squareterritory)
        button1.config(height=2, width=40)
        button1.bind('<Return>', self.squareterritory)
        button1.pack(padx=30, pady=30)
        
        label3=tk.Label(self, text="Territory of a rectangle (Type in the lenght of the longer and the shorter sides of the rectangle in cm.)", font=SMALL_FONT)
        label3.pack()
        
        self.entry2=tk.Entry(self, width=40)
        self.entry2.bind('<Return>', self.rectangleterritory)
        self.entry2.pack()
        
        self.entry3=tk.Entry(self, width=40)
        self.entry3.bind('<Return>', self.rectangleterritory)
        self.entry3.pack()
        
        button2=tk.Button(self, text="Calculate",font=AVERAGE_FONT, bg="#8fd5ef", command=self.rectangleterritory)
        button2.config(height=2, width=40)
        button2.bind('<Return>', self.rectangleterritory)
        button2.pack(padx=30, pady=30)
        
        label4=tk.Label(self, text="Territory of a circle (Type in the radius of the circle in cm.)", font=SMALL_FONT)
        label4.pack()
        
        self.entry4=tk.Entry(self, width=40)
        self.entry4.bind('<Return>', self.circleterritory)
        self.entry4.pack()
        
        button3=tk.Button(self, text="Calculate",font=AVERAGE_FONT, bg="#8fd5ef", command=self.circleterritory)
        button3.config(height=2, width=40)
        button3.bind('<Return>', self.circleterritory)
        button3.pack(padx=30, pady=30)

        button4=tk.Button(self, text="Formulas and explanations",font=AVERAGE_FONT, bg="orange",
                          command=lambda: controller.show_frame(CircumfTerrExpl))
        button4.config(height=2, width=40)
        button4.pack(padx=30, pady=30)
        
        button5=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button5.config(height=2, width=40)
        button5.pack(padx=30, pady=30)

        

    def squareterritory(self, event=None):
        convertable=self.entry1.get()
        answer_commadot=convertable.replace(",",".")
        answer=((float(answer_commadot)**2))
        answer_str=str(answer)
        answer_cdback=answer_str.replace(".",",")
        if answer_cdback.endswith(",0"):
            messagebox.showinfo("Territory",answer_cdback.replace(",0", ""))
        else:
            messagebox.showinfo("Territory",answer_cdback)

        
    def rectangleterritory(self, event=None):
        convertable=self.entry2.get()
        convertable2=self.entry3.get()
        answer_commadot=convertable.replace(",",".")
        answer_commadot2=convertable2.replace(",",".")
        answer=((float(answer_commadot)*(float(answer_commadot2))))
        answer_str=str(answer)
        answer_cdback=answer_str.replace(".",",")
        if answer_cdback.endswith(",0"):
            messagebox.showinfo("Territory",answer_cdback.replace(",0", ""))
        else:
            messagebox.showinfo("Territory",answer_cdback)

    def circleterritory(self, event=None):
        convertable=self.entry4.get()
        answer_commadot=convertable.replace(",",".")
        answer=((float(answer_commadot)**2*3.14159265359))
        answer_str=str(answer)
        answer_cdback=answer_str.replace(".",",")
        if answer_cdback.endswith(",0"):
            messagebox.showinfo("Territory",answer_cdback.replace(",0", ""))
        else:
            messagebox.showinfo("Territory",answer_cdback)


class Polygon(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Inner angles and diagonals of convex polygons", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)

        
        label=tk.Label(self, text="Type in the number of sides of the polygon, then click on the calculate button!", font=SMALL_FONT)
        label.pack()
        self.entry = tk.Entry(self, width=40)
        self.entry.bind('<Return>', self.polygon_innerangle)
        self.entry.pack()       

        button1 = tk.Button(self, text="The sum of inner angles (degrees)",font=AVERAGE_FONT, bg="#8fd5ef", command=self.polygon_innerangle)
        button1.config(height=2, width=40)
        button1.bind('<Return>', self.polygon_innerangle)
        button1.pack(padx=30, pady=30)
        
        label=tk.Label(self, text="Type in the number of sides of the polygon.", font=SMALL_FONT)
        label.pack()
        self.entry2 = tk.Entry(self, width=40)
        self.entry2.bind('<Return>', self.diagonals)
        self.entry2.pack()
        button2=tk.Button(self, text="Number of diagonals",font=AVERAGE_FONT, bg="#8fd5ef", command=self.diagonals)
        button2.config(height=2, width=40)
        button2.bind('<Return>', self.diagonals)
        button2.pack(padx=30, pady=30)

        button3=tk.Button(self, text="Formulas and explanations",font=AVERAGE_FONT, bg="orange",
                          command=lambda: controller.show_frame(DiagonalAngleExpl))
        button3.config(height=2, width=40)
        button3.pack(padx=30, pady=30)
        
        button4=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button4.config(height=2, width=40)
        button4.pack(padx=30, pady=30)
    
    def polygon_innerangle(self, event=None):
        messagebox.showinfo("Answer",((int(self.entry.get())-2)*180))

    def diagonals(self, event=None):
        answer=(((int(self.entry2.get()))*(int(self.entry2.get())-3)/2))
        answer_str=str(answer)
        answer_cdback=answer_str.replace(".",",")
        if int(self.entry2.get())<4:
            messagebox.showinfo("Diagonals", "No diagonals")
        elif answer_cdback.endswith(",0"):
            messagebox.showinfo("Diagonals",answer_cdback.replace(",0", ""))

        else:
            messagebox.showinfo("Diagonals", answer_cdback)

class Gauss(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Sum and product of consecutive numbers\n"
                                 "Example: From 1 to 5 the sum of numbers is (1+2+3+4+5)=15, and the product is (1*2*3*4*5)=120.", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)

        
        label=tk.Label(self, text="Type in the first number of the sequence in the upper, and the last number in the lower entry field.\n"
                                  "Please, use the product function with numbers below 2001.\n"
                                  "If you don't understand why, run the multiplication with 1 and 2000! :)\n"
                                  "You probably do not need such a big number! :)",font=SMALL_FONT)
        label.pack()
        self.entry = tk.Entry(self, width=40)
        self.entry.bind('<Return>', self.GaussOsszeg)
        self.entry.pack()       
      
        self.entry2 = tk.Entry(self, width=40)
        self.entry2.bind('<Return>', self.GaussOsszeg)
        self.entry2.pack()
        
        button1 = tk.Button(self, text="Sum",font=AVERAGE_FONT, bg="#8fd5ef", command=self.GaussOsszeg)
        button1.config(height=2, width=40)
        button1.bind('<Return>', self.GaussOsszeg)
        button1.pack(padx=30, pady=30)
        
        button2=tk.Button(self, text="Product",font=AVERAGE_FONT, bg="#8fd5ef", command=self.GaussSzorzat)
        button2.config(height=2, width=40)
        button2.bind('<Return>', self.GaussSzorzat)
        button2.pack(padx=30, pady=30)

        button3=tk.Button(self, text="Formulas and explanations",font=AVERAGE_FONT, bg="orange",
                          command=lambda: controller.show_frame(GaussExpl))
        button3.config(height=2, width=40)
        button3.pack(padx=30, pady=30)
        
        button4=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button4.config(height=2, width=40)
        button4.pack(padx=30, pady=30)
    def GaussOsszeg(self, event=None):
        answer=(((((int(self.entry2.get()))-((int(self.entry.get()))))+1))*((((int(self.entry.get()))+(int(self.entry2.get()))))/2))
        answer_str=str(answer)
        answer_cdback=answer_str.replace(".",",")
        if answer_cdback.endswith(",0"):
            messagebox.showinfo("Sum",answer_cdback.replace(",0", ""))
        else:
            messagebox.showinfo("Sum", answer_cdback)

    def GaussSzorzat(self, event=None):
        total=1
        if (int (self.entry2.get()))>2000:
            messagebox.showinfo("Too big number", "Please, type in a number below 2001.")
        else:
            for num in range(int(self.entry.get()),(int(self.entry2.get())+1)):
                total=total*num
            messagebox.showinfo("Product", total)
        
            
class NumsysExpl(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="About number systems", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)

        canvas=tk.Canvas(self, bg="white", height=500, width=1200)
        canvas.pack()
        canvas.create_text(600,250,fill="black", font="Verdana", text=
                           "Decimal number system\n"
                           "\n"
                           "digits: 0,1,2,3,4,5,6,7,8,9\n"
                           "place values (quetions of 10): 1,10,100,1000,10000,100000,1000000,stb.\n"
                           "example: 2018=2*1000+0*100+1*10+8*1, so 2018\n"
                           "\n"
                           "Binary number system\n"
                           "\n"
                           "digits: 0,1\n"
                           "place values (quetions of 2): 1,2,4,8,16,32,64,128,256,512,1024, etc.\n"
                           "example: 100=1*64+1*32+0*16+0*8+1*4+0*2+0*1, so 1100100\n"
                           "\n"
                           "Hexadecimal number system\n"
                           "\n"
                           "digits: 0,1,2,3,4,5,6,7,8,9,a(10),b(11),c(12),d(13),e(14),f(15)\n"
                           "place values (quetions of 16): 1,16,256,4096,65536,1048576,16777216\n"
                           "example: 2000=7*256+13*16+0*1\n"
                           "\n"
                           "\n"
                           "Converting to binary: 200/128=1, 72 remains, 72/64=1, 8 remains, 8/32=0, 8 remains d, 8/16=0, 8 remains, 8/8=1, 0 remains, 0/4=0,\n"
                           "0 remains, 0/2=0,0 remains d, 0/1=0,0 remains, so 200=11001000\n"
                           "\n"
                           "\n"
                           "Converting to hexadecimal: 2000/256=7, 208 remains, 208/16=13(d), 0 remains, 0/1=0, 0 remains, so 2000=7d0")                   
        button1 = tk.Button(self, text="Back to binary converter",font=AVERAGE_FONT, bg="#c0c0c0",
                            command=lambda: controller.show_frame(Binary))
        button1.config(height=2, width=40)
        button1.pack(padx=10,pady=10)

        button2 = tk.Button(self, text="Back to hexadecimal converter",font=AVERAGE_FONT, bg="#c0c0c0",
                            command=lambda: controller.show_frame(Hexadecimal))
        button2.config(height=2, width=40)
        button2.pack(padx=10,pady=10)
        
        button3=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button3.config(height=2, width=40)
        button3.pack(padx=10,pady=10)
        
class PithagoreanExpl(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Pithagorean-explanation", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)

               
        canvas=tk.Canvas(self, bg="white", height=520, width=1200)
        canvas.pack()

        line=canvas.create_line(950,50,1150,50, fill="black")
        line2=canvas.create_line(1150,50,1150,250, fill="black")
        line3=canvas.create_line(950,50,1150,250, fill="black")

        upper_triangle=canvas.create_polygon(950,50,1150,250,950,250,fill="#8fd5ef")
        angle1=canvas.create_oval(940,240,960,260, fill="white")
        angle2=canvas.create_oval(1160,60, 1140,40, fill="white")

        lower_triangle=canvas.create_polygon(1150,400,1150,500,950,500,fill="#6daa2c")
        line4=canvas.create_line(1150,400,950,500, fill="black")
        line5=canvas.create_line(950,500,950,400, fill="black")
        line6=canvas.create_line(950,400,1150,400, fill="black")

        angle3=canvas.create_oval(940,390,960,410, fill="white")
        angle4=canvas.create_oval(1160,510, 1140,490, fill="white")

        canvas.create_text(550,200, fill="black", font="Verdana", text=
                           "The Pithagorean-triangle has two sides that are perpendicular to each other and a hypotenuse.\n"
                           "\n"
                           "\n"
                           "If we devide a square or a rectangle in two pieces along their diagonals, we will get two Pithagorean-triangles.\n"
                           "\n"
                           "In this case, the diagonal coincides with the hypotenuse of the newly created triangles.\n"
                           "\n"
                           "In a Pithagorean triangle the hypotenuse is always the longest. The equation we need is: a^^2+b^^2=c^^2.\n"
                           "\n"
                           "a=The length of the first side, b=The length of the other side, c=The length of the hypotenuse.\n"
                           "\n"
                           "Example: The length of the two sides are 3 and 4 cm, then: 3^^2+4^^2=9+16=25, the hypotenuse is\n"
                           "\n"
                           "5 cm long, because the square root of 25 is 5. If we know the length of the hypotenuse and another side, \n"
                           "\n"
                           "we need to calculate this way: c^^2-a^^2=b^^2, vagy c^^2-b^^2=a^^2. Example: hypotenuse=15 cm, one side=9 cm, so\n"
                           "\n"
                           "15^^2-9^^2=225-81=144. The square root of 144 is 12, so the length of the other side is 12 cm.")
        
        button1=tk.Button(self, text="Back to calculator(two sides)",font=AVERAGE_FONT, bg="#c0c0c0",
                          command=lambda: controller.show_frame(TwoSides))
        button1.config(height=2, width=40)
        button1.pack(padx=10, pady=10)

        button2=tk.Button(self, text="Back to calculator(One side a hypotenuse)",font=AVERAGE_FONT, bg="#c0c0c0",
                          command=lambda: controller.show_frame(SideandHypotenuse))
        button2.config(height=2, width=40)
        button2.pack(padx=10, pady=10)
        
        button3=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button3.config(height=2, width=40)
        button3.pack(padx=10, pady=10)


class CircumfTerrExpl(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Formulas and explanations", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)

        
        canvas=tk.Canvas(self, bg="white", height=500, width=1200)
        canvas.pack()
        negyzet=canvas.create_polygon(1050,50,1150,50,1150,150,1050,150,
                                        fill="green")
        squareline_vertical=canvas.create_line(1100,50, 1100,150, fill="white")
        squareline_horizontal=canvas.create_line(1050,100, 1150,100, fill="white")
        rectangle=canvas.create_polygon(1050,200,1150,200,1150,250,1050,250,fill="blue")
        rectangleline=canvas.create_line(1100,200,1100,250, fill="white")
        circle=canvas.create_oval(1050,300,1150,400,fill="red")
        radius=canvas.create_line(1100,300,1100,350,fill="black")
        canvas.create_text(500,250,fill="black", font="Verdana", text=
                           "Square\n"
                           "\n"
                           "Circumference=4*a\n"
                           "Territory=a^^2\n"
                           "\n"
                           "Example: The circumference of a 2 cm sided square is 8 cm, while its territory is 4 cm2,\n"
                           "because 4*2=8 and 2^^2=4.\n"
                           "A 2 cm sided aquare can be divided in 4 pieces of 1 cm sided squares. (figure)\n"
                           "That's why its territory is 4 times bigger than the smaller ones.\n"
                           "\n"
                           "Rectangle\n"
                           "\n"
                           "Circumference=2*(a+b)\n"
                           "Territory=a*b\n"
                           "\n"
                           "Example: a side=20 cm, b side=40 cm, circumference=120 cm, territory=800 cm2.\n"
                           "A 20x40cm rectangle can be divided in 2 pieces of 20 cm sided squares, that's why its territory\n"
                           "is two times bigger than the smaller ones.\n"
                           "\n"
                           "Circle\n"
                           "\n"
                           "Circumference=2*r*pi\n"
                           "Territory=r^^2*pi\n"
                           "r= The radius of the circle (indicated with line in the figure), pi=3,14(rounded)\n"
                           "Example: A circle with 10 cm radius has a circumference of 2*10*3,14=62,8 cm and territory of 100^^2*3,14=314 cm2.\n")

        button1=tk.Button(self, text="Back to circumference-calculator",font=AVERAGE_FONT, bg="#c0c0c0",
                          command=lambda: controller.show_frame(PlanfigCircumf))
        button1.config(height=2, width=40)
        button1.pack(padx=10, pady=10)

        button2=tk.Button(self, text="Back to territory calculator",font=AVERAGE_FONT, bg="#c0c0c0",
                          command=lambda: controller.show_frame(PlanfigTerr))
        button2.config(height=2, width=40)
        button2.pack(padx=10, pady=10)
        
        button3=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button3.config(height=2, width=40)
        button3.pack(padx=10, pady=10)
        
class DiagonalAngleExpl(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Inner angles and diagonals of polygons", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)

        canvas=tk.Canvas(self, bg="white", height=500, width=1200)
        canvas.pack()
        negyzet=canvas.create_polygon(900,50,1100,50,1100,200,900,200, fill="red")
        line=canvas.create_line(900,50,1100,200, fill="white")
        line2=canvas.create_line(900,200,1100,50, fill="white")

        pentagon=canvas.create_polygon(1000,300,900,400,925,480,1075,480,1100,400, fill="violet")

        line3=canvas.create_line(1000,300,925,480, fill="white")
        line4=canvas.create_line(1000,300,1075,480, fill="white")
        line5=canvas.create_line(900,400,1100,400, fill="white")
        line6=canvas.create_line(900,400,1075,480, fill="white")
        line7=canvas.create_line(925,480,1100,400, fill="white")

        canvas.create_text(400,200, fill="black", font="Verdana", text=
                           "With the help of the following equation you can calculate\n"
                           "the number of diagonals in a convex polygon:\n"
                           "\n"
                           "n*(n-3)/2\n"
                           "\n"
                           "Example: quadrilateral, 4*(4-3)/2=2, so it has 2 diagonals\n"
                           "\n"
                           "Pentagon, 5*(5-3)/2=5, so it has 5 diagonals.\n"
                           "\n"
                           "\n"
                           "The sum of inner angles of convex polygons=(n-2)*180\n"
                           "\n"
                           "Example: Hexagon (6-2)*180=720 degrees the sum of the inner angles of the hexagon.\n")

        button1=tk.Button(self, text="Back to the calculator",font=AVERAGE_FONT, bg="#c0c0c0",
                          command=lambda: controller.show_frame(Polygon))
        button1.config(height=2, width=40)
        button1.pack(padx=30, pady=30)
        
        button2=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button2.config(height=2, width=40)
        button2.pack(padx=30, pady=30)
class GaussExpl(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label=tk.Label(self,text="Sum and product of consecutive numbers", font=HIGHLIGHTED_FONT)
        label.pack(pady=10,padx=10)

        canvas=tk.Canvas(self, bg="white", height=500, width=1200)
        canvas.pack()
        

        canvas.create_text(500,150, fill="black", font="Verdana", text=
                           "1+2+3+4+5+6+7+8+9+10=55. You can calculate this in a much easier way.\n"
                           "\n"
                           "Sn=((a1+an)*n)/2\n"
                           "\n"
                           "a1=The first number of the sequence--> 1\n"
                           "\n"
                           "an=The last number of the sequence --> 10\n"
                           "\n"
                           "n=The quantity of numbers in the sequence--> 10 (a1+an)-1\n"
                           "\n"
                           "So:((1+10)*10)/2=55.\n"
                           "\n"
                           "If you multiply the numbers from 1 (like 1*2*3*4*5, etc.), you will get factorial values.\n"
                           "\n"
                           "e.g. 1*2*3= 3 factorial that equals 6. Factorial is indicated with an exclamation mark, e.g. 5!= 5 factorial.")

        button1=tk.Button(self, text="Back to calculator",font=AVERAGE_FONT, bg="#c0c0c0",
                          command=lambda: controller.show_frame(Gauss))
        button1.config(height=2, width=40)
        button1.pack(padx=30, pady=30)
        
        button2=tk.Button(self, text="Back to main menu",font=AVERAGE_FONT, bg="#808080",
                          command=lambda: controller.show_frame(StartPage))
        button2.config(height=2, width=40)
        button2.pack(padx=30, pady=30)               

                
        
app=Calculators()
app.mainloop()



        
    
