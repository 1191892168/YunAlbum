
from PIL import Image

def big(filename):
    image = Image.open(filename)
    w,h = image.size
    out=image.resize((w*2,h*2))
    out.save('big.png')

def small(filename):
    image = Image.open(filename)
    w,h = image.size
    image.thumbnail((w/2, h/2))
    image.save('small.png')


if __name__ == "__main__":

     big('aa.png')
     small('a.jpg')