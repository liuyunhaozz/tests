import filecmp 

file_1 = 'testBf.csv'
file_2 = 'testB.csv'
file_3 = 'answerB.csv'

print(filecmp.cmp(file_2,file_3)) 