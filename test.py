#!/usr/bin/env python

import urllib, urllib2
import cookielib
import sys
import os
import threading
import time

with open('pass.txt') as f:
    lines = f.readlines()
print(lines)
