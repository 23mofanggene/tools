# coding:utf-8
import MySQLdb
import json
from tool import allelephrase


class DBHelp:
    def __init__(self):
        '''
        获取数据库连接 __enter__函数配合with 使用 自动调用 enter 和 exit
        :return:
        '''
        try:
            self.__db = MySQLdb.connect(host='192.168.30.252', port=3306, db='gendb', user='dna', passwd='dna',
                                        charset='utf8')
            self.__cursor = self.__db.cursor()
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            error_msg = 'MySQL error! ', e.args[0], e.args[1]
            print error_msg

    def __enter__(self):
        '''
        获取数据库连接 __enter__函数配合with 使用 自动调用 enter 和 exit
        :return:
        '''
        if self.__db==None:
            self.__db = MySQLdb.connect(host='192.168.30.252', port=3306, db='gendb', user='dna', passwd='dna',
                                    charset='utf8')
        if self.__cursor==None:
            self.__cursor = self.__db.cursor()
        return self


    def inserIntoRiskrate(self,rsid,sex,jsons):
        SQL='insert into t_riskrate(rsid,sex,data) values (%s,%s,%s)'
        self.__cursor.execute(SQL,(rsid,sex,jsons))
        self.__db.commit()

    def __exit__(self, type, value, traceback):
        self.__db.close()

    def close(self):
        self.__db.close()

    def getKeyValue(self, str):
        key = str.split(':')
        basekey = key[0].replace(',', '')
        baseValue = key[1].split('|')[1]
        return allelephrase(basekey), baseValue

    def getOrValueKeyValue(self,str):
        strs=str.split(':')
        k=allelephrase(strs[0])
        v=strs[1]
        return k,v

    def getGenotypeInfo(self, rsid):
        '''
        :param rsid:返回Genotype的概率
        :return:{"rs955988": {"CC": "0.0680", "TC": "0.3786", "TT": "0.5534"}}
        '''
        rsidinfo = {}
        rsidinfo['rsid']=rsid
        SQL = "select Genotype1,Genotype2,Genotype3 from my_population_genotype where rsid='%s' and GenotypeOwn='CHB'" % (rsid)
        self.__cursor.execute(SQL)
        result = self.__cursor.fetchone()
        genotype = {}
        for item in result:
            gtk, gtv = self.getKeyValue(item)
            genotype[gtk] = gtv
        rsidinfo['genotype'] = genotype
        orvalue={}
        prd={}
        SQL = "select control,het ,hom ,malePrd ,femalePrd from t_health_risks where rsid='%s'" % (rsid)
        self.__cursor.execute(SQL)
        result = self.__cursor.fetchone()
        malePrd=result[3]
        femalePrd=result[4]
        controlk,controlv=self.getOrValueKeyValue(result[0])
        homk,homv=self.getOrValueKeyValue(result[1])
        hetk,hetv=self.getOrValueKeyValue(result[2])
        oravaluelistk=[]
        oravaluelistv=[]
        if controlv=="1":
            oravaluelistk.append(controlk)
            oravaluelistv.append(controlv)
            if float(homv) <= float(hetv):
                oravaluelistk.append(homk)
                oravaluelistv.append(homv)
                oravaluelistk.append(hetk)
                oravaluelistv.append(hetv)
            else:
                oravaluelistk.append(hetk)
                oravaluelistv.append(hetv)
                oravaluelistk.append(homk)
                oravaluelistv.append(homv)


        elif homv=="1" and controlv!="1":
            oravaluelistk.append(homk)
            oravaluelistv.append(homv)
            if float(hetv)<=float(controlv):
                oravaluelistk.append(hetk)
                oravaluelistv.append(hetv)
                oravaluelistk.append(controlk)
                oravaluelistv.append(controlv)
            else:
                oravaluelistk.append(controlk)
                oravaluelistv.append(controlv)
                oravaluelistk.append(hetk)
                oravaluelistv.append(hetv)



        elif hetv=="1" and homv!="1" and controlv!="1":
            oravaluelistk.append(hetk)
            oravaluelistv.append(hetv)
            if float(homv)<=float(controlv):
                oravaluelistk.append(homk)
                oravaluelistv.append(homv)
                oravaluelistk.append(controlk)
                oravaluelistv.append(controlv)
            else:
                oravaluelistk.append(controlk)
                oravaluelistv.append(controlv)
                oravaluelistk.append(homk)
                oravaluelistv.append(homv)



        orvalue["k"]=oravaluelistk
        orvalue["v"]=oravaluelistv
        prd[0]=str(femalePrd)
        prd[1]=str(malePrd)
        rsidinfo['orvalue']=orvalue
        rsidinfo['prd']=prd
        #return json.dumps(rsidinfo, sort_keys=True)
        return rsidinfo

if __name__ == "__main__":
    with DBHelp() as dbhelp:
        print(dbhelp.getGenotypeInfo('rs1801058'))

