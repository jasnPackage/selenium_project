#coding:utf-8
import os,yaml


def parseyaml():
    # 当前脚本路径的父类
    basepath = os.path.dirname(os.path.dirname(__file__))

    yaml_path = basepath + "/PageElement"
    # print(yaml_path)

    pageElement = {}
    # 遍历读取yaml文件

    for fpath,dirname,fnames in os.walk(yaml_path):
        # print("fpath:%s"%fpath)
        # print("dirname:%s"%dirname)
        # print("fnames:%s" % fnames)

        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath,name)
            # print(yaml_file_path)

            # 排除一些非.yaml的文件
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path,'r',encoding='utf-8') as f:
                    page = yaml.load(f)
                    pageElement.update(page)

    # print(pageElement["baiduPage"]["search_box"]["value"])
    return pageElement


