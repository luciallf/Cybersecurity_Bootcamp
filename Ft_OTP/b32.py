import base64

def encode_script_to_base32(file_name):
    with open("ft_otp.py", 'rb') as f:
        script_content = f.read()
    encoded_script = base64.b32encode(script_content)
    return encoded_script.decode('utf-8')