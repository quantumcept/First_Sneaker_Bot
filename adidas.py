#!/usr/bin/env python
from bs4 import BeautifulSoup as bs
import requests
import timeit
import time
from getconf import *
from sys import version_info
import bs4
import random
import webbrowser
import csv
import threading
import RandomHeader

# TODO: captcha -- selenium or selenium-requests?
py3 = version_info[0] > 2

if py3:
	Base_url = 'https://www.adidas.com'
	Product_Name = input('Enter Product Name: ')
	Product_Name = product_name.replace(' ', '-')
	Product_ID = input('Enter PID: ')
	Size = int(input('Enter Size Desired: '))
else:
	Base_url = 'https://www.adidas.com'
	Product_Name = raw_input('Enter Product Name: ')
	Product_Name = Product_Name.replace(' ', '-')
	Product_ID = raw_input('Enter PID: ')
	Size = int(raw_input('Enter Size Desired: '))


SizeCode = ((Size - 4) * 20) + 530 

print(Base_url, '/us/', Product_Name, '/', Product_ID, '.html', 'forceSelSize=', Product_ID, '_', SizeCode)