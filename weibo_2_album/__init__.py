#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'weibo_2_album'

import math
import os
import cached_url
import re
import yaml
from telegram_util import cutCaption
import pic_cut
from bs4 import BeautifulSoup

prefix = 'https://m.weibo.cn/statuses/show?id='

def getWid(path):
	index = path.find('?')
	if index > -1:
		path = path[:index]
	return path.split('/')[-1]

def getCap(json, cap_limit):
	text = json['text']
	b = BeautifulSoup(text, features="html.parser")
	while b.find('a'):
		elm = b.find('a')
		md = '<div class="weibo_2_album">[%s](%s)</div>' % \
			(elm.text, elm['href'])
		print(BeautifulSoup(md, features='html.parser').find('div', class_='weibo_2_album'))
		elm.replaceWith(BeautifulSoup(md, features='html.parser').\
			find('div', class_='weibo_2_album'))
	return cutCaption(b.text, '', cap_limit)

def getImages(json, image_limit):
	raw = [x['url'] for x in json['pics']]
	return pic_cut.getCutImages(raw, image_limit)

def get(path, cap_limit = 1000, img_limit = 9):
	wid = getWid(path)
	json = yaml.load(cached_url.get(prefix + wid), Loader=yaml.FullLoader)
	json = json['data']
	return getImages(json, img_limit), getCap(json, cap_limit)

	

