# -*- coding: UTF-8 -*-

'''gene has three genetype, exmaple:AA, AT, TT, so there is three generate'''

__author__ = 'cjiang'
from scipy.optimize import fsolve
from dbgenetype import DBHelp
from tool import allelephrase
from tool import dictConvertJson
ddict = {}
sex = 0

def f(x):
    '''
    计算
    :param x:
    :return:
    '''
    genedbsnp = ddict
    allele = genedbsnp.get("orvalue").get("k")
    x, y, z = x.tolist()
    allele0=float(genedbsnp.get("genotype").get(allelephrase(allele[0])))
    allele1=float(genedbsnp.get("genotype").get(allelephrase(allele[1])))
    allele2=float(genedbsnp.get("genotype").get(allelephrase(allele[2])))
    orvalue1=float(genedbsnp.get("orvalue").get("v")[1])
    orvalue2=float(genedbsnp.get("orvalue").get("v")[2])
    a= allele0 * x + allele1 * y + allele2 * z - float(genedbsnp.get("prd").get(sex))
    b=y * (1 - x) / (x * (1 - y)) - orvalue1
    c=z * (1 - x) / (x * (1 - z)) - orvalue2
    return a,b,c
   
#{"genotype": {"CC": "0.7184", "CT": "0.2621", "TT": "0.0194"}, "orvalue": {"CC": "1", "CT": "1.3", "TT": "1.69"}, "prd": {"0": "0.29000", "1": "0.29000"}, "rsid": "rs381815"}


def getResult(dbconn,rsid):
    '''
    返回rsid的详细信息
    :param dbconn:数据库对象
    :param rsid:
    :return:rsid的详细信息
    '''
    with DBHelp() as dbhelp:
        rsidinfo = dbhelp.getGenotypeInfo(rsid)
    return rsidinfo

def getDBHelp():
    '''
    获取数据库连接和接口类
    :return:返回数据库操作实例
    '''
    return DBHelp()

if __name__ == "__main__":
    dbconn=getDBHelp()
  #  rsids = ['rs381815','rs2681472','rs751141','rs1799998','rs5443','rs1801253','rs1801058','rs7172432','rs1501299','rs7612463','rs2237892','rs231359','rs17584499','rs391300']
    rsids=["rs138694505"]
    #rsids=["rs381815"]
    result = (0.1, 0.1, 0.1)
    for rsid in rsids:
        ddict=getResult(dbconn,rsid)
        #男女循环
    #     for i in range(0,2):
    #         sex=i
    #         r = fsolve(f, result)
    #         print(rsid,sex,r)
        allele = ddict.get("orvalue").get("k")
        for i in range(0,2):
            sex=i
            prd = float(ddict.get("prd").get(sex))
            r = fsolve(f, result)
            orm = r*(1-prd) /(prd*(1-r))
            riskrate = dict(([allele[0],orm[0]],[allele[1],orm[1]],[allele[2],orm[2]]))
            print(rsid,sex,riskrate)
    dbconn.close()
