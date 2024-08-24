from Crypto.PublicKey import RSA #RSA信号
from Crypto.Signature import PKCS1_v1_5 #電子書籍のフォーマット
from Crypto.Hash import SHA256 #ハッシュ関数
from base64 import b64decode, b64encode #エンコード・・・変換,符号・記号・暗号化など デコード・・・復号化
import sys

def generate_key(keysize=2048, passphrase = None):
    new_key = RSA.generate(keysize)
    public_key = new_key.publickey().exportKey()
    secret_key = new_key.exportKey(passphrase = passphrase)
    return secret_key, public_key

def sign(secret_key, data, passphrase = None):
    try:
        rsakey = RSA.importKey(secret_key, passphrase = passphrase)
    except ValueError as e:
        print(e)
        sys.exit(1)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    digest.update(b64decode(data))
    sign = signer.sign(digest)
    return b64encode(sign)

def verify(pub_key, signature, data):
    rsakey = RSA.importKey(pub_key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    digest.update(b64decode(data))
    if signer.verify(digest, b64decode(signature)):
        return True
    else:
        return False
