from digitalsignature import *

# 秘密鍵と公開鍵を作る。（パスワードはなくても良い）
password = "password"
sk, pk = generate_key(passphrase = password)

# メッセージに署名する（署名者が行う）
message = "password"
sig = sign(sk, message, passphrase = password)
# print(sig)

#　承認テスト（承認者が行う）
if verify(pk, sig, message):
    print("承認 OK")
else:
    print("承認 NG")

#　メッセージの書き換えに対するテスト
message="hogehoge"
# sig = sign(sk, message, passphrase = password)
# changed_message = "hogehoge"
if verify(pk, sig, message):#changed_message):
    print("書き換えテスト NG")
else:
    print("書き換えテスト OK") # 承認されなければOK
    # print(pk)
    # print(sig)
    # print(message)

# 間違った秘密鍵の署名に対するテスト
sk2, pk2 = generate_key(passphrase = password)
sig2 = sign(sk2, message, passphrase = password)
if verify(pk, sig2, message):
    print("不正署名テスト NG")
else:
    print("不正署名テスト OK") # 承認されなければOK