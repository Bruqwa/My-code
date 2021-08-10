import tkinter
from tkinter import ttk
import random

def generator(length):
	length = int(length)
	upperLetters = 'ABCDEFGHIJKLOPQRSTUVWXYZ'
	lowerLetters = 'abcdefghijklopqrstuvwxyz'
	numbers = '0123456789'
	symbols = '!@#$%^&*()[]:;"?><,.-_+='

	chars = upperLetters + lowerLetters + numbers + symbols
	allchars = []
	for i in chars:
		allchars.append(i)
	random.shuffle(allchars)

	password = []
	password.append(random.choice(upperLetters))
	password.append(random.choice(lowerLetters))
	password.append(random.choice(numbers))
	password.append(random.choice(symbols))

	if len(password) <= length:
		saltlen = length - len(password)
	else:
		saltlen = 0
	password.extend(random.choices(allchars, weights=None, cum_weights=None, k=saltlen))
	random.shuffle(password)
	password = ''.join(password)
	out.delete(0, tkinter.END)
	out.insert(0, password)

def press_key(event):
	if event.char == '\r':
		generator(userInput.get())	
	else:
		pass

window = tkinter.Tk()

window.bind('<Key>', press_key)

window['bg'] = '#000000'
window.title('BruqwaPassMan')

window.geometry('770x400')
window.resizable(width=True, height = True)

canvas = tkinter.Canvas(window, height = 300, width = 300)
canvas.pack()

frame = tkinter.Frame(window, bg = 'black')
frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

title1 = tkinter.Label(frame, text = 'Enter password length\n(should be more then 4): ', bg = 'black', fg = 'orange', font =70)
title1.grid(row = 0, stick = 'we', padx = 10, pady = 10)

userInput = tkinter.Entry(frame, bg = 'black', fg = 'orange', justify='center', insertbackground = 'orange')
userInput.grid(row = 1, stick = 'we', padx = 10, pady = 10)

btnGen = tkinter.Button(frame, text = 'Generate', bg = 'orange', command = lambda: generator(userInput.get()))
btnGen.grid(row = 2, stick = 'we', padx = 10, pady = 10)

title2 = tkinter.Label(frame, text = 'Your password is: ', bg = 'black', fg = 'orange', font =70)
title2.grid(row = 3, stick = 'we', padx = 10, pady = 10)

out = tkinter.Entry(frame, bg = 'black', fg = 'lime', justify='center', insertbackground = 'lime')
out.grid(row = 4, stick = 'we', padx = 10, pady = 10)

title3 = tkinter.Label(frame, text = 'Enter name to save\ngenerated password: ', bg = 'black', fg = 'orange', font =70)
title3.grid(column = 0, row = 5, stick = 'we', padx = 10, pady = 10)

inputPassName = tkinter.Entry(frame, bg = 'black', fg = 'orange', justify='center', insertbackground = 'orange')
inputPassName.grid(column = 0, row = 6, stick = 'we', padx = 10, pady = 10)

btnSave = tkinter.Button(frame, text = 'Save password', bg = 'orange')
btnSave.grid(column = 0, row = 7, stick = 'we', padx = 10, pady = 10)

btnDelete = tkinter.Button(frame, text = 'Delete password', bg = 'orange')
btnDelete.grid(column = 1, stick = 'w', row = 7, padx = 0, pady = 10)

s = ttk.Style()
s.configure('Treeview', background = '#000')

tree = ttk.Treeview(frame, columns = ('ID', 'Name', 'Password'), height = 15, show = 'headings')
tree.column('ID', width = 30)
tree.column('Name', width = 250)
tree.column('Password', width = 250)
tree.heading('ID', text = 'ID')
tree.heading('Name', text = 'Name')
tree.heading('Password', text = 'Password')
tree.grid(column = 1, row = 0, rowspan = 7)



window.mainloop()
