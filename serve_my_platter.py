#!/usr/bin/python


import os
os.chdir('/home/pi/pi_platter/')
from bottle import route, get, run, template, static_file
from talkpp import pp_configs

HOST = '0.0.0.0'
PORT = 8080

@get('/<filename:re:.*\.css>')
def stylesheets(filename):	
	return static_file(filename, root='static/css/')

@route('/')
def index():
	return template('info_table', dict = {'a':1}, group = 'fix me')

@route('/<setting_group>')
def get_table(setting_group):
	return template('info_table', dict = pp_configs(setting_group), group = setting_group)

run(host=HOST, port=PORT, debug=True, reloader=True)
