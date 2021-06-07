from PIL import Image,ImageFilter,ImageFont,ImageOps,ImageTransform
infile='imageA'
outfile='ImageOut'
#Cropping Image file 
with Image.open(infile+'/marvaltony.jpeg') as img:
    midx=img.width/2
    midy=img.height/2
    CropArea=(midx-200,midy-250,midy+500,midx+250)
    cropped=img.crop(CruopArea)
    # cropped.show()
    cropped.save(outfile+'/marvaltony.png')
    print(img.width) #previous width
    print(cropped.width) #after width

#Resizing Image File 
with Image.open(infile +'/marval.jpg') as img:
    resized = img.resize((400,400)) 
    # resized.show()
    resized.save(outfile+'/marval.png')

#filtering image
with Image.open(infile+'/cartoon.jpg') as img:
    filtered=img.filter(ImageFilter.GaussianBlur(5))
    # filtered.show()
    filtered.save(outfile+'/cartoon.png')

#rotating image 
with Image.open('imageA/citin.jpg') as img:
    rotated=img.transpose(Image.ROTATE_90)
    # rotated.show()
    rotated.save(outfile+'/citin.png')
    
#filtering grayscale
with Image.open(infile+'/tony.jpg') as img:
    grayed= ImageOps.grayscale(img)
    grayed.save(outfile+'/tony.jpg')
    # grayed.show()
with Image.open(infile+'/citizen.jpg') as img:
    # rotated=img.transpose(Image.FLIP_LEFT_RIGHT)
    # rotated.show()
    rotated =img.transpose(Image.ROTATE_90)
    rotated.save(outfile+'/citizen.jpg')
    
    

    
    