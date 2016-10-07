from math import cos,sin,radians

class vertex:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def rotateY(self,angle):
        y = self.y * cos(radians(angle)) - self.z * sin(radians(angle))
        z = self.y * sin(radians(angle)) + self.z * cos(radians(angle))
        return vertex(self.x,y,z)
        
    def rotateX(self,angle):
        x = self.x * cos(radians(angle)) - self.z * sin(radians(angle))
        z = self.x * sin(radians(angle)) + self.z * cos(radians(angle))
        return vertex(x,self.y,z)
   
    def rotateZ(self,angle):
        x = self.x * cos(radians(angle)) - self.y * sin(radians(angle))
        y = self.x * sin(radians(angle)) + self.y * cos(radians(angle))
        return vertex(x,y,self.z)
    
    def _3Dto2D(self,fov,dist):
        f=fov/(self.z+dist)
        x = (self.x * f)
        y = (self.y * f)
        return vertex(x,y,self.z)

        
        
if __name__=='__main__':
    vertex()
