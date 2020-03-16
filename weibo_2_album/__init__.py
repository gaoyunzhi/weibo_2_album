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

prefix = 'https://m.weibo.cn/statuses/show?id='

def getWid(path):
	index = path.find('?')
	if index > -1:
		path = path[:index]
	return path.split('/')[-1]

def getCap(json, cap_limit):
	text = html2markdown.convert(json['text'])
	return cutCaption(text, '', cap_limit)

def getImages(json, image_limit):
	raw = [x['url'] for x in json['pics']]
	return pic_cut.getCutImages(raw, image_limit)

def get(path, cap_limit = 1000, img_limit = 9):
	wid = getWid(path)
	json = yaml.load(cached_url.get(prefix + wid), Loader=yaml.FullLoader)
	json = json['data']
	return getImages(json, img_limit), getCap(json, cap_limit)

	

