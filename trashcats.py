#!/usr/bin/python3

import os
import random
import subprocess

i2cbus = str(1) #strval of the i2c bus, not the address
i2caddress = '0x3c' #i2c device address, i2cdetect to figure it out


def runi2cset(iter, bang1, bang2):
        global i2cbus, i2caddress
        for i in range(1,iter):
                proc = subprocess.Popen(['i2cset', '-y', i2cbus, i2caddress, bang1, bang2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = proc.communicate()
                        #print(stdout)
                        #print(stderr)
def rescursor():
        runi2cset(2, '0x00', '0x21') # set screen width
        runi2cset(2, '0x00', '0x00') # screen width start
        runi2cset(2, '0x00', '0x7F') # screen width end (128)
        runi2cset(2, '0x00', '0x22') # set screen height
        runi2cset(2, '0x00', '0x00') # screen height start line
        runi2cset(2, '0x00', '0x07') # screen height end line (7 for 128x64)

def initscreen():
        runi2cset(2, '0x00', '0xAF')
        runi2cset(2, '0x00', '0xA8')
        runi2cset(2, '0x00', '0x3F')
        runi2cset(2, '0x00', '0xD3')
        runi2cset(2, '0x00', '0x00')
        runi2cset(2, '0x00', '0x40')
        runi2cset(2, '0x00', '0xA1')
        runi2cset(2, '0x00', '0xC8')
        runi2cset(2, '0x00', '0xDA')
        runi2cset(2, '0x00', '0x22') # 0x22 sets cursor to 8pixel, 0x32 for 4 pixel but then the 5x5 will overflow to the top...
        runi2cset(2, '0x00', '0xA4')
        runi2cset(2, '0x00', '0xA6')
        runi2cset(2, '0x00', '0xD5')
        runi2cset(2, '0x00', '0x40')
        runi2cset(2, '0x00', '0x8D')
        runi2cset(2, '0x00', '0x14')
        runi2cset(2, '0x00', '0x20')
        runi2cset(2, '0x00', '0x20')
        rescursor()


def fillscreen():
        runi2cset(1025, '0x40', '0xFF') #iter + 1

def clearscreen():
        runi2cset(1025, '0x40', '0x0') #iter + 1

def weirdtests():
        temparray = []
        for i in range(1,128):
                temparray.append(i)
        for i in range(1, len(temparray)):
                thisone = random.choice(temparray)
                runi2cset(2, '0x40', str(hex(thisone)))

def fontsupply(inputstring):
        systemfont = [
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['00','00','00','00','00','00'],
['5c','00','00','00','00','00'],
['06','00','06','00','00','00'],
['28','7c','28','7c','28','00'],
['5c','54','fe','54','74','00'],
['44','20','10','08','44','00'],
['28','54','54','20','50','00'],
['06','00','00','00','00','00'],
['38','44','00','00','00','00'],
['44','38','00','00','00','00'],
['02','07','02','00','00','00'],
['10','10','7c','10','10','00'],
['c0','00','00','00','00','00'],
['10','10','10','10','10','00'],
['40','00','00','00','00','00'],
['60','10','0c','00','00','00'],
['7c','64','54','4c','7c','00'],
['48','7c','40','00','00','00'],
['64','54','54','54','48','00'],
['44','54','54','54','6c','00'],
['3c','20','70','20','20','00'],
['5c','54','54','54','24','00'],
['7c','54','54','54','74','00'],
['04','04','64','14','0c','00'],
['7c','54','54','54','7c','00'],
['5c','54','54','54','7c','00'],
['44','00','00','00','00','00'],
['c4','00','00','00','00','00'],
['10','28','44','00','00','00'],
['28','28','28','28','28','00'],
['44','28','10','00','00','00'],
['08','04','54','08','00','00'],
['7c','44','54','54','5c','00'],
['7c','24','24','24','7c','00'],
['7c','54','54','54','6c','00'],
['7c','44','44','44','44','00'],
['7c','44','44','44','38','00'],
['7c','54','54','54','44','00'],
['7c','14','14','14','04','00'],
['7c','44','44','54','74','00'],
['7c','10','10','10','7c','00'],
['44','44','7c','44','44','00'],
['60','40','40','44','7c','00'],
['7c','10','10','28','44','00'],
['7c','40','40','40','40','00'],
['7c','08','10','08','7c','00'],
['7c','08','10','20','7c','00'],
['38','44','44','44','38','00'],
['7c','14','14','14','08','00'],
['3c','24','64','24','3c','00'],
['7c','14','14','14','68','00'],
['5c','54','54','54','74','00'],
['04','04','7c','04','04','00'],
['7c','40','40','40','7c','00'],
['0c','30','40','30','0c','00'],
['3c','40','30','40','3c','00'],
['44','28','10','28','44','00'],
['0c','10','60','10','0c','00'],
['44','64','54','4c','44','00'],
['7c','44','00','00','00','00'],
['0c','10','60','00','00','00'],
['44','7c','00','00','00','00'],
['00','01','00','01','00','00'],
['40','40','40','40','40','40'],
['00','01','00','00','00','00'],
['7c','24','24','24','7c','00'],
['7c','54','54','54','6c','00'],
['7c','44','44','44','44','00'],
['7c','44','44','44','38','00'],
['7c','54','54','54','44','00'],
['7c','14','14','14','04','00'],
['7c','44','44','54','74','00'],
['7c','10','10','10','7c','00'],
['44','44','7c','44','44','00'],
['60','40','40','44','7c','00'],
['7c','10','10','28','44','00'],
['7c','40','40','40','40','00'],
['7c','08','10','08','7c','00'],
['7c','08','10','20','7c','00'],
['38','44','44','44','38','00'],
['7c','14','14','14','08','00'],
['3c','24','64','24','3c','00'],
['7c','14','14','14','68','00'],
['5c','54','54','54','74','00'],
['04','04','7c','04','04','00'],
['7c','40','40','40','7c','00'],
['0c','30','40','30','0c','00'],
['3c','40','30','40','3c','00'],
['44','28','10','28','44','00'],
['0c','10','60','10','0c','00'],
['44','64','54','4c','44','00'],
['10','7c','44','00','00','00'],
['6c','00','00','00','00','00'],
['44','7c','10','00','00','00'],
['02','01','02','01','00','00'],
['00','00','00','00','00','00']]
        print(len(systemfont))
        ordarray = []
        outarray = []
        stringlen = len(inputstring)
        for char in range(0, stringlen):
                ordarray.append(ord(inputstring[char]))
        print(ordarray)
        for charnum in ordarray:
                for i in range(0, len(systemfont[charnum])):
                        thischar = '0x' + str(systemfont[charnum][i])
                        outarray.append(thischar)
        return outarray


def writetext(text):
        for i in fontsupply(text):
                runi2cset(2, "0x40", i)

initscreen()
fillscreen()
rescursor()
clearscreen()
rescursor()
writetext("Yay this display            works!          bitBANGin!@#$")
