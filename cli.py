import sys
from Num2EnglishText import Num2EnglishText
num2EnglishText = Num2EnglishText()
print('Type number values and hit return. Will print English language version of that number');
print('All non number values will be ignored')
print('Type both the control and C keys to exit');
for line in sys.stdin:
    print(num2EnglishText.process(line.rstrip()))

