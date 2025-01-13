from PIL import Image

i=Image.open("Imagetest.bmp")
sortie=i.copy()

modification = [((0,3),(255,0,0)),((1,3),(255,0,0)),((2,3),(0,0,255)),((3,2),(15, 157, 232)),((1,0),(255, 0, 0)),
                ((0,1),(0, 255, 0)),((3,1),(0, 255, 255)),((3,0),(255, 0, 255))]
for (position,couleur) in modification:
        sortie.putpixel(position,couleur)

sortie.save("Imageout0.bmp")


