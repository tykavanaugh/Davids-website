#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flask project for David's website'
Created on Sun Aug  9 14:55:03 2020

@author: BlackBox
"""
#https://imgur.com/a/ho8O23f decking photo
from flask import Flask,redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
