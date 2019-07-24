#coding:utf-8
import os,configparser

cur_path = os.path.dirname(os.path.relpath(__file__))
configPath = os.path.join(cur_path,"cfg.ini")
conf = configparser.ConfigParser()
conf.read(configPath)


smtp_server = conf.get("email","smtp_server")

sender = conf.get("email","sender")

psw = conf.get("email","psw")

port = conf.get("email","port")

receiver = conf.get("email","receiver")