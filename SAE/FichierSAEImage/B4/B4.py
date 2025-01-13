from PIL import Image

i=Image.open("B4/IUT-Orleans.bmp")
sortie=Image.new("L",i.size)
valeur = []

for y in range(i.size[1]):
    for x in range(i.size[0]):
        r = i.getpixel((x, y))[0]
        v = i.getpixel((x, y))[1]
        b = i.getpixel((x, y))[2]
        if (r*r+v*v+b*b) >= (255*255*3/2):
            valeur.append(255)
        else: 
            valeur.append(0)

sortie.putdata(valeur)
sortie.save("imageout3.bmp")
