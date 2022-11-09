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
    except:
        # wikipedia
        print(wikipedia.summary(search))


input_ent = Entry(root, width=57)
input_ent.place(x=26, y=200)

submit_btn = Button(root, width=15, height=2, text="Submit", command=user_input)
submit_btn.place(x=50, y=230)

clear_btn = Button(root, width=15, height=2, text="Clear")
clear_btn.place(x=230, y=230)

result_bar = Scrollbar(root, width=360, orient=VERTICAL)
result_bar.place(x=20, y=270)


root.geometry("400x550")
root.resizable(0, 0)
root.attributes("-topmost", True)
root.mainloop()