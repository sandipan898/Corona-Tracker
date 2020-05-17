import json
import requests
from pandas import DataFrame
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox
import numpy as np
from bs4 import BeautifulSoup
import textwrap as tw
import selenium 
from selenium import webdriver


frame_stat = None
frame_data = None
button_show = None
canvas1 = None
frame1 = None
root = None
info = None

def call_browser(arg):
    browser = webdriver.Chrome("")
    if arg == '1':
        browser.get("https://www.who.int/")

    if arg == '2':
        browser.get("https://sandipandas898.wixsite.com/sandipandas")

def get_data(url):
    response = requests.get(url)
    data = json.loads(response.content)
    return data

def get_chart(country):

    info = get_data("https://pomber.github.io/covid19/timeseries.json")
    with open("corona_timeseries.txt", "w") as f:
        f.write(info)
        f.close()

    with open("corona_timeseries.txt", "r") as f:
        info = eval(f.read())
        f.close()


