#!/usr/bin/python
#-*- coding: UTF-8 -*-

author__ = 'cjiang'

import sys
import subprocess
from optparse import OptionParser
import MySQLdb
import json
from tool import allelephrase
#from dbgenetype import getKeyValue

reload(sys)
sys.setdefaultencoding('utf-8')
# 打开数据库连

db = MySQLdb.connect(host='192.168.30.252', port=3306, db='gendb', user='dna', passwd='dna', charset='utf8')
	# 使用cursor()方法获取操作游标 
cursor = db.cursor()
	# SQL 查询语句

#disease = ['高血压','2型糖尿病','高甘油三酯血症','冠状动脉粥样硬化性心脏病（冠心病）','哮喘','脑卒中（中风）','心脏骤停','肺癌','胃癌（胃贲门腺癌）','痛风']	
sql = "select data  from t_riskrate where rsid in (select rsid from t_all_23mofang_rsids where zhname='肺癌') and sex='%d'" %(1)
try:
	# 执行SQL语句
	cursor.execute(sql)
	results = cursor.fetchall()
	newdict={}
	rsids=[]
	orms=[]
	rates=[]
	for riskrate in results:
		ddict=eval(riskrate[0])
		rsid=ddict.get("rsid")
		rsids.append(rsid)
		newdict[ddict.get("rsid")]=ddict.get("rrvalue")
	rsidinfo = {}
	for rsid in rsids:
		SQL = "select Genotype1,Genotype2,Genotype3 from my_population_genotype where rsid='%s' and GenotypeOwn='CHB'" % (rsid)
		cursor.execute(SQL)
		result = cursor.fetchone()
		genotype = {}
		alleles=[]
		for item in result:
			key = item.split(':')
			basekey = key[0].replace(',', '')
			baseValue = key[1].split('|')[1]
			genotype[basekey] = baseValue
			alleles.append(eval(baseValue))
#			print(alleles)
		rsidinfo[rsid] = genotype
		orm=list(newdict.get(rsid).values())
		orms.append(orm)
#		allele=list(rsidinfo.get(rsid).values())
		rates.append(alleles)
#		print(rates)
	ormx=[]
	for a in orms[0]:
		for b in orms[1]:
			for c in orms[2]:
				for d in orms[3]:
					for e in orms[4]:
						for f in orms[5]:		
							total=a*b*c*d*e*f
							ormx.append(total)
		#		print(total)
	ratex=[]
	for aa in rates[0]:
		for bb in rates[1]:
			for cc in rates[2]:
				for dd in rates[3]:
					for ee in rates[4]:
						for ff in rates[5]:			
							sumx=aa*bb*cc*dd*ee*ff
							ratex.append(sumx)
		#		print(sumx)
	print(ormx,ratex)
except:
	print("Error: unable to fecth data")
db.close()

