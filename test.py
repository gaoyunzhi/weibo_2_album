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

def test(url, rotate=False):
	r = weibo_2_album.get(url)
	album_sender.send(chat, url, r, rotate = rotate)
	
if __name__=='__main__':
	test('https://m.weibo.cn/status/ICZq9agmD?mblogid=ICZq9agmD&luicode=10000011&lfid=1076036520732164')
	# test('http://weibointl.api.weibo.cn/share/138804312.html?weibo_id=4492279152896775&from=groupmessage&isappinstalled=0')