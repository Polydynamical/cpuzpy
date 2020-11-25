from tkinter import *
import win32api

global w
W, H = 768, 768
x, y = W/2, H/2

root = Tk()
root.title('Tkinter DND')
root.iconbitmap('C:/Users/andre/Downloads/web-programming.ico')
root.geometry("768x768")

canv = Canvas(root, width=768, height=768, bg="white")
canv.pack()


#chessboard = PhotoImage(file="D:/projects/cpuz/images/chessboard.png")
#my_image = canv.create_image(x, y, image=chessboard)
#
#
#global bB
#bB = PhotoImage(file="D:/projects/cpuz/images/pieces/bB.png") # black bishop
#global w
#w = Button(canv, image = bB)
#w.pack() 
#
#def move():
#	def drag(g):
#		def snap(h):
#			w.destroy()
#			w.place(100,100)
#			w.pack()
#		canv.bind("<ButtonRelease-1>", snap)
#		w.destroy()
#		w.place(x=g.x, y=g.y)
#		w.pack()
#	canv.bind("<B1-Motion>", drag)
#
#
#
## download all chess pieces
#w.destroy()
#w = Button(canv, image = bB, command=move)
#w.pack() 



img = PhotoImage(file="C:/Users/andre/Downloads/web-programming.png")
img = img.subsample(20)
my_image = canv.create_image(260, 125, image=img)

def move(e):
	# e.x
	# e.y
        def snap(g):
                canv.delete(my_image)
                my_image2 = canv.create_image(100,100, image=img)
        canv.bind("<ButtonRelease-1>", snap)
        global img
        global my_image
        img = PhotoImage(file="C:/Users/andre/Downloads/web-programming.png")
        img = img.subsample(20)
        my_image = Button(e.x, e.y, image=img)
        my_label.config(text="Coordinates: " + str(e.x) + " y " + str(e.y))
 
 	# if win32api.GetKeyState(0x01) == -127:
 

canv.bind("<B1-Motion>", move)

root.mainloop()
