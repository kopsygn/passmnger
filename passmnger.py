#!/usr/bin/python
# coding: UTF-8

import getpass
import pyperclip
import sys
import hashlib
import data_file_ctrlr

#####################################使い方############################################
usage = "pswdmngrにオプションの引数は不要です。その代わり名前で機能を指定します\n"
usage+= "\n"
usage+= "pswdmngr.get     パスワードをクリップボードにコピーします。\n"
usage+= "pswdmngr.add     管理するアカウントを追加する\n"
usage+= "pswdmngr.del     アカウントを削除する\n"
usage+= "pswdmngr.list    アカウント一覧を表示する。\n"
usage+= "pawdmngr.cmps    マスターパスワードの変更する\n"
usage+= "pawdmngr.help    ヘルプ表示\n"
usage+= "管理したいアカウント名及びパスワードに、スペースは使わないでください"
#######################################################################################


#定数#
#認証用のマスターパスワードがハッシュ化されたファイル
MASTERPASSWORD_FILEPASS = "./hashedfile.dat"

#暗号化されたアカウントデータのファイル
ACCOUNT_FILEPASS = "./accountfile.dat"

#関数#
#マスターパスワード認証
def certification(password,filepass):

    hashed_data = open(filepass).read()
    
    if hashlib.sha512(password).hexdigest() != hashed_data:
        print("***faild password***")
        exit()
    else:
        print("***successfull***\n")

        
#パスワードの出力、今回はクリップボードにコピーする
def outputdata(password):

    pyperclip.copy(password)
    print("copy on clipboard")


    
#メインストリーム シンボリックリンクを使用して実行コマンド名で機能を判断して実行#
#パスワード出力メイン機能

hashed_master_password = open(MASTERPASSWORD_FILEPASS).read()
master_password = getpass.getpass("plz password > ")
certification(master_password)

accounts = loaddata(ACCOUNT_FILEPAS, master_password)

linkname = sys.argv[0].split("/")[-1]

#管理しているパスワードをクリップボードへ出力
if linkname == "pswdmngr.get":
    accountlist = loaddata(ACCOUNT_FILEPAS)
    
    #引数にアカウント名を渡してもOK

    if sys.argv != 0:
        account = raw_input("plz accountdata > ")
    else:
        account = sys.arg[1]



        if(accountlist.get(account) is not None):
        outputdata(accountlist[account])
    else:
        print("sorry;_; '" +  account + "' is Not Found")

#管理しているアカウントの追加
elif linkname == "pswdmngr.add":
    print "test"
    
#管理しているアカウントの削除
elif linkname == "pswdmngr.del":
    print "test"
    
#管理しているアカウントをリスト表示
elif linkname == "pswdmngr.list":
    for acnt in loaddata(sorted(ACCOUNT_FILEPAS).keys()):
        print acnt
    
#マスターパスワードの変更
elif linkname == "pswdmngt.cmps":
    newpass = getpass.getpass("plz new password > ")

    if newpass == getpass.getpass("one more type > "):
        encryption()
        file = open(MASTERPASSWORD_FILEPASS,w)
        file = hashlib.md5(password).hexdigest()#ファイルに書き込み
    else:
        print("no match password")
        exit();
    
#ヘルプ・使い方表示 .helpもここでキャッチする。
else:
    print usage

