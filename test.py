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
# chat = tele.bot.get_chat(-1001198682178)
chat = tele.bot.get_chat('@web_record')

def test(url, rotate=False):
	r = weibo_2_album.get(url)
	print(r.imgs)
	print(r.video)
	album_sender.send(chat, url, r, rotate = rotate)
	
if __name__=='__main__':
	test('https://m.weibo.cn/status/4569486260444196')