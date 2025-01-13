from PIL import Image

def trouver(i):
    return i%2

i=Image.open("imageout4.bmp")
sortie=i.copy()

for y in range(i.size[1]):
    for x in range(i.size[0]): 
        if trouver(i.getpixel((x, y))[0])==0:
            sortie.putpixel((x,y),((0,0,0)))
        else:
            sortie.putpixel((x,y),(255,255,255))

sortie.save("imageout5.bmp")