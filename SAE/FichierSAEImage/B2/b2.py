from PIL import Image

i=Image.open("B2/hall-mod_0.bmp")
sortie=i.copy()
sortieinversee= sortie.transpose(Image.FLIP_LEFT_RIGHT)
sortieinversee.save("Imageout1.bmp")