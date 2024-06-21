deck = {}
i = 0
for j in range(4):
    for k in range(1, 14):
        deck[i] = (j, k) #花色、點數
        i += 1

def point(l):
    p = 0
    l.sort()
    
    c = 0
    if len(l) <= 4:
        for i in range(len(l)):
            if l[i] == 1:#計算A的數量
                c += 1
    else :
        for i in range(4):
            if l[i] == 1:
                c += 1

    for i in range(len(l)):
        if l[i] in [11, 12, 13]:
            l[i] = 10
        elif l[i] == 1:
            l[i] = 11
        p += l[i]

    while p > 21 and c > 0:#如果超過，則將一張A改為1
        p -= 10
        c -= 1

    return p

import random
out = []
player = random.sample([i for i in range(52)], 2)
out.extend(player)
player_c = [deck[i][1]for i in player]#玩家的牌
player_p = point(player_c)#玩家點數
dealer = random.sample([i for i in range(52) if i not in out], 2)
out.extend(dealer)
dealer_c = [deck[i][1]for i in dealer]
dealer_p = point(dealer_c)
print(player_p)
while True:
    call = int(input("call"))
    if call == 1:
        player.extend(random.sample([i for i in range(52) if i not in out], 1))
        player_c = [deck[i][1]for i in player]
        player_p = point(player_c)
        print(f"You drew: {deck[player[-1]][1]}")
        if player_p <= 21:
            print(player_p)
            continue
        else :
            print(player_p)
            print("bust")
            pass
                        
    print('Dealer~')
    if dealer_p <= 17:
        dealer.extend(random.sample([i for i in range(52) if i not in out], 1))
        dealer_c = [deck[i][1]for i in dealer]
        dealer_p = point(dealer_c)
    print(dealer_p)
    
    if player_p <= 21 and dealer_p <= 21:
        if player_p > dealer_p:
            print('Player win')
        elif dealer_p > player_p:
            print('Dealer win')
        else:
            print('draw')
    elif player_p >21 and dealer_p <= 21:
        print('Dealer win')
    elif player_p <=21 and dealer_p > 21:
        print('Player win')
    else:
        print('draw')
    again = input('Play again y/n : ')
    if again == 'y':
        out = []
        player = random.sample([i for i in range(52)], 2)
        out.extend(player)
        player_c = [deck[i][1]for i in player]#玩家的牌
        player_p = point(player_c)#玩家點數
        dealer = random.sample([i for i in range(52) if i not in out], 2)
        out.extend(dealer)
        dealer_c = [deck[i][1]for i in dealer]
        dealer_p = point(dealer_c)
        print(player_p)
        continue
    else:
        break

        
            


