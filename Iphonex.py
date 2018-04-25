#-*-coding:utf-8-*-
import requests
import re
import sys

class downloader(object):

	def __init__(self):
		self.names = []
		self.prices=[]
		self.nums=[]
		self.url='https://s.taobao.com/search?q=iphonex&imgfile=&ie=utf8&app=detailproduct&through=1'

	def get_data(self,url):
		#url = 'https://s.taobao.com/search?q=iphonex&imgfile=&ie=utf8&app=detailproduct&through=1'
		html = requests.get(url)
		html.encoding = 'utf-8'
		data = html.text
		self.names = re.findall(r'"raw_title":"([^"]+)"',data,re.I)
		self.prices = re.findall(r'"view_price":"([^"]+)"',data,re.I)
		self.nums = len(self.prices)

	def writer(self,name,path,price):
		with open(path,'a',encoding = 'utf-8') as f:
			f.write(name+'\n')
			f.write(price)
			f.write('\n\n')

if __name__ == '__main__':
	dl = downloader()
	dl.get_data(dl.url)
	print('The information of IPhone X is downloading:')
	for i in range(dl.nums):
		dl.writer("name:" + dl.names[i],'iphonex.txt',"the price is :"+dl.prices[i])
		sys.stdout.write('Progress Status:%.1f%%' % float(i/dl.nums*100)+'\r')
		sys.stdout.flush()
	print('finish!!')
