import tkinter as tk

root = tk.Tk()
root.geometry("1000x1000")
img = tk.PhotoImage(file="D:/projects/cpuz/images/pieces/bK.png")

def drag():
	
	global b
	b.pack_forget()
	b = tk.Button(root,text="Click to destroy", bd=0)
	b.pack()

	def snap(g):
		b.pack_forget()
	b.config(command=b.pack_forget) 
	
		
b = tk.Button(root,image=img,command=drag, bd=0)
b.pack()
root.mainloop()
