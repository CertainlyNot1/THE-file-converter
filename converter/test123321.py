from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from werkzeug.utils import secure_filename
from moviepy.video.io.VideoFileClip import VideoFileClip

from pdf2docx import Converter
from PIL import Image

import fitz
from docx import Document

from pptx import Presentation
from fpdf import FPDF
from bs4 import BeautifulSoup
import requests




def goldenLeBonBonClatt22():
    leUrl = 'https://www.xe.com/currency/'
    LeResponse = requests.get(leUrl)
    LeSoup = BeautifulSoup(LeResponse.text, 'html.parser')
    LeCurrencies = []
    for LeI in LeSoup.find_all('span',class_='currencyCode'):
        LeCurrencyCode = LeI.get_text(strip = True).replace('-','')
        LeCurrencies.append(LeCurrencyCode)
    return LeCurrencies

# print(goldenLeBonBonClatt22())

def get_rich(in_currency, out_currency):
    url = f"https://www.google.com/finance/quote/{in_currency}-{out_currency}?sa=X&ved=2ahUKEwiwpMTwnoyJAxVIQ_EDHYzuEU0QmY0JegQIARAs"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency = soup.find("div", class_="YMlKec fxKbKc").get_text()
    return float(currency)

def get_ratedd():
    currencies = ["UAH","TRY","CAD"]
    rates = {}
    for currency in currencies:
        try:
            
            rates[currency] = get_rich('USD',currency)
        except Exception as e:
            rates[currency] = 'N/A'

    return rates

print(get_ratedd())