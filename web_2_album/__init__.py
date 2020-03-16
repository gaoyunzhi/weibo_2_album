#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'weibo_2_album'

import math
import os
import cached_url

prefix = 'https://m.weibo.cn/statuses/show?id='

def get(path):
	wid = re.split('(/|\?)', path)
	cached_url.get(prefix + wid)
	

