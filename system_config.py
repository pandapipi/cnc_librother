#!/usr/bin/env python3
# import yaml
# # yaml文件中含有多个文档时，分别获取文档中数据
# user_yam_file = 'ym_config.yaml'
# def get_yaml_load_all(yaml_file):
#     # 打开yaml文件
#     file = open(yaml_file, 'r', encoding="utf-8")
#     file_data = file.read()
#     file.close()
#     all_data = yaml.load(file_data, Loader=yaml.FullLoader)
#     return all_data
#     # for data in all_data:
#     #     print(data)
# def write_yam_config(udict,yaml_file):
#     try:
#         with open(yaml_file,'w')as f:
#             data = yaml.dump(udict,f)
#     except:
#         pass
# def change_yam_data(key,value):
#     uudict = get_yaml_load_all(user_yam_file)
#     uudict[key] = value
#     print(uudict)
#     write_yam_config(uudict,user_yam_file)
# if __name__ == '__main__':
#     ud = get_yaml_load_all(user_yam_file)
#     print(ud)
#     #change_yam_data('SysIP','COM3')
import yaml
import os
sys_yaml_file = "ym_config.yaml"
class SysConfigYaml:

    def __init__(self,yaml_file):

        self.yamlfile = yaml_file
        current_path = os.path.abspath(".")
        self.yaml_path = os.path.join(current_path, self.yamlfile)
        self.p_yaml = self.get_yaml_data()
        print(self.p_yaml)
    def get_yaml_data(self):
        try:
            # 打开yaml文件
            print("***获取yaml文件数据***")
            file = open(self.yaml_path, 'r', encoding="utf-8")
            file_data = file.read()
            file.close()
            #
            # print(file_data)
            # print("类型：", type(file_data))
            #
            # # 将字符串转化为字典或列表
            # print("***转化yaml数据为字典或列表***")
            data = yaml.load(file_data)
            # print(data)
            # print("类型：", type(data))
            return data
        except:
            return None

    def GetPhase(self,phase):
        try:
            return(self.p_yaml[phase])
        except:
            return None
    def GetPKey(self,phase,key):
        try:
            return(phase.get(key))
        except:
            return None
    def SetValue(self,phase,key,value):
        try:
            phase[key] = value
            return phase
        except:
            return None
    def SaveYamlFile(self):
        try:
            file = open(self.yaml_path, 'w', encoding='utf-8')
            yaml.dump(self.p_yaml, file)
            file.close()
            return True
        except:
            return None
if __name__ == '__main__':
    # current_path = os.path.abspath(".")
    # yaml_path = os.path.join(current_path, "ym_config.yaml")
    # p_yaml = get_yaml_data(yaml_path)
    # t = GetValue(p_yaml,'RelayMachine')
    # Com = t['Com']
    # print('...')
    # print(t)
    # print(Com)
    # print(type(Com))
    # SetValue(t,'Add',3)
    # print(t)
    y = SysConfigYaml(sys_yaml_file)
    print( y.get_yaml_data())
    ph = y.GetPhase('TouchTestMachine')
    print(y.GetPKey(ph,'Com'))
    y.SetValue(ph,'Bard',9600)
    print(ph)
    y.SaveYamlFile()
