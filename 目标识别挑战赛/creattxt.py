import os

path = os.listdir('image')


for name in path:
    
    with open('txt/' + name[:-4] + '.txt', 'w') as f:
        f.write('START\n')
        f.write('END\n')
        