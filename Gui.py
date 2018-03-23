import tkinter as tk
import pickle

window = tk.Tk()
window.title('zhihuishu_login')
window.geometry('200x130')

l1 = tk.Label(window,text='Your phone number:')
l1.pack()

e1 = tk.Entry(window,show=None)
e1.pack()

l2 = tk.Label(window,text = 'password:')
l2.pack()
e2 = tk.Entry(window,show="*")
e2.pack()


def save():
	dataDic = {'account':'0','key':'0'}
	dataDic['account'] = e1.get()
	dataDic['key'] = e2.get()
	with open('data.txt','wb') as file:
		pickle.dump(dataDic,file)

b = tk.Button(window,text='confirm',command=save)
b.pack()

window.mainloop()
