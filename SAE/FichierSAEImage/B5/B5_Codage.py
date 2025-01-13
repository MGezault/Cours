from PIL import Image

def cacher(i,b):
    return i-(i%2)+b

i=Image.open("B2/hall-mod_0.bmp")
logo =Image.open ("imageout3.bmp")
sortie=i.copy()

for y in range(logo.size[1]):
    for x in range(logo.size[0]): 
        r, g, b = i.getpixel((x,y))
        if logo.getpixel((x, y)) == 255:
            sortie.putpixel((x,y),((cacher(r,1)),g,b))
        else:
            sortie.putpixel((x,y),(cacher(r,0),g,b))

sortie.save("imageout4.bmp")