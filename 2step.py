# import pyotp

# totp = pyotp.TOTP('base32secret3232') # サーバー側であらかじめ指定する一意の値
# totp.now() # => '492039'                # nowメソッドで値の確認


# totp.verify('492039')                        # => True

# # import pyotp

# # hotp = pyotp.HOTP('base32secret3232')
# # hotp.at(0) # => '260182'
# # hotp.at(1) # => '055283'
# # hotp.at(1401) # => '316439'

# # # 値が正しいかどうかを確認
# # hotp.verify('316439', 1401) # => True
# # hotp.verify('316439', 1402) # => False



# # import pyotp
# # pyotp.random_base32()

import qrcode
import pyotp
import time

# ユーザーに渡す乱数を作成
random_base32 = pyotp.random_base32()
# uriを作成
uri = pyotp.totp.TOTP(random_base32).provisioning_uri(name="marsquai@google.com",issuer_name="サンプルアプリ")
# QRコードを作成
img = qrcode.make(uri)
# print(img)
img.save('qr_code.png')
img.show()


# 1000秒間OneTimePasswordを表示
totp = pyotp.TOTP(random_base32)
for i in range(1000):
    print(totp.now())
    time.sleep(1)