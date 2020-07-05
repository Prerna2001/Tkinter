from tkinter import *
import requests
from bs4 import BeautifulSoup



root = Tk()
root.geometry("400x180")
root.title("Corona Tracker App")

url = "http://worldometers.info/coronavirus"
r=requests.get(url)
data = r.content
soup = BeautifulSoup(data, 'html.parser')
cases = soup.find_all('div',class_ = "maincounter-number")
def get_data():
    case_lb1['text'] = f"Total cases: {cases[0].get_text().strip()}"
    death_lb1['text'] = f"Total Death: {cases[1].get_text().strip()}"
    recoverd_lb1['text'] = f"Total Recovered: {cases[2].get_text().strip()}"
    lb1['text'] = ":Stay Home:"

frame = Frame(root, borderwidth = 5, bg="orange")
frame.pack(fill=X)

btn = Button(frame, text ="Get Data", font ="lucida 15 bold", command =get_data)
btn.pack()

case_lb1 = Label(frame, text = "Total Cases: ", bg="orange", fg = "green", font ="arial 15 bold")
case_lb1.pack()

death_lb1 = Label(frame, text ="Total deaths: ", bg="orange", fg = "red", font="arial 15 bold")
death_lb1.pack()

recoverd_lb1 = Label(frame, text = "Total Recovered: ", bg="orange", fg = "blue", font ="arial 15 bold")
recoverd_lb1.pack()

lb1 = Label(root, text ="", bg="steelblue", fg="white", font="arial 15 bold")
lb1.pack(fill=X)





root.mainloop()