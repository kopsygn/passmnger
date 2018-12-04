import hashlib
from Crypto.Cipher import AES


#ファイルパスとデータ(dict)を受け取ってファイルに書き込み
def save_data(filepass,filedata):
    #マスターパスワードをキーとしてアカウントファイルを暗号化する
    def encryption(password,data):
        
        key = hashlib.md5(password).hexdigest()
        crypto = AES.new(key)
        crypted_data = crypto.encrypt(data)
        
        return crypted_data
    return nothing


#アカウントファイルをディクショナリに落とす
def load_data(key,filepass):

    #マスターパスワードをキーとしてアカウントファイルを復号化する
    def decryption(password,crypted_data):

        key = hashlib.md5(password).hexdigest()
        crypto = AES.new(key)
        decrypted_data = crypto.decrypt(crypted_data)

        return decrypted_data

    
    account_list = open(filepass)
    dicto = dict(map(lambda l:l.split(" "), account_list.read().split("\n")))

    account_list.close()
    
    return dicto

