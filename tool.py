#coding:utf-8
__author__ = 'similarface'
import json
def dictConvertJson(dict):
    '''
    将字典转化成Json进行返回
    :param dict:字典
    :return:json对象
    '''
    return json.dumps(dict,sort_keys=True)

def allelephrase(str):
    b=[]
    for i in str:
       b.append(i)
    b.sort()
    return ''.join(b)

if __name__=="__main__":
    print(allelephrase('AG'))
