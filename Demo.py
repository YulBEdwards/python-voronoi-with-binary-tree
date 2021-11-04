# original Python version by
# Janson Hendryli 
# Tarumanagara University
# Jakarta, Indonesia
# jansonhendryli@gmail.com
# https://github.com/jansonh/Voronoi

import tkinter as tk

from Voronoi import Voronoi

class MainWindow:
    # radius of drawn points on canvas
    RADIUS = 1.5
    label = True
    
    # flag to lock the canvas when drawn
    LOCK_FLAG = False
    
    def __init__(self, master):
        self.master = master
        self.master.title("Voronoi")

        self.frmMain = tk.Frame(self.master, relief=tk.RAISED, borderwidth=1)
        self.frmMain.pack(fill=tk.BOTH, expand=1)

        self.w = tk.Canvas(self.frmMain, width=700, height=600)
        self.w.config(background='white')
        self.w.bind('<Double-1>', self.onDoubleClick)
        self.w.pack()       

        self.frmButton = tk.Frame(self.master)
        self.frmButton.pack()
        
        self.btnCalculate = tk.Button(self.frmButton, text='Calculate', width=25, command=self.onClickCalculate)
        self.btnCalculate.pack(side=tk.LEFT)
        
        self.btnClear = tk.Button(self.frmButton, text='Clear', width=25, command=self.onClickClear)
        self.btnClear.pack(side=tk.LEFT)
        
    def onClickCalculate(self):
        if not self.LOCK_FLAG:
            self.LOCK_FLAG = True

            pObj = self.w.find_all()
            points = []
            print("start")
            flag = 0            
            for p in pObj:
                if flag == 0:
                    coord = self.w.coords(p)                 
                    points.append((coord[0]+self.RADIUS, coord[1]+self.RADIUS))
                flag = flag+1
                if flag == 2: flag = 0

            vp = Voronoi(points)
            vp.process()
            lines = vp.get_output()
            self.drawLinesOnCanvas(lines)
            
            #for L in lines:
            #   print(L)

    def onClickClear(self):
        self.LOCK_FLAG = False
        self.w.delete(tk.ALL)

    def onDoubleClick(self, event):
        if not self.LOCK_FLAG:
            self.w.create_oval(event.x-self.RADIUS, event.y-self.RADIUS, event.x+self.RADIUS, event.y+self.RADIUS, fill="black")
            t =   "   "+str(event.x)+" "+str(event.y)
            if self.label: self.w.create_text(event.x,event.y,anchor="s",font=("Ariel", 7),text=t)

    def drawLinesOnCanvas(self, lines):
        for l in lines:
            self.w.create_line(l[0], l[1], l[2], l[3], fill='blue')

def main(): 
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
