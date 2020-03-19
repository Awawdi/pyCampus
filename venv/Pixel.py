class Pixel:

    def __init__(self,x=0,y=0,red=0,green=0,blue=0):
        self._x=x # - x coordinate
        self._y=y # - y coordinate
        self._red=red # - a value between 0 and 255
        self._green=green # - a value between 0 and 255
        self._blue=blue # - a value between 0 and 255

    def set_coords(self, x, y):
      self._x=x
      self._y=y

    def set_grayscale(self):
        average = (self._red + self._green + self._blue ) / 3
        self._red = self._green = self._blue = int(average)

    def checkColors(self):
        extra=""
        if self._red ==0 and self._green ==0 and self._blue > 50: extra = "Blue"
        if self._red == 0 and self._green > 50 and self._blue == 0: extra = "Green"
        if self._red > 50 and self._green == 0 and self._blue == 0: extra = "Red"
        return extra

    def print_pixel_info(self):
        str= self.checkColors()
        print('X: %s, Y: %s, Color: (%s,%s,%s) %s' %(self._x,self._y, self._red, self._green, self._blue, str))

def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()

main()
