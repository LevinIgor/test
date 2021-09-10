class RomanNumerals:
    
    def to_roman(val):
        vall = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  val > 0:
            for _ in range(val // vall[i]):
                roman_num += syb[i]
                val -= vall[i]
            i += 1
        return roman_num
        

    def from_roman(roman_num):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(roman_num)):
            if i > 0 and rom_val[roman_num[i]] > rom_val[roman_num[i - 1]]:
                int_val += rom_val[roman_num[i]] - 2 * rom_val[roman_num[i - 1]]
            else:
                int_val += rom_val[roman_num[i]]
        return int_val


print (RomanNumerals.to_roman(1023))
print (RomanNumerals.from_roman("X"))
        
    
    
        

    
