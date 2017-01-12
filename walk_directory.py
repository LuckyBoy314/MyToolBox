# -*- coding:utf-8 -*-

import os

def FileContentReplace(directory,origin,replace):
	"对directory中所有文件就地替换指定的内容"
	assert os.path.isdir(directory)
	results = []
	for root,dirs,files in os.walk(directory, topdown=True):
		for fl in files:
			results.append(os.path.join(root,fl))
			
	for each_file in results:
		f = open(each_file,'r+')
		all_the_lines=f.readlines()
		f.seek(0)
		f.truncate()
		for line in all_the_lines:
			f.write(line.replace(origin,replace))    
		f.close()

def FileDelete(directory,tag):
	"删除directory中以tag开头的文件"
	assert os.path.isdir(directory)
	results = []
	for root, dirs, files in os.walk(directory, topdown=True):
		for fl in files:
			results.append(os.path.join(root, fl))

	for each_file in results:
		filename =  os.path.basename(each_file)
		if filename.startswith(tag):
			os.remove(each_file)

if __name__ == "__main__":
	FileDelete("D:/T639_HR","17011008")