import tkinter
from tkinter import ttk
import random
import sqlite3


def generator(length):
	
	if length.isdigit():
	
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
	
	else:
		out.delete(0, tkinter.END)
		userInput.delete(0, tkinter.END)
		userInput.insert(0, 'Enter digit only!')
		out.insert(0, 'Enter digit only!')


class Database:
  
	def __init__(self):
		self.conn = sqlite3.connect('data.sqlite')
		self.cur = self.conn.cursor()
		self.cur.execute('CREATE TABLE IF NOT EXISTS Passwords (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, password TEXT)')
		self.conn.commit()

	def view(self):
		self.cur.execute('SELECT * FROM Passwords')
		rows = self.cur.fetchall()
		return rows
	
	def save(self, name, psw):
		self.cur.execute('INSERT INTO Passwords(name, password) VALUES (?,?)', (str(name), str(psw)))
		self.conn.commit()		

	def delete(self, index):
		self.cur.execute('DELETE FROM Passwords WHERE id=?', (str(index),))
		self.conn.commit()		

	def __del__(self):
		self.conn.close()

data = Database()

def view_in_tree(tree):
	tree.delete(*tree.get_children())
	rows = data.view()
	for row in rows:
		#print(row)
		tree.insert('', tkinter.END, values = row)

def not_common():
	mark = []
	rows = data.view()
	for row in rows:
		if str(out.get()) in row[2]:
			out.delete(0, tkinter.END)
			out.insert(0, '!!!Password exists!!!')
			mark.append(False)
		elif str(inputPassName.get()) in row[1]:
			inputPassName.delete(0, tkinter.END)
			inputPassName.insert(0, '!!!Name exists!!!')
			mark.append(False)
		else:
			mark.append(True)
	if False in mark:
		return False
	else:
		return True

def save_password():
	def saveit():
		data.save(inputPassName.get(), out.get())
		inputPassName.delete(0, tkinter.END)
		inputPassName.insert(0, 'Password saved!')

	if len(out.get()) == 0:
		userInput.delete(0, tkinter.END)
		userInput.insert(0, 'Generate password!')
	elif len(inputPassName.get()) == 0:
		inputPassName.delete(0, tkinter.END)
		inputPassName.insert(0, 'Enter name!')
	else:
		if not_common():
			saveit()
			view_in_tree(tree)
		else:
			pass

def delete_row(tree):
	try:
		selected = tree.selection()[0]
		index = tree.item(selected)['values']
		index = index[0]	
		tree.delete(selected)
		data.delete(index)
	except IndexError:
		pass


window = tkinter.Tk()

window['bg'] = '#000000'
window.title('BruqwaPassMan')

window.geometry('770x400')
window.resizable(width=True, height = True)

canvas = tkinter.Canvas(window, height = 300, width = 300)
canvas.pack()

frame = tkinter.Frame(window, bg = 'black')
frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

tree = ttk.Treeview(frame, columns = ('id', 'Name', 'Password'), height = 15, show = 'headings')
tree.column('id', width = 30)
tree.column('Name', width = 250)
tree.column('Password', width = 250)
tree.heading('id', text = 'ID')
tree.heading('Name', text = 'Name')
tree.heading('Password', text = 'Password')
tree.grid(column = 1, row = 1, rowspan = 7)

title1 = tkinter.Label(frame, text = 'Enter password length\n(should be more then 4): ', bg = 'black', fg = 'orange', font =70)
title1.grid(column = 0, row = 0, stick = 'we', padx = 10, pady = 10)

userInput = tkinter.Entry(frame, bg = 'black', fg = 'orange', justify='center', insertbackground = 'orange')
userInput.grid(column = 0, row = 1, stick = 'we', padx = 10, pady = 10)

btnGen = tkinter.Button(frame, text = 'Generate', bg = 'orange', command = lambda: generator(userInput.get()))
btnGen.grid(column = 0, row = 2, stick = 'we', padx = 10, pady = 10)

title2 = tkinter.Label(frame, text = 'Your password is: ', bg = 'black', fg = 'orange', font =70)
title2.grid(column = 0, row = 3, stick = 'we', padx = 10, pady = 10)

out = tkinter.Entry(frame, bg = 'black', fg = 'lime', justify='center', insertbackground = 'lime')
out.grid(column = 0, row = 4, stick = 'we', padx = 10, pady = 10)

title3 = tkinter.Label(frame, text = 'Enter name to save\ngenerated password: ', bg = 'black', fg = 'orange', font =70)
title3.grid(column = 0, row = 5, stick = 'we', padx = 10, pady = 10)

inputPassName = tkinter.Entry(frame, bg = 'black', fg = 'orange', justify='center', insertbackground = 'orange')
inputPassName.grid(column = 0, row = 6, stick = 'we', padx = 10, pady = 10)

btnSave = tkinter.Button(frame, text = 'Save password', bg = 'orange', command = lambda: save_password())
btnSave.grid(column = 0, row = 7, stick = 'we', padx = 10, pady = 10)

title4 = tkinter.Label(frame, text = 'Saved Passwords: ', bg = 'black', fg = 'orange', font =70)
title4.grid(column = 1, row = 0, stick = 'ws', padx = 10, pady = 10)

btnDelete = tkinter.Button(frame, text = 'Delete', bg = 'orange', command = lambda: delete_row(tree))
btnDelete.grid(column = 1, stick = 'es', row = 0, padx = 0, pady = 10)

s = ttk.Style()
s.configure('Treeview', background = '#000', foreground = 'lime')

view_in_tree(tree)

window.mainloop()