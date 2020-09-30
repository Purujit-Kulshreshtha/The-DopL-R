import tkinter
window = tkinter.Tk()
window.title("Velocity")
window.geometry("200x500")

def slide(var):
	level = slider.get()

slider = tkinter.Scale(window, from_=-255, to=255, command=slide, troughcolor = "#f5efef", label = "Velocity")
slider.pack()

window.mainloop()
