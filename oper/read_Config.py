#coding=utf-8
#!usr/bin/python
import os
import configparser
import filePath#引入我们自己的写的获取路径的类

path = filePath.get_Path()#调用实例化，还记得这个类返回的路径为C:\Users\songlihui\PycharmProjects\dkxinterfaceTest
config_path = os.path.join(path,'test_data','config.ini')#项目目录+上后边文件夹及文件名
print(config_path)
config = configparser.ConfigParser()#调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')
print(config.sections())

class ReadConfig():
    def get_config_str(self, sections,option):
        value = config.get(sections,option)
        return value
    def get_config_int(self,section,option):
        value = config.getint(section,option)
        return value
    def get_config_boolean(self,section,option):
        value = config.getboolean(section,option)
        return value
    def get_config_float(self,section,option):
        value = config.getfloat(section,option)
        return value
    # def get_config_str(self,section,option):
    #     return self.conf.get(section,option)
    #
    # def get_config_boolean(self,section,option):
    #     return self.conf.getboolean(section,option)
    #
    # def get_config_int(self,section,option):
    #     return self.conf.getint(section,option)
    #
    # def get_config_float(self,section,option):
    #     return self.conf.getfloat(section,option)
    # def get_http(self,sections, name):
    #     value = config.get('HTTP', name)
    #     return value
    # def get_email(self, sections,name):
    #     value = config.get(sections, name)
    #     return value
    # def get_mysql(self, name):#数据库
    #     value = config.get('DATABASE', name)
    #     return value


if __name__ == '__main__':#测试一下，我们读取配置文件的方法是否可用
    print('HTTP中的baseurl值为：', ReadConfig().get_config('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_config('on_off'))


