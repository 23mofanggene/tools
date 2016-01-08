#!/usr/bin/python
#-*- coding: UTF-8 -*-

import MySQLdb
import sys
from tool import allelephrase

reload(sys)
sys.setdefaultencoding('utf-8')
# 打开数据库连接

db = MySQLdb.connect(host='192.168.30.252', port=3306, db='gendb', user='dna', passwd='dna', charset='utf8')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
disease = ['高血压','2型糖尿病','高甘油三酯血症','冠状动脉粥样硬化性心脏病（冠心病）','哮喘','脑卒中（中风）','心脏骤停','肺癌','胃癌（胃贲门腺癌）','痛风']
for item in disease:	
	sql = "select data  from t_riskrate where rsid in (select rsid from t_all_23mofang_rsids where zhname='%s') and sex='%d'" %(item , 1)
#	print(item)
	try:
	# 执行SQL语句
		cursor.execute(sql)
   		# 获取所有记录列表
		large=[]
		small=[]
		up=1
		down=1
		newdict={}
		rsid=[]
		results = cursor.fetchall()
		for riskrate in results:
			ddict=eval(riskrate[0])
#			print(ddict)
			orm=list(ddict.get("rrvalue").values())
			ss=max(orm)
			dd=min(orm)
			newdict[ddict.get("rsid")]=ddict.get("rrvalue")
			large.append(ss)
			small.append(dd)
			rsid.append(ddict.get("rsid"))
		for i in large:
			up*=i
#		print(up)
		for j in small:
			down*=j
#		print(down)
#		length = len(results)

		genetype = "SELECT rsid, snp_vcf.`GENTYPE` AS ref FROM snp_vcf WHERE sampleid = '111-1111-2490' AND rsid IN (SELECT rsid FROM t_all_23mofang_rsids WHERE zhname = '%s') UNION ALL SELECT rsid, concat(ref,ref) AS ref FROM `T_DBSNP_HG19_138` WHERE `T_DBSNP_HG19_138`.`RSID` IN (SELECT rsid FROM t_all_23mofang_rsids WHERE zhname = '%s') AND `T_DBSNP_HG19_138`.`RSID` NOT IN (SELECT rsid FROM snp_vcf WHERE sampleid = '111-1111-2490' AND rsid IN (SELECT rsid FROM t_all_23mofang_rsids WHERE zhname = '%s'))" %(item,item,item)
		cursor.execute(genetype)
		allele = cursor.fetchall()
#		total = len(allele)
#		print(allele)
		genestyle={}
		for gene in allele:
			k,v=(gene[0],gene[1])
			genestyle[k]=v
#		print(genestyle)
		orx=[]
		c=1
		for id in rsid:
			orx.append(newdict.get(id).get(allelephrase(genestyle.get(id))))
		for m in orx:
			c*=m
		print str(item)+ ','+str(down) +','+str(c) +','+str(up)
	except Exception,e:
   		print("Error: unable to fecth data")
   		print(e)
db.close()

