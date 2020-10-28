from PIL import Image, ImageFilter

image =Image.open("milt.jpg")
image.save("milt2.jpg")
image.rotate(180).save("milt3.jpg")
image.rotate(90).save("milt4.jpg")
image.convert(mode = "L").save("milt5.jpg")
degistir =(320,200)
image.thumbnail(degistir)
image.save("milt.6.jpg")
image.filter(ImageFilter.GaussianBlur(5)).save("milt7.jpg")
kırpılacak_alan =(340,0,950,600)
image2 =Image.open("tilt.jpg")
image2.crop(kırpılacak_alan).save("tilt2.jpg")