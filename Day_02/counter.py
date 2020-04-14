from collections import Counter

num_lst = [1, 1, 2, 2, 1, 1, 2, 2, 2, 3, 4, 4, 3, 3, 2, 4, 6, 5, 4, 3, 7, 2, 5, 5, 6, 8, 7, 6, 5, 3]
kk = Counter(num_lst)
print(kk)

letter_lst='wdwdwdwad wdawawdadawa awdawdAAAA'
print(Counter(letter_lst))

words='word counter word counter Padma Padma counter 2019 word counter'
wrd=words.split()
kk=Counter(wrd)
print(kk)