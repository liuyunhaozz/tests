import os
import filecmp

modelm = os.listdir('exp11/labels')
modelx = os.listdir('exp12/labels')
modell = os.listdir('exp13/labels')

cout = 0
for file in modelm:
    if not filecmp.cmp('exp11/labels/' + file, 'exp12/labels/' + file):
        print(f'file{file} is not even!')
        cout += 1
print(cout)


