from flask import Flask, render_template, request
import requests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
import os

app = Flask(__name__), static_folder="currency_chart_fixed/static")
API_KEY = 'fca_live_xa0BIncYUXOowI2zzWTs7xjCvAEB7QGdlUi7Of2o'
BASE_URL = 
