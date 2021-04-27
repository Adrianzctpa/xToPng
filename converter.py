import os
from PIL import Image,ImageFilter

def converter():
    path = input("Insert your file path with the images: ")
    tmpsave = input("Insert here where you want to save your file: ")

    if os.path.isdir(tmpsave) == False:
        os.mkdir(tmpsave)
    pathtosave = tmpsave

    question = input("Do you want to modify your image AND convert it to png? Y/N")
    if question == "Y" or "y" or '':
        for imgs in os.listdir(path):
            img = Image.open(f"{path}/{imgs}")
            modify = input('''What do you want to do, then?
            Blur the image? Smooth it? Sharp it?
            ''')
            if modify == "Blur" or "blur":
                filteredimg = img.filter(ImageFilter.BLUR)
                filteredimg.save(f"{pathtosave}/{imgs}blur.png", "png")
            elif modify == "Smooth" or "smooth":
                filteredimg = img.filter(ImageFilter.SMOOTH)
                filteredimg.save(f"{pathtosave}/{imgs}smooth.png", "png")
            elif modify == "Sharp" or "sharp":
                filteredimg = img.filter(ImageFilter.SHARPEN)
                filteredimg.save(f"{pathtosave}/{imgs}sharp.png", "png")        
    elif question == "N" or "n":
        pass
    else:
        print("Uh, I said 'Y' or 'N'.")

    question2 = input("Do you want to convert every file to png? Y/N")
    if question2 == "Y" or "y" or '':    
        for imgs in os.listdir(path):
            img = Image.open(f"{path}/{imgs}")
            img.save(f"{pathtosave}/{imgs}.png", "png")
            print("Done!")
    elif question2 == "N" or "n":
        print("Bye!")
        exit
    else:
        print("Y or N.")              

converter()