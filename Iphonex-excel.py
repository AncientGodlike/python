#-*-coding:utf-8-*-
import requests
import re
import sys
import xlwt

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

	book = xlwt.Workbook(encoding='utf-8',style_compression=0)
	sheet = book.add_sheet('iphonex',cell_overwrite_ok=True)


	
	for i in range(dl.nums):
		#dl.writer(str(i+1)+"." + "name:" + dl.names[i],'iphonex.csv',"the price is :"+dl.prices[i])
		sheet.write(0,0,'商品名称')
		sheet.write(0,1,'销售价格')
		sheet.write(i+1,0,dl.names[i])
		sheet.write(i+1,1,dl.prices[i])
		book.save('iphonex.xls')

		sys.stdout.write('Progress Status:%.1f%%' % float(i/dl.nums*100)+'\r')
		sys.stdout.flush()
	print('finish!!')
