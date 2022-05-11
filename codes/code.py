from matplotlib import pyplot as plt
manufacturing_prob = {'A':0.25,'B':0.35,'C':0.40}
defective_prob = {'A':0.05,'B':0.04,'C':0.02}
X = ['A','B','C']
total_defective_prob = manufacturing_prob['A']*defective_prob['A']+manufacturing_prob['B']*defective_prob['B']+manufacturing_prob['C']*defective_prob['C']
is_defective_from = {'A': (manufacturing_prob['A']*defective_prob['A'])/total_defective_prob,'B':(manufacturing_prob['B']*defective_prob['B'])/total_defective_prob,'C':(manufacturing_prob['C']*defective_prob['C'])/total_defective_prob}
Y = [is_defective_from['A'],is_defective_from['B'],is_defective_from['C']]
plt.stem(X,Y)
plt.xlabel('Machine')
plt.ylabel('Probability that bolt is defective ')
plt.title('PMF graph')
plt.show()
print( 'Probability that bolt is from machine B given that it is defective : ',is_defective_from['B'] )
