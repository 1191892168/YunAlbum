from PIL import Image
def cut (filename,a,b,c,d):


    img = Image.open("a.jpg")

    cropped = img.crop((a, b, c, d))  # (left, upper, right, lower)
    cropped.save("cut.jpg")
if __name__=="__main__":
    a = input('输入左坐标')
    a=int(a)
    b = input('输入上坐标')
    b=int(b)
    c = input('输入右坐标')
    c=int(c)
    d = input('输入下坐标')
    d=int(d)
    cut('a.jpg',a,b,c,d)