from cProfile import label
import wolframalpha
import wikipedia
from tkinter import *

root = Tk()


def user_input():
    search = (input_ent.get())
    
    try:
        # wolframalpha
        api_id = "******-**********" # you will need to enter the API key from wolframalpha
        client = wolframalpha.Client(api_id)
        result = client.query(search)
        answer = next(result.results).text
        print(answer)
        textarea.config(text="" + answer)

    except:
        # wikipedia
        print(wikipedia.summary(search))


def clear_search():
    clear = input_ent.delete(0, "end")


input_ent = Entry(root, 
                  width=57)
input_ent.place(x=26, y=100)

submit_btn = Button(root, 
                    width=22, 
                    height=2, 
                    text="Submit",
                    command=user_input)
submit_btn.place(x=25, y=130)

clear_btn = Button(root, 
                   width=22, 
                   height=2, 
                   text="Clear",
                   command=clear_search)
clear_btn.place(x=208, y=130)

'''

needs fixing

result_lab = Label(root,
                   width=49,
                   height=10,
                   bg="grey")
result_lab.place(x=25, y=190)

v_s = Scrollbar(result_lab)
v_s.pack(side=RIGHT, fill=Y)

textarea = Label(root,
                width=43,
                height=5,
                wrap=NONE,
                yscrollcommand=v_s.set)
textarea.place(x=20, y=270)

root.geometry("400x400")
root.resizable(0, 0)
root.attributes("-topmost", True)
root.mainloop()

https://www.youtube.com/watch?v=BckVJoE94Lk
https://github.com/Azzy001/Vehicle_Management_System_Tk/blob/main/Sales_GUI.py
https://github.com/Azzy001/Contact_Book/blob/main/main_contact.py
https://github.com/Azzy001/Guess_Game_Tk/blob/main/guess_game_Tk.py
'''