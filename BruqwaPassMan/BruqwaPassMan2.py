from tkinter import *
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
	out.delete(0, END)
	out.insert(0, password)

def press_key(event):
	if event.char == '\r':
		generator(userInput.get())	
	else:
		pass

window = Tk()

window.bind('<Key>', press_key)

window['bg'] = '#000000'
window.title('BruqwaPassMan')
#window.wm_attributes('-alpha', 0,7)
window.geometry('230x270')
window.resizable(width=True, height = True)

canvas = Canvas(window, height = 300, width = 300)
canvas.pack()

frame = Frame(window, bg = 'black')
frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

title1 = Label(frame, text = 'Enter password length\n(should be more then 4): ', bg = 'black', fg = 'orange', font = 40)
title1.grid(row = 0, stick = 'we', padx = 10, pady = 10)

userInput = Entry(frame, bg = 'black', fg = 'orange', justify='center', insertbackground = 'orange')
userInput.grid(row = 1, stick = 'we', padx = 10, pady = 10)

btn = Button(frame, text = 'Generate', bg = 'orange', command = lambda: generator(userInput.get()))
btn.grid(row = 2, stick = 'we', padx = 10, pady = 10)

title2 = Label(frame, text = 'Your password is: ', bg = 'black', fg = 'orange', font = 40)
title2.grid(row = 3, stick = 'we', padx = 10, pady = 10)

out = Entry(frame, bg = 'black', fg = 'lime', justify='center', insertbackground = 'lime')
out.grid(row = 4, stick = 'we', padx = 10, pady = 10)



window.mainloop()
