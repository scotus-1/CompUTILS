from PIL import Image
import os
import glob


#  img = Image.open("mai-san.png").convert("RGB")
# img.save("mai-san.jpg", "jpeg")


for filename in os.listdir(os.getcwd()):
    if os.path.isdir(filename):
        print(filename)


print("Found: " + str(len(glob.glob('*.jpg'))) + " out of " + str(len(os.listdir(os.getcwd()))) + " jpeg's")


