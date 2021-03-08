import random
def playing_card():
    x=[]
    suit =['\u2660','\u2665','\u2666','\u2663']
    rank = list('123456789')+['10']+list('JQK')
    for i in suit:
        for a in rank:
            x.append(a + i)
    return x

card =(playing_card())
print(len(card))
random.shuffle(card)
print(card)
p = random.sample(card,3)
print(p)