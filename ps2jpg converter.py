from PIL import Image
filename = ".ps file location"
img = Image.open(filename)
img.save('output.jpg')
