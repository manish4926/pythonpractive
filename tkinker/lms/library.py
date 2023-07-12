from tkinter import *

class LibraryManagementSystem:
    BGCOLOR1 = "powder blue"
    BGCOLOR2 = "powder blue"

    FGCOLOR1 = "green"
    FGCOLOR2 = "black"

    DEFAULT_FONT = "times new roman"

    TITLE_FONT_SIZE = 40

    FONT_WEIGHT_BOLD = "bold"
    FONT_WEIGHT_NORMAL = "bold"

    def __init__(self):
        self.root = Tk()
        self.root.title("Library Management System")
        self.setWindowSize()

        self.getLabel("Welcome to Library Management System", self.BGCOLOR1,self.FGCOLOR1, 20, self.DEFAULT_FONT, self.TITLE_FONT_SIZE, self.FONT_WEIGHT_BOLD,2,6)

        frame = self.getFrame(12, 20,0, self.BGCOLOR1)
        dataframe1 = self.setDataFrameToFrame(frame, "LMS", self.BGCOLOR1, self.FGCOLOR1, 20, self.DEFAULT_FONT, self.TITLE_FONT_SIZE, self.FONT_WEIGHT_BOLD, 0,5, 900, 350)

        self.root.mainloop()



    def setWindowSize(self, width = 1500, height = 800):
        self.root.geometry(str(width)+"x"+str(height)+"+0+0")

    def getLabel(self, title, bgColor:str = "", fgColor:str = "", border:int = 20, font:str = "times new roman", fontSize:int = 20, fontWeight = "normal", paddingX:int = 0, paddingY: int = 0):
        self.lblTitle = Label(self.root, text =title,bg=bgColor,fg= fgColor, bd=border, relief= RIDGE, font=(font, fontSize, fontWeight), padx=paddingX, pady=paddingY)
        self.lblTitle.pack(side=TOP, fill=X)

    def getFrame(self, border:int = 12, paddingX:int = 0, paddingY:int = 0, bgColor:str = ""):
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, pady=0, bg=self.BGCOLOR1)
        frame.place(x=0,y=130, width=1530, height=400)
        return frame

    def setDataFrameToFrame(self, frameName, title, bgColor:str = "", fgColor:str = "", border:int = 20, font:str = "times new roman", fontSize:int = 20, fontWeight = "normal", paddingX:int = 0, paddingY: int = 0, width:int=0, height:int=0):
        DataFrameLeft = LabelFrame(frameName, text=title, bg=bgColor, fg=fgColor, bd=border, relief=RIDGE, font=(font, fontSize, fontWeight))
        DataFrameLeft.place(x=paddingX, y=paddingY, width=width, height=height)






if(__name__ == "__main__"):

    lms = LibraryManagementSystem()

