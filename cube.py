from vertex import*
from Tkinter import*
from time import*

class cube:
    def __init__(self,bg="black",col="white",width=1,rotX=0,rotY=0):
        self.ff,self.df,self.kX,self.kY,self.iX,self.iY=1,1,rotX,rotY,0,0
        self.a,self.b,self.t1,self.t2=0,0,0,0
        self.jX,self.jY=0,0
        self.bg,self.color,self.width=bg,col,width
        self.root=Tk()
        self.c=Canvas(self.root,bg=self.bg,width=600,height=600)
        self.c.configure(scrollregion=(-300,-300,300,300))
        self.c.pack(side="top",expand=True)
        self.c.bind("<Button-1>",self.click)
        self.c.bind("<ButtonRelease-1>",self.release)
        self.vertices=[[-1,1,-1],[1,1,-1],[1,-1,-1],[-1,-1,-1],[-1,1,1],[1,1,1],[1,-1,1],[-1,-1,1]]
        self.face=[[0,1,2,3],[1,5,6,2],[5,4,7,6],[4,0,3,7],[0,4,5,1],[3,2,6,7]] 

    def click(self,event):
        self.a,self.b,self.t1=event.x,event.y,time()

    def release(self,event):
        self.a,self.b,self.t2=(-1*(self.a-event.x)),(-1*(self.b-event.y)),time()
        if self.a==0 and self.b==0:
            self.ff-=0.05
            if self.ff<0:
                self.ff=0
        else:
            self.jX=(self.a//(self.t2-self.t1))//140
            try:
                self.iX=(self.kX//self.jX)
            except ZeroDivisionError:
                pass
            self.jY=(self.b//(self.t2-self.t1))//140
            try:
                self.iY=(self.kY//self.jY)
            except ZeroDivisionError:
                pass
            self.df=1
        
    def rotate(self):
        while True:
            if self.jX==0:
                self.kX=self.kX
            else:
                self.kX=((self.iX*self.jX)*self.ff)*self.df
            if self.jY==0:
                self.kY=self.kY
            else:
                self.kY=((self.iY*self.jY)*self.ff)*self.df
                
            v=[]
            self.c.delete("all")
            for i in range(8):
                v.append(vertex(self.vertices[i][0],self.vertices[i][1],self.vertices[i][2]))
                r=v[i].rotateX(self.kX).rotateY(self.kY).rotateZ(0)
                v[i]=r._3Dto2D(200,3.5)
            for j in range(6):
                self.c.create_polygon(v[self.face[j][0]].x,v[self.face[j][0]].y,v[self.face[j][1]].x,v[self.face[j][1]].y,v[self.face[j][2]].x,v[self.face[j][2]].y,v[self.face[j][3]].x,v[self.face[j][3]].y,outline=self.color,fill='',width=self.width)
            self.c.update()
            sleep(0.03)
            self.iX,self.iY,self.df=(self.iX+1),(self.iY+1),(self.df-0.01)
            if self.df<0.5:
               self.jX,self.jY,self.df=0,0,1
            if self.iX>360:
                self.iX=1
            if self.iY>360:
                self.iY=1
            
if __name__== "__main__":
    cube()
