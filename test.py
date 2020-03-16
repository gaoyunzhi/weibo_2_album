#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import weibo_2_album

def test():
	print(weibo_2_album.get('https://m.weibo.cn/status/4483347235306786'))
	# print(weibo_2_album.get(
	# 	'https://www.weibo.com/1648544895/IyEMGc6xw'))
	# print(weibo_2_album.get(
	# 	'https://www.weibo.com/6433426551/IuUsbf8m6?filter=hot&root_comment_id=0&type=comment')
	# print(weibo_2_album.get(
	# 	'https://www.weibo.com/1588066533/Iu6Q9rxsA?type=comment#_rnd1584356495395')
	# print(weibo_2_album.get(
	# 	'https://www.weibo.com/tv/v/IysDf4bn9?fid=1034:4482128985915435')
	
if __name__=='__main__':
	test()