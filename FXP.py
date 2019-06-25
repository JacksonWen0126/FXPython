
def update1(Balance,num):
    f1=open('SecretFile.txt','r+')
    text = f1.read()
    B1=Balance
    n1=num
#cant replace the original and update in the file
    text = text.replace(B1,n1)
    print(text)
    f1.write(str(text))
    f1.close()
    return

def load1():
    f=open('SecretFile.txt','r')
    print('before readn'+str(f))
    f1 = f.read().split(',')
    Balance=f1[1]
    Balance = Balance.strip()
    #print(Balance)
    #print(str(f1))
    f.close()
    return Balance
    
Balance=float(load1())
rqe = int(input('Do you need help? 1.yes 2.no\n'))


if rqe == 1:
    wyn = int(input('1.Deposit/withdraw 2.Exchanged 3.Info\n'))
    if wyn == 1:
        num = int(input('How Much? Negative amount for withdraw\n'))
        temp=Balance
        Balance +=num
        print(Balance)
        update1(str(temp),str(Balance))
        print('Now balance is '+str(Balance))
    elif wyn ==2:
        exn=float(int(input('Exchange rate now is 1 Gold = 51.3RMB, enter the amount of Gold you want\n')))
        tt= exn*51.3
        print('System will exchange '+str(exn)+' Gold for '+str(tt)+" from your account" )
        Balance-=tt
        print('Now your balance is ' +str(Balance))
    else:
        
        print('There is nothing special and your balance '+str(Balance))
        
else:
    print('Have a good day and btw your balance is ' +str(Balance))