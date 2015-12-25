#!/usr/bin/python
#-*- coding: UTF-8 -*-

‘ gene has three genetype, exmaple:AA, AT, TT, so there is three generate'

__author__='cjiang'

import os,sys
import logging
import commands
from optparse import OptionParser
import time
import re
import math
import numpy
import scipy
import multiprocessing


def parseCommand():
	usage = "usage: %prog <-1 input1> <-2 input2> <-3 input3> <-4 input4> <-o outputDir>"
	version = "%prog 1.0"
	parser = OptionParser(usage = usage, version = version)
	parser.add_option("-1", "--input1", dest = "input1", help = "the rs number")
	parser.add_option("-2", "--input2", dest = "input2", help = "incidence of a disease")
	parser.add_option("-3", "--input3", dest = "input3", help = "OR1疾病的杂合基因型OR值".decode("utf8"))
	parser.add_option("-4", "--input4", dest = "input4", help = "OR2疾病的杂合基因型OR值".decode("utf8"))
	parser.add_option("-5", "--input5", dest = "input5", help = "OR3疾病的纯合基因型OR值".decode("utf8")
	parser.add_option("-o", "--output", dest = "output", default = "/data2/output", help = "输出目录".decode("utf8"))
	return parser.parse_args()

	
def getgenetype(listrs, genetype):
	if options.input1 == None:
		print "input1 is required, use -1 <file name> to specify"
		print "see -h for help"
		sys.exit(-1)
	listrs = {}
	for i in lenrs
def getgenerate():





def getriskrate():

	



		
def equations(p):
	x, y ,z = p 
	return (a*x+b*y+c*z-options.input4, y*(1-x)/x*(1-y)-options.input2, z*(1-x)/x*(1-z)-options.input3)
	x, y ,z = fsolve(equations, (0.01, 0.01, 0.01))
	print ("equations((x, y, z))")
		
	
def getResult(AA=-1,AT=-1,AC=-1,AG=-1,TT=-1,TC=-1,TG=-1,CC=-1,CG=-1,GG=-1):
	dict={}
	result={}
	if AA!=-1 
		dict.insert('AA',AA)
		result.insert('AA','')
	if len(dict)=3:

	for i in dict:
	    result.getkey(dict(key1)),key2,key3=equations（dict.val,val,）
		
	

	
def getOR(orx, ory, orz):	
	orx = options.input2/x
	ory = options.input2/y
	orz = options.input2/z
		

def SNP(ployrs, oddsrate):
	ployrs = orx* ory*orz
	oddsrate = ployrs/input2
	
def diseaseRR():

 



def main():
	time1 = time.time()
	(options, args) = parseCommand()
	
	if options.input3 == None:
		print "input3 is required, use -3 <file name> to specify"
		print "see -h for help"
		sys.exit(-1)
	if options.input4 == None:
		print "input4 is required, use -4 <file name> to specify"
		print "see -h for help"
		sys.exit(-1)
	if options.input2 == None:
		return genetypeRR
	if options.input2 != None:
		return diseaseRR
	
	
	
	
	

	if options.input2 != None:
		
	
	
	
	
	
	
	
		print "input2 is required, use -2 <file name> to specify"
		print "see -h for help"
		sys.exit(-1)
	
	return 1
	

	
if __name__ == "__main__"
	main()
	
	
	
