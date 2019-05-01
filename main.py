#!/usr/bin/python3
# -*- coding: utf-8 *-*
from PIL import Image
import qrcode
import subprocess
print("Clearing QR payloads dir..")
try:
    cmd = subprocess.check_output(['rm', 'genqr/*'],stderr=subprocess.STDOUT)
    print(output)
except:
    print("Path already cleared or deleted...")
    pass
payloads = open("payloads.txt").readlines()
i = 0
while i < len(payloads):
    payloads[i] = payloads[i].strip()
    i+=1
i = 0
while i < len(payloads):
    img = qrcode.make(payloads[i])
    img.save("genqr/payload-{}.png".format(i))
    i+=1
print("Generated {} payloads!".format(len(payloads)))
print("Opening last generated payload...")
Image.open("genqr/payload-{}.png".format(i-1)).show()
print("Thanks for using QRGen, made by H0nus..")