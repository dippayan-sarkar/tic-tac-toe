from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('380x340')
root.title('Dippayan')
root.iconbitmap(r'1.1.ico')

player1=[]
player2=[]



clicked=True
count=0


def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked=True
    count=0
    l = Label(root, text=' Player1:X', font='lucida 15 bold')
    l.grid(row=0, column=1)

    l1 = Label(root, text=' Player2:O', font='lucida 15 bold')
    l1.grid(row=0, column=2)

    b1 = Button(root, text='', bd=7, relief=RIDGE, width=15, height=5, command=lambda: click(b1))
    b1.grid(row=1, column=1)

    b2 = Button(root, text='', bd=7, relief=RIDGE, width=15, height=5, command=lambda: click(b2))
    b2.grid(row=1, column=2)

    b3 = Button(root, text='', bd=7, relief=RIDGE, width=15, height=5, command=lambda: click(b3))
    b3.grid(row=1, column=3)

    b4 = Button(root, text='', bd=7, relief=RIDGE, width=15, height=5, command=lambda: click(b4))
    b4.grid(row=2, column=1)

    b5 = Button(root, text='', bd=7, relief=RIDGE, width=15, height=5, command=lambda: click(b5))
    b5.grid(row=2, column=2)

    b6 = Button(root, text='', bd=7, relief=RIDGE, width=15, height=5, command=lambda: click(b6))
    b6.grid(row=2, column=3)

    b7 = Button(root, text='', bd=7, relief=RIDGE, width=15, height=5, command=lambda: click(b7))
    b7.grid(row=3, column=1)

    b8 = Button(root, text='', bd=7, relief=RIDGE, width=15, height=5, command=lambda: click(b8))
    b8.grid(row=3, column=2)

    b9 = Button(root, text='', bd=7, relief=RIDGE, width=15, height=5, command=lambda: click(b9))
    b9.grid(row=3, column=3)


def click(b):
    global clicked,count
    if b['text']==''and clicked== True:
        b['text']='X'
        clicked= False
        count= count+1
        checked_if_won()
    elif b['text']==''and clicked== False:
        b['text']='O'
        clicked= True
        count= count+1
        checked_if_won()
    else:
        messagebox.showerror('Dippayan','Box is already been filled \n Choose another box....  ')

def checked_if_won():
    global winner
    winner=False
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg='blue')
        b2.config(bg='blue')
        b3.config(bg='blue')
        winner = True
        messagebox.showinfo('Dippayan', 'Congratulations!!! X wins ')
        disable_all_buttons()


    elif b1['text']=='X' and b4['text']=='X' and b7['text']=='X':
        b1.config(bg='blue')
        b4.config(bg='blue')
        b7.config(bg='blue')
        winner= True
        messagebox.showinfo('Dippayan','Congratulations!!! X wins ')
        disable_all_buttons()
    elif b4['text']=='X' and b5['text']=='X' and b6['text']=='X':
        b4.config(bg='blue')
        b5.config(bg='blue')
        b6.config(bg='blue')
        winner= True
        messagebox.showinfo('Dippayan','Congratulations!!! X wins ')
        disable_all_buttons()
    elif b7['text']=='X' and b8['text']=='X' and b9['text']=='X':
        b7.config(bg='blue')
        b8.config(bg='blue')
        b9.config(bg='blue')
        winner= True
        messagebox.showinfo('Dippayan','Congratulations!!! X wins ')
        disable_all_buttons()
    elif b2['text']=='X' and b5['text']=='X' and b8['text']=='X':
        b2.config(bg='blue')
        b5.config(bg='blue')
        b8.config(bg='blue')
        winner= True
        messagebox.showinfo('Dippayan','Congratulations!!! X wins ')
        disable_all_buttons()
    elif b3['text']=='X' and b6['text']=='X' and b9['text']=='X':
        b3.config(bg='blue')
        b6.config(bg='blue')
        b9.config(bg='blue')
        winner= True
        messagebox.showinfo('Dippayan','Congratulations!!! X wins ')
        disable_all_buttons()
    elif b1['text']=='X' and b5['text']=='X' and b9['text']=='X':
        b1.config(bg='blue')
        b5.config(bg='blue')
        b9.config(bg='blue')
        winner= True
        messagebox.showinfo('Dippayan','Congratulations!!! X wins ')
        disable_all_buttons()
    elif b3['text']=='X' and b5['text']=='X' and b7['text']=='X':
        b3.config(bg='blue')
        b5.config(bg='blue')
        b7.config(bg='blue')
        winner= True
        messagebox.showinfo('Dippayan','Congratulations!!! X wins ')
        disable_all_buttons()

#for O

    if b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(bg='blue')
        b2.config(bg='blue')
        b3.config(bg='blue')
        winner = True
        messagebox.showinfo('Dippayan', 'Congratulations!!! O wins ')
        disable_all_buttons()

    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(bg='blue')
        b4.config(bg='blue')
        b7.config(bg='blue')
        winner = True
        messagebox.showinfo('Dippayan', 'Congratulations!!! O wins ')
        disable_all_buttons()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(bg='blue')
        b5.config(bg='blue')
        b6.config(bg='blue')
        winner = True
        messagebox.showinfo('Dippayan', 'Congratulations!!! O wins ')
        disable_all_buttons()
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        b7.config(bg='blue')
        b8.config(bg='blue')
        b9.config(bg='blue')
        winner = True
        messagebox.showinfo('Dippayan', 'Congratulations!!! O wins ')
        disable_all_buttons()
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(bg='blue')
        b5.config(bg='blue')
        b8.config(bg='blue')
        winner = True
        messagebox.showinfo('Dippayan', 'Congratulations!!! O wins ')
        disable_all_buttons()

    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg='blue')
        b6.config(bg='blue')
        b9.config(bg='blue')
        winner = True
        messagebox.showinfo('Dippayan', 'Congratulations!!! O wins ')
        disable_all_buttons()

    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg='blue')
        b5.config(bg='blue')
        b9.config(bg='blue')
        winner = True
        messagebox.showinfo('Dippayan', 'Congratulations!!! O wins ')
        disable_all_buttons()

    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        b3.config(bg='blue')
        b5.config(bg='blue')
        b7.config(bg='blue')
        winner = True
        messagebox.showinfo('Dippayan', 'Congratulations!!! O wins ')
        disable_all_buttons()


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)




#for menu bar
menu1= Menu(root)
root.config(menu=menu1)
option_menu= Menu(menu1,tearoff=False)
menu1.add_cascade(label='Option',menu=option_menu)
option_menu.add_command(label='reset game',command=reset)
option_menu.add_command(label='game on')













reset()
root.mainloop()