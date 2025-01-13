from PIL import Image

i=Image.open("ImageExemple.bmp")
sortie=Image.new("L",i.size)
valeur = []

for y in range(i.size[1]):
    for x in range(i.size[0]):
        valeur.append((i.getpixel((x, y))[0]+i.getpixel((x, y))[1]+i.getpixel((x, y))[2])//3)
sortie.putdata(valeur)
sortie.save("imageout2.bmp")

