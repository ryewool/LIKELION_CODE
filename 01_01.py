from tkinter import *
import pandas as pd
import os

print(os.getcwd())
# dat = pd.read_excel("./dic_excel.xlsx")
dat2 = pd.read_csv("공공데이터.csv", encoding="utf-8")
# print(dat)
print(dat2)
print()

def click():
    word = entry.get()
    output.delete(0.0, END)
    try:
        def_word = dat2.loc[dat2['용어'] == word, '용어설명'].values[0]  # pandas
    except:
        def_word = "단어 뜻을 찾을 수 없음 "

    output.insert(END, def_word)


window = Tk()
window.title("My Dictionary")

label = Label(window, text="원하는 단어를 입력 후, 엔터 키 누르기")
label.grid(row=0, column=0, sticky=W)

button = Button(window, text="제출", width=5, command=click)
button.grid(row=2, column=0, sticky=W)

label2 = Label(window, text="\n의미:")
label2.grid(row=3, column=0, sticky=W)

output = Text(window, width=50, height=6, wrap=WORD, background="Light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

entry = Entry(window, width=15, bg="light green")
entry.grid(row=1, column=0, sticky=W)
window.mainloop()
