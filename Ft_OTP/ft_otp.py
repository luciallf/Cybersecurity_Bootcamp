# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/02 11:37:28 by lucilope          #+#    #+#              #
#    Updated: 2023/05/10 14:39:03 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pyotp
import random
import argparse
import hmac
import hashlib
import binascii
import os
import base64
import time
import struct
from cryptography.fernet import Fernet


def arguments():

    analizador = argparse.ArgumentParser()    
    
    analizador.add_argument('-g', dest ='hex', help="el programa recibirá un clave hexadecimal de 64 caracteres y la guardarña en un archivo ft_otp-key") 
    analizador.add_argument('-k', nargs = '*',  dest = 'key', help= "el programa generará una contraseña temporal y la mostrará en la salida estándar ") 
    args = analizador.parse_args()
    return args 


def read_files_hex():
    with open ("key.hex", "r") as file:
        hex = file.read()    
        return (hex)


#un programa que registre la clave hexadecimal 
def key_hex(hex):
    if len(hex) >= 64 and all(c in '0123456789abcdefABCDEF' for c in hex):
        pass
    else:
        print ("Error, la clave no es hexadecimal") 
        exit() 


#funcion que cree la clave que encripte
def encrypt_key(hex_key):
    key = binascii.unhexlify(hex_key)
    cipher_key = Fernet.generate_key()
    f = Fernet(cipher_key)
    token = f.encrypt(key)
    with open('master.key', 'wb') as file:
        file.write(cipher_key)
    with open('ft_otp.key', 'wb') as file:
        file.write(token)
    return token

#FUNCION K

#funcion para desencriptar la clave 

def descrypt():
    with open("master.key", "rb") as file:
        lectura = file.read()
    with open("ft_otp.key", "rb") as file:
        lectotp = file.read()
        f = Fernet(lectura)
        token_decrypt = f.decrypt(lectotp)
        token_encode = base64.b32encode(token_decrypt)
        token = token_encode.decode('utf-8')        
        return token

#funcion para generar el hotp con el hmac

def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

def get_totp_token(secret):
    x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
    while len(x)!=6:
        x+='0'
    return x

def pytopt(token):
    topt = pyotp.TOTP(token)
    print("Current OTP:", topt.now())

if __name__ == "__main__":
  
    args = arguments()
    gen = args.hex
    key = args.key
    if gen:
        hex = read_files_hex()
        key_hex(hex)
        encrypt_key(hex)
        print("Key was successfully saved in ft_otp.key.")
        exit()
    if (key[0] == "ft_otp.key"):
        encr = descrypt()
        print(get_totp_token(encr))
        token = descrypt()
        pytopt(token)
    else:
        print("ERROR")




        

    
        

