#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import weibo_2_album
import yaml
from telegram.ext import Updater
import album_sender
import os

with open('CREDENTIALS') as f:
	CREDENTIALS = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(CREDENTIALS['bot_token'], use_context=True)
chat = tele.bot.get_chat(-1001198682178)
# channel = tele.bot.get_chat('@web_record')

def test(url, rotate=False):
	r = weibo_2_album.get(url)
	print(r)
	album_sender.send(chat, url, r, rotate = rotate)
	
if __name__=='__main__':
	test('http://m.weibo.cn/status/JvnZsz6Lb')