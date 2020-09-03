# -*- coding:utf-8 -*-
import PySimpleGUI as sg

sg.theme("DackAmber")

layout=[
    [sg.Text("Some text on Row 1")]
    ,[sg.Text("Enter something on Row 2"),sg.InputText()]
    ,[sg.Button("OK"),sg.Button("Cancel")]
]

window=sg.Window("window Title",layout)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED or event=='cancel':
        break
    print("you entered",values[0])
window.close()