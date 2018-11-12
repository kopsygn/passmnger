import getpass
import pyperclip
import sys




def certification(password):
    if password != "testpass":
        print("***faild password***")
        exit()
    else:
        print("***successfull***\n")

def loaddata():
    accntfile = open("accountfile.dat")
    dicto = {"gmail":"nicemailpass"}
    return dicto


def outputdata(password):
    pyperclip.copy(password)
    print("copy on clipboard")



    
certification(getpass.getpass("plz password > "))

accountlist = loaddata()

if sys.argv != 0:
    account = raw_input("plz accountdata > ")
else:
    account = sys.arg[1]


if(accountlist.get(account) is not None):
    outputdata(accountlist[account])
else:
    print("sorry;_; '" +  account + "' is Not Found")

