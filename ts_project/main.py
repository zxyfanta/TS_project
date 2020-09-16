# -*- coding:utf-8 -*-
import PySimpleGUI as SG
from itertools import chain

# 等级分布
leave = 10
# range范围
leaveRange = leave + 1

SG.theme("Topanga")
# 列的名称
read_com_name = ["S", "N"]
# 拼凑各个列的key
read_str_name = [[str(i) + str(j) for i in read_com_name] for j in range(3, 11)]
var_list = {}
dict_n = {"N" + str(i): 2 for i in range(3, 11)}
dict_s = {"S" + str(i): i for i in range(3, 11)}
result_g = 0


# 获取界面上的值
def get_values(window, values):
    # 判断界面中的值是否为空
    dict_nv = {"N" + str(i): int(values["N" + str(i)]) for i in range(3, 11)}
    dict_sv = {"S" + str(i): int(values["S" + str(i)]) for i in range(3, 11)}
    for i in dict_nv.keys():
        print(i, ":", dict_nv[i])
    for i in dict_n.values():
        if i in [None, ""]:
            SG.popup("N列值输入有误")
    for i in dict_s.values():
        if i in [None, ""]:
            SG.popup("S列值输入有误")
    TSv = int(values["TS"])
    calculate_1(TSv, dict_sv, dict_nv)
    show_data(window, values)


def calculate_1(TSv, dict_sv, dict_nv):
    from constraint import Problem
    problem = Problem()
    # dict_n = {"N" + str(i): 2 for i in range(3, 11)}
    # dict_s = {"S" + str(i): i for i in range(3, 11)}]
    dict_s = dict_sv
    dict_n = dict_nv
    for i, j in enumerate('abcdefg'):
        problem.addVariable(j, range(0, dict_n["N" + str(6 - i + 3)] + 1))
    TS = TSv
    problem.addConstraint(
        lambda a, b, c, d, e, f, g: a * (dict_s["S10"] - dict_s["S9"]) + b * (dict_s["S9"] - dict_s["S8"]) + c * (
                dict_s["S8"] - dict_s["S7"]) + d * (dict_s["S7"] - dict_s["S6"]) + e * (
                                            dict_s["S6"] - dict_s["S5"]) + f * (dict_s["S5"] - dict_s["S4"]) + g * (
                                            dict_s["S4"] - dict_s["S3"]) == TS, ("a", "b", "c", "d", "e", "f", "g"))
    result = problem.getSolutions()
    # 加入全局变量
    global result_g
    result_g = result


def show_data(window, valuse, index=0):
    # 更新数据
    global result_g
    result = result_g
    index = index
    window["num"].Update(str(index + 1))
    window["totle"].Update(str(len(result)))
    update_data = ["P", "TS", "N_new", "Percentage"]
    # 临时存储p列值
    p_v = {}
    for i, j in zip(range(9, 2, -1), "abcdefg"):
        window["P" + str(i)].Update(result[index][j])
        p_v["P" + str(i)] = result[index][j]
    # TS9=P9*(S10-S9)
    for i in range(9, 2, -1):
        window["TS" + str(i)].Update(
            int(p_v["P" + str(i)]) * (int(valuse["S" + str(i + 1)]) - int(valuse["S" + str(i)])))
    # N_new=当前N-晋升上一级N+晋升这一级N

    for i in range(10, 2, -1):
        window["N_new" + str(i)].Update(
            int(valuse["N" + str(i)]) + int(p_v.get("P" + str(i - 1), 0)) - int(p_v.get("P" + str(i), 0)))

    # 晋级比例，用晋级人数除以原来人数
    for i in range(9, 2, -1):
        if int(p_v["P" + str(i)]) == 0:
            continue
        window["Percentage" + str(i)].Update(str("%.2f%%" % (float(p_v["P" + str(i)]) / int(valuse["N" + str(i)]))))


def main_gui():
    st_layout = [
        SG.Text("调薪包"), SG.InputText(key="TS", size=(15, 1))
    ]
    head_attr = {"size": (10, 1)}
    head_layout = [SG.Text("任职"), SG.Text("平均工资（S)", **head_attr),
                   SG.Text("现状人数(N)", **head_attr)]

    head_layout = [SG.Text("任职"), SG.Text("平均工资（S)", **head_attr),
                   SG.Text("现状人数(N)", **head_attr), SG.Text("调薪人数", **head_attr),
                   SG.Text("调薪包", **head_attr), SG.Text("调整后人数", **head_attr), SG.Text("调整比例", **head_attr)]
    # 初始化layout
    main_layout = [st_layout, head_layout]
    # 第一列的名称
    leave_name = ["一级", "二级", "三级", "四级", "五级", "六级", "七级", "八级"]
    leave_name.reverse()
    # 列的名称
    com_name = ["S", "N", "P", "TS", "N_new", "Percentage"]
    # com_name = ["S", "N"]
    # 拼凑各个列的key
    str_name = [[str(i) + str(j) for i in com_name] for j in range(10, 2, -1)]
    text_attr = {"size": (10, 1), "default_text": "0"}
    for i, j in zip(leave_name, str_name):
        main_layout.append([SG.Text(i), *[SG.InputText(**text_attr, key=k) for k in j]])
    end_layout = [SG.Button("计算"), SG.Button("上一个"), SG.Text("", key="num"), SG.Text("", key="totle"), SG.Button("下一个"),
                  SG.Button("Exit")]
    main_layout.append(end_layout)
    window = SG.Window("调薪计算程序", layout=main_layout)
    while True:
        event, values = window.read()
        if event in ["计算"]:
            get_values(window, values)
        if event in ["上一个"]:
            if int(window["num"].get()) == 1:
                SG.Popup("第一个了")
                continue
            else:
                show_data(window, values, int(window["num"].get()) - 2)
                # window["num"].Update(str(int(window["num"].get()) - 1))
        if event in ["下一个"]:
            if int(window['num'].get()) == int(window["totle"].get()):
                # if int(values["num"]) == int(values["totle"]):
                SG.popup("最后一个了")
                continue
            else:
                show_data(window, values, int(window["num"].get()))
                # window["num"].Update(str(int(window["num"].get()) + 1))
        if event in [None, "Exit"]:
            break
    window.close()


if __name__ == '__main__':
    main_gui()
