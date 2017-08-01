#!/usr/bin/python

import bottle
import os
from bottle import route, get, post, run, template, static_file, request, redirect
from talkpp import pp_configs, command

base_path = os.path.abspath(os.path.dirname(__file__))
views_path = os.path.join(base_path, 'views')
bottle.TEMPLATE_PATH.insert(0, views_path)

HOST = '0.0.0.0'
PORT = 8080
DEBUG = True 

@get('/<filename:re:.*\.css>')
def stylesheets(filename):	
	return static_file(filename, root='static/css/')

@post('/payload')
def button_payload():
	arg = request.POST.get('btn0')
	command(arg)
	redirect('/general')

@route('/')
def index():
	setting_group = 'general'
	return template('info_table', dict = pp_configs(setting_group), group = setting_group)

@route('/<setting_group>')
def get_table(setting_group):
	return template('info_table', dict = pp_configs(setting_group), group = setting_group)

run(host=HOST, port=PORT, debug=DEBUG, reloader=True)
