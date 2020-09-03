# -*- coding:utf-8 -*-

import PySimpleGUI as sg


class Promote_Model:
    # 初始化函数
    def __init__(self, ST):
        # 载入录入参数

        # 调薪包
        _st = ST

        # 人员等级


sg.theme("Topanga")
layout_struct = [
    [sg.Text("任职"), sg.Text("R级", size=(15, 1)), sg.Text("平均工资（S)", size=(15, 1)),
     sg.Text("现状人数(N)", size=(15, 1)), sg.Text("调薪人数", size=(15, 1))],
    [sg.Text("八级"), sg.InputText(size=(15, 1), default_text=""), sg.InputText(size=(15, 1), default_text=""),
     sg.InputText(size=(15, 1), default_text=""), sg.InputText(size=(15, 1), default_text="")],
    [sg.Text("七级"), sg.InputText(size=(15, 1), default_text=""), sg.InputText(size=(15, 1),
                                                                              default_text=""), sg.InputText(
        size=(15, 1), default_text=""), sg.InputText(size=(15, 1), default_text="")],
    [sg.Text("六级"), sg.InputText(size=(15, 1), default_text=""), sg.InputText(size=(15, 1),
                                                                              default_text=""), sg.InputText(
        size=(15, 1), default_text=""), sg.InputText(size=(15, 1), default_text="")],
    [sg.Text("五级"), sg.InputText(size=(15, 1), default_text=""), sg.InputText(size=(15, 1),
                                                                              default_text=""), sg.InputText(
        size=(15, 1), default_text=""), sg.InputText(size=(15, 1), default_text="")],
    [sg.Text("四级"), sg.InputText(size=(15, 1), default_text=""), sg.InputText(size=(15, 1),
                                                                              default_text=""), sg.InputText(
        size=(15, 1), default_text=""), sg.InputText(size=(15, 1), default_text="")],
    [sg.Text("三级"), sg.InputText(size=(15, 1), default_text=""), sg.InputText(size=(15, 1),
                                                                              default_text=""), sg.InputText(
        size=(15, 1), default_text=""), sg.InputText(size=(15, 1), default_text="")],
    [sg.Text("二级"), sg.InputText(size=(15, 1), default_text=""), sg.InputText(size=(15, 1),
                                                                              default_text=""), sg.InputText(
        size=(15, 1), default_text=""), sg.InputText(size=(15, 1), default_text="")],
    [sg.Text("一级"), sg.InputText(size=(15, 1), default_text=""), sg.InputText(size=(15, 1),
                                                                              default_text=""), sg.InputText(
        size=(15, 1), default_text=""), sg.InputText(size=(15, 1), default_text="")]
]
layout_main = [
    [sg.Text("调薪包"), sg.InputText(key="_st_", size=(15, 1))],
    [sg.TabGroup([[sg.Tab(title="人员结构", layout=layout_struct)]])],
    [sg.Button("OK"), sg.Button("Exit")]
]

window = sg.Window("调薪计算程序", layout=layout_main)

event, values = window.read()

window.close()

# print(event, values[0], values[1], values[2])
