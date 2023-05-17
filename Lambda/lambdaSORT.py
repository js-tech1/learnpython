dna = 'ACCGXXTAFHREXH'
sequances = dna.split('X')
sequances.sort(key=len, reverse=True)

print(sequances)
sequances = list(filter(lambda x: len(x)> 0,sequances))
print(sequances)

#split at x with the most numbers of alphabets
#reverse command reveerses the order