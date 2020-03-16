#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'weibo_2_album'

import math
import os
import cached_url
import re
import yaml

prefix = 'https://m.weibo.cn/statuses/show?id='

def getWid(path):
	index = path.find('?')
	if index > -1:
		path = path[:index]
	return path.split('/')[-1]

def get(path):
	wid = getWid(path)
	json = yaml.load cached_url.get(prefix + wid)
	

