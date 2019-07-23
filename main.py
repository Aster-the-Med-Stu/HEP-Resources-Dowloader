# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:27:48 2019

@author: Aster-the-Med-Stu

Always believe something pawsome is about to happen🐾🐾
"""

import requests, json
# getpass 这个库是哪个逗比想起来的这个用法……
from getpass import getpass
# from multiprocessing.pool import ThreadPool
from getch import pause_exit
# Tk 用于弹出选择文件夹的界面
# import tkinter as tk
# from tkinter import filedialog
# 貌似我想多了诶，直接放在同一个文件夹下不就好了……
import os

# 用 Session 应对 Abook 自动更新
session = requests.Session()

# 没错，登陆的时候密码是明文传输的……
Login_URL = "http://abook.hep.com.cn/loginMobile.action"
Check_Login_URL = "http://abook.hep.com.cn/verifyLoginMobile.action"

# 其他 URL
Courses_Info_URL = "http://abook.hep.com.cn/selectMyCourseList.action?mobile=true&cur=1"
Course_Contents_Structure_URL = "http://abook.hep.com.cn/resourceStructure.action"
Course_Get_Resource_Info_URL = "http://abook.hep.com.cn/courseResourceList.action"
Download_URL = "http://abook1.hep.com.cn"
# 这里我使用了 mitmproxy 配合 Postern 获取的手机端 Abook API


def GetCookies():
    Login_Response = session.post(Login_URL,
                                   data={
                                       "loginUser.loginName": Username,
                                       "loginUser.loginPassword": Password
                                   })
    print(Login_Response)
    Cookies = Login_Response.cookies.get_dict()
    return Cookies


def CheckLogin(Cookies):
    Login_Result_JSON = session.post(Check_Login_URL, cookies=Cookies)
    #Login_Result_JSON = session.post(Check_Login_URL)
    return Login_Result_JSON


def GetJSON(Input_URL, Cookies):
    # Result_JSON = session.get(Input_URL, cookies=Cookies)
    Result_JSON = session.get(Input_URL, cookies=Cookies).json()
    return Result_JSON


def GetCourseContentsStructure(course_Info_ID, Cookies):
    payload = {'courseInfoId':course_Info_ID}
    Result_JSON = session.post(Course_Contents_Structure_URL, params = payload, cookies=Cookies).json()
    return Result_JSON

def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)


def Write_Contents():
    pass
    # package_name = response['Package'][0]['fields']['name']
    # for doc in response['Document']:
    #     path = os.path.join(package_name, doc[0]['fields']['name'])
    #     basedir = os.path.dirname(filename)
    #     if not os.path.exists(basedir):
    #         os.makedirs(basedir)

    #     content = doc[0]['fields']['content']
    #     with open(filename, "w") as f:
    #         f.write(content)


if __name__ == '__main__':
    # Username = input("请输入您登陆 Abook 的时候使用的用户名：\n")
    # Password = getpass("请输入您的密码（输入的时候看不见任何东西）：\n")
    # 一句小小的提醒
    Username = "marchhappy"
    Password = ""
    print(
        "\n友情提醒：\n您与高等教育出版社的 Abook 服务器之间的数据，在互联网上是明文传输的，这意味着任何有心人都能“看到”您 Abook 的密码。\n如果您的 Abook 密码和别的常用软件，例如 QQ，重复的话，强烈建议修改！！！\n"
    )
    print("Logging you in...")
    # 判断登陆是否成功
    #Cookies = GetCookies()
    # print(Cookies)
    # Cookies = {
    #     'SERVERID': '987ae75ad05152c48774f44de4990a8c|1559462205|1559460849',
    #     'icourse_SESSION': 'A40DC197AEEA69617C117B0F7C537B9F'
    # }
    Cookies = {'SERVERID': '987ae75ad05152c48774f44de4990a8c|1563876843|1563876843', 'icourse_SESSION': '995B2252774A9FEF72CCF95670514EE6'}
    Login_Result = CheckLogin(Cookies)
    # print(Login_Result.title)
    # 此处有错，因为 requests 木有 title 这个属性，当然意思是这个意思
    # elif Login_Result.title == "用户失效":
    #     print("用户名或密码错误，请检查……（若确认无误，麻烦开一个 Issue 以协助排查）")
    if Login_Result.text == "{\"message\":\"已登录\"}":
        pass
    else:
        print("登陆失败，麻烦开个 Issue 以协助排查您的问题……错误信息：\n")
        print(Login_Result)
        print(Login_Result.text)
        pause_exit('按任意键退出...')
    print("Login OK")
    # 获取账户下的所有课程列表
    Lessons_JSON = GetJSON(Courses_Info_URL, Cookies)
    Lessons_List = Lessons_JSON[0]["myMobileCourseList"]

    # 选择需要下载的课程序号，获取课程信息以及 print 所有资源类型
    for index, book in enumerate(Lessons_List):
        print('[%d] | %s' % (index, book['courseTitle']))
    choice = int(input('Input the index of the file you want:\n'))
    
    Structure_JSON = GetCourseContentsStructure(Lessons_List[choice]['courseInfoId'], Cookies)
    #for index, book in enumer
    # Folder_List = [i:Folder_List [i] if Structure_JSON[i]['type'] == 5]
#    Folder_List = []
#    for i in Structure_JSON:
#        if i['type'] == 5:
#            Folder_List.append(i)
    # 还是 Pythonic 一点的写法吧……
    Chapter_List = [i for i in Structure_JSON if i['type'] == 5]
    Folder_List = list(filter(lambda x:))
    # 当然实际上还有一种写法，用的 lambda 函数
    # Chapter_List = list(filter(lambda x: x['type'] == 5, Stucture_JSON))
    # 排除资源类型
    
    # 包含资源类型

    # 操作 dict，按章节整理资源

    # dict 转 目录结构，以及从 dict 中获取文件名

    # Prompt for saving locationg

    # 下载资源，写入

    # 询问是否还需要下载下一本书