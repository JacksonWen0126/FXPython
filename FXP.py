rqe = int(input('Do you need help? 1.yes 2.no\n'))
Balance = 100
if rqe == 1:
    wyn = int(input('1.Deposit/withdraw 2.Exchanged 3.Info\n'))
    if wyn == 1:
        num = int(input('How Much? Negative amount for withdraw\n'))
        Balance +=num
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