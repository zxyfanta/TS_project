# -*- coding:utf-8 -*-

import PySimpleGUI as SG


def main_view():
    SG.theme("Topanga")
    layout_struct = [
        [SG.Text("任职"), SG.Text("R级", size=(15, 1)), SG.Text("平均工资（S)", size=(15, 1)),
         SG.Text("现状人数(N)", size=(15, 1)), SG.Text("调薪人数", size=(15, 1))],
        [SG.Text("八级"), SG.InputText(size=(15, 1), default_text=""), SG.InputText(size=(15, 1), default_text=""),
         SG.InputText(size=(15, 1), default_text=""), SG.InputText(size=(15, 1), default_text="")],
        [SG.Text("七级"), SG.InputText(size=(15, 1), default_text=""), SG.InputText(size=(15, 1),
                                                                                  default_text=""), SG.InputText(
            size=(15, 1), default_text=""), SG.InputText(size=(15, 1), default_text="")],
        [SG.Text("六级"), SG.InputText(size=(15, 1), default_text=""), SG.InputText(size=(15, 1),
                                                                                  default_text=""), SG.InputText(
            size=(15, 1), default_text=""), SG.InputText(size=(15, 1), default_text="")],
        [SG.Text("五级"), SG.InputText(size=(15, 1), default_text=""), SG.InputText(size=(15, 1),
                                                                                  default_text=""), SG.InputText(
            size=(15, 1), default_text=""), SG.InputText(size=(15, 1), default_text="")],
        [SG.Text("四级"), SG.InputText(size=(15, 1), default_text=""), SG.InputText(size=(15, 1),
                                                                                  default_text=""), SG.InputText(
            size=(15, 1), default_text=""), SG.InputText(size=(15, 1), default_text="")],
        [SG.Text("三级"), SG.InputText(size=(15, 1), default_text=""), SG.InputText(size=(15, 1),
                                                                                  default_text=""), SG.InputText(
            size=(15, 1), default_text=""), SG.InputText(size=(15, 1), default_text="")],
        [SG.Text("二级"), SG.InputText(size=(15, 1), default_text=""), SG.InputText(size=(15, 1),
                                                                                  default_text=""), SG.InputText(
            size=(15, 1), default_text=""), SG.InputText(size=(15, 1), default_text="")],
        [SG.Text("一级"), SG.InputText(size=(15, 1), default_text=""), SG.InputText(size=(15, 1),
                                                                                  default_text=""), SG.InputText(
            size=(15, 1), default_text=""), SG.InputText(size=(15, 1), default_text="")]
    ]
    layout_main = [
        [SG.Text("调薪包"), SG.InputText(key="_st_", size=(15, 1))],
        [SG.TabGroup([[SG.Tab(title="人员结构", layout=layout_struct)]])],
        [SG.Button("OK"), SG.Button("Exit")]
    ]

    window = SG.Window("调薪计算程序", layout=layout_main)
    while True:
        event, values = window.read()
        if event in [None, 'cancel']:
            break
    window.close()

    print(event, values[0], values[1], values[2])


class PromoteModel:
    # 初始化变量
    R_key = ["R" + str(i) for i in range(3, 11)]
    S_key = ["S" + str(i) for i in range(3, 11)]
    N_key = ["N" + str(i) for i in range(3, 10)]
    R_list = dict.fromkeys(["R" + str(i) for i in range(3, 11)])
    S_list = dict.fromkeys(["S" + str(i) for i in range(3, 11)])
    N_list = dict.fromkeys(["N" + str(i) for i in range(3, 10)])

    def Conculated(self):
        pass

    # 初始化函数
    def __init__(self, St):
        # 载入录入参数

        # 调薪包
        _st = St
        print(self.R_list)
        # 人员等级
        main_view()


if __name__ == '__main__':
    mode = PromoteModel(10)
