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
    """
    Esta función define y analiza los argumentos de línea de comandos.
    """
    analizador = argparse.ArgumentParser()
    analizador.add_argument('-g', dest='hex', help="El programa recibirá una clave hexadecimal de 64 caracteres y la guardará en un archivo ft_otp.key")
    analizador.add_argument('-k', nargs='*', dest='key', help="El programa generará una contraseña temporal y la mostrará en la salida estándar")
    args = analizador.parse_args()
    return args

def read_files_hex():
    """
    Esta función lee el contenido del archivo "key.hex".
    """
    with open("key.hex", "r") as file:
        hex = file.read()
        return hex

def key_hex(hex):
    """
    Esta función verifica si la clave es hexadecimal.
    """
    if len(hex) >= 64 and all(c in '0123456789abcdefABCDEF' for c in hex):
        pass
    else:
        print("Error, la clave no es hexadecimal")
        exit()

def encrypt_key(hex_key):
    """
    Esta función encripta la clave hexadecimal y la guarda en los archivos "master.key" y "ft_otp.key".
    """
    key = binascii.unhexlify(hex_key)
    cipher_key = Fernet.generate_key()
    f = Fernet(cipher_key)
    token = f.encrypt(key)
    with open('master.key', 'wb') as file:
        file.write(cipher_key)
    with open('ft_otp.key', 'wb') as file:
        file.write(token)
    return token

def descrypt():
    """
    Esta función desencripta la clave guardada en los archivos "master.key" y "ft_otp.key".
    """
    with open("master.key", "rb") as file:
        lectura = file.read()
    with open("ft_otp.key", "rb") as file:
        lectotp = file.read()
        f = Fernet(lectura)
        token_decrypt = f.decrypt(lectotp)
        token_encode = base64.b32encode(token_decrypt)
        token = token_encode.decode('utf-8')
        return token

def get_hotp_token(secret, intervals_no):
    """
    Esta función genera un token HOTP usando HMAC.
    """
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

def get_totp_token(secret):
    """
    Esta función genera un token TOTP (basado en el tiempo) usando la función get_hotp_token.
    """
    x = str(get_hotp_token(secret, intervals_no=int(time.time()) // 30))
    while len(x) != 6:
        x += '0'
    return x

def pytopt(token):
    """
    Esta función utiliza la biblioteca pyotp para generar un OTP.
    """
    totp = pyotp.TOTP(token)
    print("Current OTP:", totp.now())

if __name__ == "__main__":
    args = arguments()
    gen = args.hex
    key = args.key
   
