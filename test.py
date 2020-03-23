#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import weibo_2_album
import yaml
from telegram.ext import Updater
import album_sender

with open('CREDENTIALS') as f:
	CREDENTIALS = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(CREDENTIALS['bot_token'], use_context=True)
chat = tele.bot.get_chat(-1001198682178)

def test(url, rotate=False):
	r = weibo_2_album.get(url)
	album_sender.send(chat, url, r, rotate = rotate)

	if rotate:
		for index, img_path in enumerate(imgs):
			img = Image.open(img_path)
			img = img.rotate(180)
			img.save(img_path)
			img.save('tmp_image/%s.jpg' % index)
	
if __name__=='__main__':
	test('https://m.weibo.cn/status/4483347235306786')
	# test('http://weibointl.api.weibo.cn/share/131595305.html', rotate=True)
	# test('http://www.douban.com/people/zhuyige/status/2869326971/')