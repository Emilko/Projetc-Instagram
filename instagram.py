import ImageFilter
import Image
from bottle import route, run
@route('/workspace/Instagram')
def hello():
        return 'Hello World'
run(host='localhost', port= 8080, debug= True )

class CInstagramImage:
        def __init__(self, name = None, description = None):
                self.name = name
                self.im = Image.open(self.name)
                self.description = description
                self.filt = None
                
        def setDescription(self, description = None):
                self.description = description
               
        def printDesc(self):
                print self.description
       
        def applyFilter(self, aCFilter):
                self.imCopy = aCFilter.applyFilter(self.im)
       
        def showImage(self):
                self.imCopy.save("test.jpg", "JPEG")
class CFilter: 
        def applyFilter(self, anImage):
                pass
                       
class CFilterBlur(CFilter):
        def applyFilter(self, anImage):
                anImage = anImage.filter(ImageFilter.BLUR)
                return anImage 
 
class CFilterSharpen(CFilter):
        def applyFilter(self, anImage):
                anImage = anImage.filter(ImageFilter.SHARPEN)
                return anImage
                           
class CFilterGrayscale(CFilter):
        def applyFilter(self, anImage):
                new_image = Image.new('RGB', anImage.size)
                new_image_list = []
               
                pixels = anImage.getdata()
               
                for pixel in pixels:
                        r,g,b = pixel
                        v = int(0.2126*int(r) + 0.7152*int(g) + 0.0722*int(b))
                        new_pixel = (v,v,v)
                        new_image_list.append(new_pixel)
                new_image.putdata(new_image_list)
                return new_image
 
class CFilterInvert(CFilter):
        def applyFilter(self, anImage):
                new_image = Image.new('RGB', anImage.size)
                new_image_list = []
               
                pixels = anImage.getdata()
               
                for pixel in pixels:
                        r,g,b = pixel
                        r = 255-int(r)
                        g = 255-int(g)
                        b = 255-int(b)
                        new_pixel = (r,g,b)
                        new_image_list.append(new_pixel)
                new_image.putdata(new_image_list)
                return new_image
 
class CFilterThreshold(CFilter):
        def __init__(self, threshold):
                self.threshold = threshold
               
        def applyFilter(self, anImage):
                new_image = Image.new('RGB', anImage.size)
                new_image_list = []
               
                pixels = anImage.getdata()
               
                for pixel in pixels:
                        r,g,b = pixel
                       
                        v = int(0.2126*int(r) + 0.7152*int(g) + 0.0722*int(b))
                        if v > self.threshold:
                                        v = 255
                        elif v <= self.threshold:
                                        v = 0
                        new_pixel = (v,v,v)
                        new_image_list.append(new_pixel)
                new_image.putdata(new_image_list)
                return new_image
            
            
class CFilterRedAndBlue(CFilter):
        def __init__(self, redandblue):
                self.redandblue = redandblue
        def applyFilter(self, anImage):
                new_image = Image.new('RGB', anImage.size)
                new_image_list = []
               
                pixels = anImage.getdata()
               
                for pixel in pixels:
                        r,g,b = pixel
                       
                        v = int(0.7126*int(r) + 0.122*int(g) + 0.0722*int(b))
                        if v > self.redandblue:
                                        v = 255
                        elif v <= self.redandblue:
                                        v = 0
                        new_pixel = (v,0,v)
                        new_image_list.append(new_pixel)
                new_image.putdata(new_image_list)
                return new_image
            
class CFilterGreenLantern(CFilter):
        def __init__(self, greenlantern):
                self.greenlantern = greenlantern
        def applyFilter(self, anImage):
                new_image = Image.new('RGB', anImage.size)
                new_image_list = []
               
                
                pixels = anImage.getdata()
                for pixel in pixels:
                        r,g,b = pixel
                        v = int(0.7126*int(r) + 0.122*int(g) + 0.0722*int(b))
                        if v > self.greenlantern:
                                        v = 255
                        elif v <= self.greenlantern:
                                        v = 0
                        new_pixel = (0,v,0)
                        new_image_list.append(new_pixel)
                new_image.putdata(new_image_list)
                return new_image
            
class CFilterTwoFace(CFilter):
        
        def __init__(self, twoface):
                self.redandblue = twoface
        def applyFilter(self, anImage):
                new_image = Image.new('RGB', anImage.size)
                new_image_list = []
               
                
                pixels = anImage.getdata()
                for pixel in pixels:
                        r,g,b = pixel
                        v = int(0.7126*int(r) + 0.122*int(g) + 0.0722*int(b))
                        if v > self.twoface:
                                        v = 255
                        elif v <= self.twoface:
                                        v = 0
                        new_pixel = (v,v,v)
                        new_image_list.append(new_pixel)
                new_image.putdata(new_image_list)
                return new_image



 
def main():
        asd = CInstagramImage("insta01.jpg")
        f = CFilterGreenLantern(150)
        asd.applyFilter(f)
        asd.showImage()
        
        
 
main()