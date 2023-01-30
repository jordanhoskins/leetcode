symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

merges = {
    "DCCCC": "CM", # 900
    "CCCC": "CD", # 400
    "LXXXX": "XC",# 90
    "XXXX": "XL", # 40
    "VIIII": "IX",# 9
    "IIII": "IV", # 4
}

def merge_symbols(roman_numeral):
    for merge in merges:
        if roman_numeral.endswith(merge):
            return roman_numeral.replace(merge, merges[merge])
    return roman_numeral

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        # subtract from num with largest available symbol, 
        # keep track of symbols used
        while num:
            available_symbols = [
                (sym, numeral) 
                for sym, numeral in symbols.items()
                if numeral <= num
            ]
            largest_sym_numeral = available_symbols[-1]
            roman += largest_sym_numeral[0]
            roman = merge_symbols(roman)
            num -= largest_sym_numeral[1]

        return roman
