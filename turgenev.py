from tkinter import *
import requests
import webbrowser
import json

url = ''

def send_text(event):

	global url

	button_1.config(state="disabled")

	lable_3['text'] = 'sending...'

	root.update()
	
	key = key_entry.get()
	content = text.get(1.0, END)
	answer = requests.post('https://turgenev.ashmanov.com/', data={'api': 'risk', 'key': key, 'text': content,'more': 1})
	answer = json.loads(answer.text)

	lable_3['text'] = 'Done'
	url = 'http://turgenev.ashmanov.com/?t='+answer['link']

	button_1.config(state="normal")
	button_2.config(state="normal")

	

def open_link(event):
	webbrowser.open_new(url)

# рисую интерфейс
root = Tk()

root.title("Программа для проверки текстов на сервисе turgenev.ashmanov.com")
root.geometry('600x450')
root.resizable(width=False, height=False)

frame_1 = Frame()
frame_2 = Frame()
frame_3 = Frame()
frame_4 = Frame()

frame_1.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()


lable_1 = Label(frame_1, text="KEY сюда =>")
key_entry = Entry(frame_1, width=45)

button_1 = Button(frame_1, text="Проверить текст")
button_1.pack(side=RIGHT, pady=5, padx=10)
button_1.bind("<Button-1>", send_text)

lable_1.pack(side=LEFT)
key_entry.pack(side=RIGHT)

lable_2 = Label(frame_2, text="Текст для проверки:")
lable_2.pack()

text = Text(frame_2, width=70, height=20, bg="lightblue", fg='black', wrap=WORD)
text.pack()

lable_3 = Label(frame_3, text="")
lable_3.pack()

button_2 = Button(frame_4, text="Ссылка на результаты проверки")
button_2.pack(side=RIGHT, pady=5, padx=10)
button_2.bind("<Button-1>", open_link)
button_2.config(state="disabled")

root.event_add('<<Paste>>', '<Control-igrave>')
root.event_add("<<Copy>>", "<Control-ntilde>")


root.mainloop()