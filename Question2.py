class Point:  

    def _init_(self, x, y):
        self.x = x
        self.y = y


class rectangle: 
    def _init_(self, bottomLeftCorner = Point(0,0), topRightcorner=Point(12,12)):
        self.bottomLeftCorner = bottomLeftCorner
        self.topRightcorner = topRightcorner

        self.height = topRightcorner.y - bottomLeftCorner.y  
        self.width = topRightcorner.x - bottomLeftCorner.x  
        self.area = self.height * self.width  
        self.perimeter = 2 * (self.height + self.width)  

    def intersect(Rec1, Rect1, Rec2, Rect2):  
        if (Rect2.x < Rec2.x or Rec1.x > Rect2.x or Rect1.y < Rec2.y or Rec1.y > Rect2.y):
            return True
        
Shape = rectangle(Point(0, 0), Point(12, 12))  
print(shape.area)  
print(shape.perimeter)  


rectA = rectangle(Point(0, 6), Point(10, 10))
rectB = rectangle(Point(2, 4), Point(12, 12))


Rectangle.intersect(rectA.bottomLeftCorner, rectA.topRightcorner, rectB.bottomLeftCorner, rectB.topRightcorner)