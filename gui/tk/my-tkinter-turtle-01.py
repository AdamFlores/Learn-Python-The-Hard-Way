import Tkinter as tkinter
import turtle
import sys

def main():

	root = tkinter.Tk()
	
	cv = tkinter.Canvas(root, width=600, height=600)
	
	cv.pack(side=tkinter.LEFT) 
	
	root.title("Draw!")
	
	t=turtle.RawTurtle(cv)
	
	screen = t.getScreen()
	
	screen.setworldcoordinates(0,0,600,600)
	
	frame=tkinter.Frame(root)
	
	frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
	
	def quitHandler():
		sys.exit(0)
	
	quitButton=tkinter.Button(frame,text="Quit",command=quitHandler)
	
	quitButton.pack()

	tkinter.mainloop()


if __name__ == "-__main__":
	main()
	