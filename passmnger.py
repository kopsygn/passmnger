
#################################使い方################################################
usage = "pswdmngrにオプションの引数は不要です。その代わり名前で機能を指定します\n"
usage = "\n"
usage+= "pswdmngr.get     パスワードをクリップボードにコピーします。\n"
usage+= "pswdmngr.add     管理するアカウントを追加する\n"
usage+= "pswdmngr.del     アカウントを削除する\n"
usage+= "pswdmngr.list    アカウント一覧を表示する。\n"
usage+= "pawdmngr.cmps     マスターパスワードの変更する\n"
usage+= "pawdmngr.help    ヘルプ表示\n"
#######################################################################################


import getpass
import pyperclip
import sys
import hashlib
from Crypto.Cipher import AES


#定数#
#認証用のマスターパスワードがハッシュ化されたファイル
MASTERPASSWORD_FILEPASS = "./hashedfile.dat"

#暗号化されたアカウントデータのファイル
ACCOUNT_FILEPASS = "./accountfile.dat"


#関数#
#マスターパスワードをキーとしてアカウントファイルを暗号化する
def encryption(password,data):

    key = hashlib.md5(password).hexdigest()
    crypto = AES.new(key)
    crypted_data = crypto.encrypt(data)

    return crypted_data

#マスターパスワードをキーとしてアカウントファイルを復号化する
def decryption(password,crypted_data):

    key = hashlib.md5(password).hexdigest()
    crypto = AES.new(key)
    decrypted_data = crypto.decrypt(crypted_data)

    return decrypted_data

#認証用のマスターパスワードが正しいものかを判定するプログラム
#認証が出来なければプログラムを強制終了する。
def certification(password,hashedpass):

    if hashlib.sha512(password).hexdigest() != hashedpass:
        print("***faild password***")
        exit()
    else:
        print("***successfull***\n")

#アカウントファイルをディクショナリに落とす
def loaddata():

    accntfile = open("accountfile.dat")
    
    dicto = {"gmail":"nicemailpass"}
    return dicto

#パスワードの出力、今回はクリップボードにコピーする
def outputdata(password):

    pyperclip.copy(password)
    print("copy on clipboard")

    
#メインストリーム シンボリックリンクを使用して実行コマンド名で機能を判断して実行#
#パスワード出力メイン機能
if sys.argv[0] == "pswdmngr.get":
    certification(getpass.getpass("plz password > "))
    
    accountlist = loaddata()
    
    #引数にアカウント名を渡してもOK

    if sys.argv != 0:
        account = raw_input("plz accountdata > ")
    else:
        account = sys.arg[1]
        
    if(accountlist.get(account) is not None):
        outputdata(accountlist[account])
    else:
        print("sorry;_; '" +  account + "' is Not Found")

#管理アカウントの追加
elif sys.argv[0] == "pswdmngr.add":

#管理アカウントの削除
elif sys.argv[0] == "pswdmngr.del":

#管理しているアカウントをリスト表示
elif sys.argv[0] == "pswdmngr.list":

#マスターパスワードの変更
elif sys.argv[0] == "pswdmngt.cmps":

#ヘルプ・使い方表示
else:
    print usage
    
