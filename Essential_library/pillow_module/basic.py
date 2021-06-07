from PIL import Image 

ImageFile='ImageArchive/cat.jpeg'
OutFile='ImageOut/cat.png'
image =Image.open(ImageFile)
print(image.filename)
print(image.format)
print(image.width)
print(image.height)
print(image.mode)

#saving image in another format 
image.save(OutFile)
img=Image.open(OutFile)

#show image with the default image viewer
img.show()
