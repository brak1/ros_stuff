#!/usr/bin/env python

import csv
import random
import numpy as np
import matplotlib.pyplot as plt
from _ast import Num
from math import sqrt
from mpl_toolkits.mplot3d import axes3d
from scipy.signal import savgol_filter


ifile  = open('sample.csv', "rb")
reader = csv.reader(ifile)
results = []
rownum = 0
