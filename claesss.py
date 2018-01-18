#!/usr/bin/python
# -*- coding: utf-8 -*- Module for sopel. Will fetch html from claes.cash and display latest data in your IRC channel. 
# https://github.com/erikpi/
import sys
import os
import requests, json 
import re 
import locale 

locale.setlocale(locale.LC_ALL, 'sv_SE') 

def parseclaes(siten):
    siten = "https://claes.cash/"
    web_handle = urllib2.urlopen(siten)
    r = requests.get(siten)
#        if not r.status_code == 200
 #           return None

    response = r.text
    data = json.loads(response)
    if not data:
        return None
    tweets = re.findall('Claes har gjort <span id ="weeksTweetsbetsec" title="Nya tweets hittils"></span>', r.text)

@module.commands('cc') 
def cc(bot,trigger):
    bot.say(tweets)
