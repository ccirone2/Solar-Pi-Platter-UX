#!/usr/bin/python

from bottle import route, get, post, run, template, static_file, request
from talkpp import pp_configs, command

HOST = '0.0.0.0'
PORT = 8080
DEBUG = True 

@get('/<filename:re:.*\.css>')
def stylesheets(filename):	
	return static_file(filename, root='static/css/')

@post('/payload')
def button_payload():
	button_label = request.POST.get('btn_lbl')
	arg = request.POST.get(button_label)
	command(arg)

@route('/')
def index():
	setting_group = 'general'
	return template('info_table', dict = pp_configs(setting_group), group = setting_group)

@route('/<setting_group>')
def get_table(setting_group):
	return template('info_table', dict = pp_configs(setting_group), group = setting_group)

run(host=HOST, port=PORT, debug=DEBUG, reloader=True)