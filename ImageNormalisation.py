from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
from PIL import ImageFont
from PIL import ImageFont,ImageDraw
file=askopenfilename()
image=Image.open(file)
image=image.convert("RGB")
images=[]
lables=[]
n=file.split("/")[-1][:-3]
for i in range(3):
	for j in (0.1,0.5,0.9):
		source=image.split()
		mid=source[i].point(lambda x:int(x*j))
		source[i].paste(mid)
		im=Image.merge(image.mode,source)
		lables.append('channel {} intensity {}'.format(i,j))
		images.append(im)
font=ImageFont.truetype("C:/Windows/Fonts/Arial.ttf",size=30)
first_image=images[0]
contact_sheet=Image.new(first_image.mode,(first_image.width*3,first_image.height*3+3*85))
(x,y)=(0,0)
for j,i in enumerate(images):
	i.show()
	r=n+str(j)
	i.save(r+".png")
draw=ImageDraw.Draw(contact_sheet)
for i,img in enumerate(images):
	contact_sheet.paste(img,(x,y))
	draw.text((x,y+first_image.height+5),lables[i],font=font)
	if x+first_image.width==contact_sheet.width:
		x=0
		y=y+first_image.height+85
	else:
		x=x+first_image.width
contact_sheet=contact_sheet.resize((int(contact_sheet.width),int(contact_sheet.height)))
contact_sheet.show()
contact_sheet.save(n+".png")


