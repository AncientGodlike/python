#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import sys

class downloader(object):

	def __init__(self):
		#define th target webisite
		self.server = 'http://www.51shucheng.net/'
		self.target ='http://www.51shucheng.net/kehuan/santi'
		self.names = []     
		self.urls = []
		self.nums = 0

	#to get all the url
	def get_download_url(self):
		req = requests.get(url=self.target)
		req.encoding ='utf-8'
		html = req.text
		div_soup = BeautifulSoup(html,'lxml')
		div = div_soup.find_all('div',class_='mulu-list')
		a_soup = BeautifulSoup(str(div))
		a = a_soup.find_all('a')
		self.nums = len(a)
		for each in a:
			self.names.append(each.string+each.get('href'))
			self.urls.append(self.server+each.get('href'))

	def get_contents(self,url):
		url='http://www.51shucheng.net/kehuan/santi/santi1/174.html'
		data = requests.get(url)
		data.encoding='utf-8'
		html = data.text
		soup = BeautifulSoup(html,'lxml')
		texts = soup.find_all('div',class_="neirong")
		texts = texts[0].text.replace('\xa0'*8,'\n\n')
		return texts

	def writer(self,name,path,text):
		write_flag = True
		with open(path,'a',encoding = 'utf-8') as f:
			f.write(name+'\n')
			f.writelines(text)
			f.write('\n\n')

if __name__ == '__main__':
	dl = downloader()
	dl.get_download_url()
	print('The task of dowloading SanTi is starting:')
	for i in range(dl.nums):
		dl.writer(dl.names[i],'三体.txt',dl.get_contents(dl.urls[i]))
		sys.stdout.write(' Progress Status:%.1f%%' % float(i/dl.nums*100)+'\r')
		sys.stdout.flush()
	print('done!')

