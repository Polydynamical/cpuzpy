from tkinter import *

def drag_start(event):
	widget = event.widget
	widget.startX = event.x
	widget.startY = event.y

def drag_motion(event):
	widget = event.widget
	x = widget.winfo_x() - widget.startX + event.x
	y = widget.winfo_y() - widget.startY + event.y
	widget.place(x=x, y=y)

window = Tk()
window.geometry("800x800")
# a1 = Button(canv, bg="red").grid(row=7, column=7)
# window.attributes ("-transparentcolor", "red")
#
# bgimg = PhotoImage(file="images/chessboard.png")
# bgimg.subsample(1.04166666666666, 1.04166666666666666)

# background = Label(window, image=bgimg)
# background.pack()










































# White Rook starting on h1

#####################################################
img1 = PhotoImage(file="images/pieces/wR.png")
wR1 = Button(window, image=img1, height=100, width=100)
wR1.place(x=700, y=700)

wR1.bind("<Button-1>", drag_start)
wR1.bind("<B1-Motion>", drag_motion)
#####################################################




# White rook starting on a1

#####################################################
img2 = PhotoImage(file="images/pieces/wR.png")
wR2 = Button(window, image=img2, height=100, width=100)
wR2.place(x=0, y=700)

wR2.bind("<Button-1>", drag_start)
wR2.bind("<B1-Motion>", drag_motion)
#####################################################




# White knight starting on g1

#####################################################
img3 = PhotoImage(file="images/pieces/wN.png")
wN1 = Button(window, image=img3, height=100, width=100)
wN1.place(x=600, y=700)

wN1.bind("<Button-1>", drag_start)
wN1.bind("<B1-Motion>", drag_motion)
#####################################################




# White knight starting on b1

#####################################################
img4 = PhotoImage(file="images/pieces/wN.png")
wN2 = Button(window, image=img4, height=100, width=100)
wN2.place(x=100, y=700)

wN2.bind("<Button-1>", drag_start)
wN2.bind("<B1-Motion>", drag_motion)
#####################################################




# White bishop starting on f1

#####################################################
img5 = PhotoImage(file="images/pieces/wB.png")
wB1 = Button(window, image=img5, height=100, width=100)
wB1.place(x=500, y=700)

wB1.bind("<Button-1>", drag_start)
wB1.bind("<B1-Motion>", drag_motion)
#####################################################




# White bishop starting on c1

#####################################################
img6 = PhotoImage(file="images/pieces/wB.png")
wB2 = Button(window, image=img6, height=100, width=100)
wB2.place(x=200, y=700)

wB2.bind("<Button-1>", drag_start)
wB2.bind("<B1-Motion>", drag_motion)
#####################################################




# White King starting on e1

#####################################################
img7 = PhotoImage(file="images/pieces/wK.png")
wK = Button(window, image=img7, height=100, width=100)
wK.place(x=400, y=700)

wK.bind("<Button-1>", drag_start)
wK.bind("<B1-Motion>", drag_motion)
#####################################################





# White Queen starting on d1

#####################################################
img8Q = PhotoImage(file="images/pieces/wQ.png")
wQ = Button(window, image=img8Q, height=100, width=100)
wQ.place(x=300, y=700)

wQ.bind("<Button-1>", drag_start)
wQ.bind("<B1-Motion>", drag_motion)
#####################################################





# White Pawn starting on a2

#####################################################
img8 = PhotoImage(file="images/pieces/wP.png")
wP0 = Button(window, image=img8, height=100, width=100)
wP0.place(x=0, y=600)

wP0.bind("<Button-1>", drag_start)
wP0.bind("<B1-Motion>", drag_motion)
#####################################################




# White Pawn starting on b2

#####################################################
img9 = PhotoImage(file="images/pieces/wP.png")
wP1 = Button(window, image=img9, height=100, width=100)
wP1.place(x=100, y=600)

wP1.bind("<Button-1>", drag_start)
wP1.bind("<B1-Motion>", drag_motion)
#####################################################





# White Pawn starting on c2

#####################################################
img10 = PhotoImage(file="images/pieces/wP.png")
wP2 = Button(window, image=img10, height=100, width=100)
wP2.place(x=200, y=600)

wP2.bind("<Button-1>", drag_start)
wP2.bind("<B1-Motion>", drag_motion)
#####################################################





# White Pawn starting on d2

#####################################################
img11 = PhotoImage(file="images/pieces/wP.png")
wP3 = Button(window, image=img11, height=100, width=100)
wP3.place(x=300, y=600)

wP3.bind("<Button-1>", drag_start)
wP3.bind("<B1-Motion>", drag_motion)
#####################################################





# White Pawn starting on e2

#####################################################
img12 = PhotoImage(file="images/pieces/wP.png")
wP4 = Button(window, image=img12, height=100, width=100)
wP4.place(x=400, y=600)

wP4.bind("<Button-1>", drag_start)
wP4.bind("<B1-Motion>", drag_motion)
#####################################################





# White Pawn starting on f2

#####################################################
img13 = PhotoImage(file="images/pieces/wP.png")
wP5 = Button(window, image=img13, height=100, width=100)
wP5.place(x=500, y=600)

wP5.bind("<Button-1>", drag_start)
wP5.bind("<B1-Motion>", drag_motion)
#####################################################





# White Pawn starting on g2

#####################################################
img14 = PhotoImage(file="images/pieces/wP.png")
wP6 = Button(window, image=img14, height=100, width=100)
wP6.place(x=600, y=600)

wP6.bind("<Button-1>", drag_start)
wP6.bind("<B1-Motion>", drag_motion)
#####################################################





# White Pawn starting on h2

#####################################################
img15 = PhotoImage(file="images/pieces/wP.png")
wP7 = Button(window, image=img15, height=100, width=100)
wP7.place(x=700, y=600)

wP7.bind("<Button-1>", drag_start)
wP7.bind("<B1-Motion>", drag_motion)
#####################################################


















# Black Rook starting on h8

#####################################################
img16 = PhotoImage(file="images/pieces/bR.png")
bR1 = Button(window, image=img16, height=100, width=100)
bR1.place(x=700, y=0)

bR1.bind("<Button-1>", drag_start)
bR1.bind("<B1-Motion>", drag_motion)
#####################################################




# Black rook starting on a8

#####################################################
img17 = PhotoImage(file="images/pieces/bR.png")
bR2 = Button(window, image=img17, height=100, width=100)
bR2.place(x=0, y=0)

bR2.bind("<Button-1>", drag_start)
bR2.bind("<B1-Motion>", drag_motion)
#####################################################




# Black knight starting on g8

#####################################################
img18 = PhotoImage(file="images/pieces/bN.png")
bN1 = Button(window, image=img18, height=100, width=100)
bN1.place(x=600, y=0)

bN1.bind("<Button-1>", drag_start)
bN1.bind("<B1-Motion>", drag_motion)
#####################################################




# Black knight starting on b8

#####################################################
img19 = PhotoImage(file="images/pieces/bN.png")
bN2 = Button(window, image=img19, height=100, width=100)
bN2.place(x=100, y=0)

bN2.bind("<Button-1>", drag_start)
bN2.bind("<B1-Motion>", drag_motion)
#####################################################




# Black bishop starting on f8

#####################################################
img20 = PhotoImage(file="images/pieces/bB.png")
bB1 = Button(window, image=img20, height=100, width=100)
bB1.place(x=500, y=0)

bB1.bind("<Button-1>", drag_start)
bB1.bind("<B1-Motion>", drag_motion)
#####################################################




# Black bishop starting on c8

#####################################################
img21 = PhotoImage(file="images/pieces/bB.png")
bB2 = Button(window, image=img21, height=100, width=100)
bB2.place(x=200, y=0)

bB2.bind("<Button-1>", drag_start)
bB2.bind("<B1-Motion>", drag_motion)
#####################################################




# Black King starting on e8

#####################################################
img22 = PhotoImage(file="images/pieces/bK.png")
bK = Button(window, image=img22, height=100, width=100)
bK.place(x=400, y=0)

bK.bind("<Button-1>", drag_start)
bK.bind("<B1-Motion>", drag_motion)
#####################################################




# Black Queen starting on d8

#####################################################
img23 = PhotoImage(file="images/pieces/bQ.png")
bQ = Button(window, image=img23, height=100, width=100)
bQ.place(x=300, y=0)

bQ.bind("<Button-1>", drag_start)
bQ.bind("<B1-Motion>", drag_motion)
#####################################################







# Black Pawn starting on a7

#####################################################
img24 = PhotoImage(file="images/pieces/bP.png")
bP0 = Button(window, image=img24, height=100, width=100)
bP0.place(x=0, y=100)

bP0.bind("<Button-1>", drag_start)
bP0.bind("<B1-Motion>", drag_motion)
#####################################################




# Black Pawn starting on b7

#####################################################
img25 = PhotoImage(file="images/pieces/bP.png")
bP1 = Button(window, image=img25, height=100, width=100)
bP1.place(x=100, y=100)

bP1.bind("<Button-1>", drag_start)
bP1.bind("<B1-Motion>", drag_motion)
#####################################################





# Black Pawn starting on c7

#####################################################
img26 = PhotoImage(file="images/pieces/bP.png")
bP2 = Button(window, image=img26, height=100, width=100)
bP2.place(x=200, y=100)

bP2.bind("<Button-1>", drag_start)
bP2.bind("<B1-Motion>", drag_motion)
#####################################################





# Black Pawn starting on d7

#####################################################
img27 = PhotoImage(file="images/pieces/bP.png")
bP3 = Button(window, image=img27, height=100, width=100)
bP3.place(x=300, y=100)

bP3.bind("<Button-1>", drag_start)
bP3.bind("<B1-Motion>", drag_motion)
#####################################################





# Black Pawn starting on e7

#####################################################
img28 = PhotoImage(file="images/pieces/bP.png")
bP4 = Button(window, image=img28, height=100, width=100)
bP4.place(x=400, y=100)

bP4.bind("<Button-1>", drag_start)
bP4.bind("<B1-Motion>", drag_motion)
#####################################################





# Black Pawn starting on f7

#####################################################
img29 = PhotoImage(file="images/pieces/bP.png")
bP5 = Button(window, image=img29, height=100, width=100)
bP5.place(x=500, y=100)

bP5.bind("<Button-1>", drag_start)
bP5.bind("<B1-Motion>", drag_motion)
#####################################################





# Black Pawn starting on g7

#####################################################
img30 = PhotoImage(file="images/pieces/bP.png")
bP6 = Button(window, image=img30, height=100, width=100)
bP6.place(x=600, y=100)

bP6.bind("<Button-1>", drag_start)
bP6.bind("<B1-Motion>", drag_motion)
#####################################################





# Black Pawn starting on h7

#####################################################
img31 = PhotoImage(file="images/pieces/bP.png")
bP7 = Button(window, image=img31, height=100, width=100)
bP7.place(x=700, y=100)

bP7.bind("<Button-1>", drag_start)
bP7.bind("<B1-Motion>", drag_motion)
#####################################################











window.mainloop()
