################################################
# Given a value from 1 to 999,999,999
# return this number vlaue (or string of a numeric)
# in it's human readable format.
#
# Example:
#    print(Num2EnglishText().process(123))
#  returns
#    "one, hundred, twenty, three"
################################################

class Num2EnglishText:

    def process(self, aStr):
        return self.__SEPERATOR.join(self.__process(aStr))

    __SEPERATOR = ' '

    __DIGITS = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
                5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    __DIGITS_MAX_EX = 10
    __DIGITS_MIN = 1

    __TEENS = {10: 'ten', 11: 'eleven',
               12: 'twelve', 13: 'thirteen', 15: 'fifteen'}
    __TEENS_MAX_EX = 20
    __TEENS_MIN = __DIGITS_MAX_EX

    __TWENTIES = {2: 'twenty', 3: 'thirty',
                  4: 'forty', 5: 'fifty', 8: 'eighty'}
    __TWENTIES_MAX_EX = 100
    __TWENTIES_MIN = __TEENS_MAX_EX
    __TWENTIES_POSTFIX = 'ty'

    __HUNDREDS_MAX_EX = 1000
    __HUNDREDS_MIN = __TWENTIES_MAX_EX
    __HUNDREDS_POSTFIX = 'hundred'

    __THOUSANDS_MAX_EX = 1000000
    __THOUSANDS_MIN = __HUNDREDS_MAX_EX
    __THOUSANDS_POSTFIX = 'thousand'

    __MILLIONS_MAX_EX = 1000000000
    __MILLIONS_MIN = __THOUSANDS_MAX_EX
    __MILLIONS_POSTFIX = 'million'

    __PROCESS_MAX_EX = __MILLIONS_MAX_EX

    def __clean(self, numStr, min=1, max=__PROCESS_MAX_EX):
        try:
            if isinstance(numStr, str):
                # String any non number values from the string
                numStr = ''.join(filter(str.isdigit, numStr))
            elif isinstance(numStr, int):
                numStr = str(numStr)
            if not isinstance(numStr, str):
                return False
            result = int(numStr)
            if not min <= result < max:
                return [False, numStr]
            return [result, str(result)]
        except:
            return False

    def __digits(self, aStr):
        aNum, aStr = self.__clean(
            aStr, self.__DIGITS_MIN, self.__DIGITS_MAX_EX)
        if not bool(aNum):
            return []
        return [self.__DIGITS[aNum]]

    def __teens(self, aStr):
        aNum, aStr = self.__clean(aStr, self.__TEENS_MIN, self.__TEENS_MAX_EX)
        if not bool(aNum):
            return self.__process(aStr)
        bottom = aStr[1]
        if aNum in self.__TEENS:
            return [self.__TEENS[aNum]]
        return [self.__process(bottom).pop() + 'teen']

    def __twenties(self, aStr):
        aNum, aStr = self.__clean(
            aStr, self.__TWENTIES_MIN, self.__TWENTIES_MAX_EX)
        if not bool(aNum):
            return self.__process(aStr)
        top = int(aStr[0])
        bottom = aStr[1]
        result = []
        if top in self.__TWENTIES:
            result.append(self.__TWENTIES[top])
        else:
            result.append(self.__process(top).pop() + self.__TWENTIES_POSTFIX)
        tail = self.__process(bottom)
        result.extend(tail)
        return result

    def __hundreds(self, aStr):
        aNum, aStr = self.__clean(
            aStr, self.__HUNDREDS_MIN, self.__HUNDREDS_MAX_EX)
        if not bool(aNum):
            return self.__process(aStr)
        top = int(aStr[0])
        bottom = aStr[-2:]
        result = []
        result.extend(self.__process(top))
        result.append(self.__HUNDREDS_POSTFIX)
        tail = self.__twenties(bottom)
        result.extend(tail)
        return result

    # TODO: thuosands/millions and above might be made recursive.
    def __thousands(self, aStr):
        aNum, aStr = self.__clean(
            aStr, self.__THOUSANDS_MIN, self.__THOUSANDS_MAX_EX)
        if not bool(aNum):
            return self.__process(aStr)
        _len = len(aStr)
        if 6 == _len:
            top = int(aStr[0:3])
        elif 5 <= _len:
            top = int(aStr[0:2])
        elif 4 <= _len:
            top = int(aStr[0])
        bottom = aStr[-3:]
        result = []
        result.extend(self.__process(top))
        result.append(self.__THOUSANDS_POSTFIX)
        tail = self.__process(bottom)
        result.extend(tail)
        return result

    def __millions(self, aStr):
        aNum, aStr = self.__clean(
            aStr, self.__MILLIONS_MIN, self.__MILLIONS_MAX_EX)
        if not bool(aNum):
            return self.__process(aStr)
        _len = len(aStr)
        if 9 <= _len:
            top = int(aStr[0:3])
        elif 8 <= _len:
            top = int(aStr[0:2])
        elif 7 == _len:
            top = int(aStr[0])
        bottom = aStr[-6:]
        result = []
        result.extend(self.__process(top))
        result.append(self.__MILLIONS_POSTFIX)
        tail = self.__thousands(bottom)
        result.extend(tail)
        return result

    def __process(self, aStr):
        aNum, aStr = self.__clean(aStr)
        if not bool(aNum):
            return []
        if self.__DIGITS_MIN <= aNum < self.__DIGITS_MAX_EX:
            return self.__digits(aStr)
        elif self.__TEENS_MIN <= aNum < self.__TEENS_MAX_EX:
            return self.__teens(aStr)
        elif self.__TWENTIES_MIN <= aNum < self.__TWENTIES_MAX_EX:
            return self.__twenties(aStr)
        elif self.__HUNDREDS_MIN <= aNum < self.__HUNDREDS_MAX_EX:
            return self.__hundreds(aStr)
        elif self.__THOUSANDS_MIN <= aNum < self.__THOUSANDS_MAX_EX:
            return self.__thousands(aStr)
        elif self.__MILLIONS_MIN <= aNum < self.__MILLIONS_MAX_EX:
            return self.__millions(aStr)
