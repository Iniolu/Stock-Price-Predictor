from flask import Flask, render_template, request, jsonify
import yfinance as yf
import pandas as pd
import torch
import torch.nn as nn
import numpy as np
from sklearn.preprocessing import MinMaxScaler


app = Flask(__name__)




