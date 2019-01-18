def count_anagrams(strings):
    "Return the number of pairs of anagrams in a tuple of strings"
    total=0
    big_d=dict()
    letter_d=dict()
    for word in strings:
        if word not in big_d:
            big_d[word]=list(0 for i in range(26))
            for letter in word:
                big_d[word][ord(letter)-97]+=1
            v=tuple(big_d[word])
            if v not in letter_d:
                letter_d[v]=1
            else:
                letter_d[v]+=1
    total=sum(letter_d[x]*(letter_d[x]-1)/2 for x in letter_d)
    return total
