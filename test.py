#!/usr/bin/env python

import urllib, urllib2
import cookielib
import sys
import os
import threading
import time

with open("pass.txt", r) as fi

         id = [l.strip() for l in fi]
 ​        ​fi​ ​=​ ​f​.​read​().​splitlines​() 

 ​for​ ​id ​in​ ​fi​: 
 ​        ​t​ ​=​ ​threading​.​Thread​(​​args​=​(​id​,​fi​)
 ​        ​t​.​start​() 
 ​        ​threads​.​append​(​t​) 
 ​        ​time​.​sleep​(​0.5​)
