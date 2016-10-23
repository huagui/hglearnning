# -*- coding:UTF-8 -*-
a = u'''id,price,f_name,l_name,phone,adree,name
		112,23,aaa,bb,ccc,ddd,哈哈
113,24,aaa,bb,ccc,ddd,哈哈
'''


def analyse_csv(data,column=None):
	# print data
	if '\n' in data:
		record_lsit = data.split('\n')
		# print record_lsit
		data_index = 0
		if column:
			data_index = 1
			key_list = record_lsit[0].split(',')
		children_list = []
		# print key_list
		for record in record_lsit[1:]:
			
			if ',' in record:
				children = {}
				for index,item in enumerate(record.split(',')):
					# print key_list[index] , item
					children[key_list[index]]=item
				children_list.append(children)
		return children_list

	else:
		return None

if __name__ == '__main__':
	children_list =  analyse_csv(a,True)
	print len(children_list)
	for i in children_list:
		print i
