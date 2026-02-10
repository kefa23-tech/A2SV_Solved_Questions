class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
                1: "I",
                2: "II",
                3: "III",
                4: "IV",
                5: "V",
                6: "VI",
                7: "VII",
                8: "VIII",
                9: "IX",
                10: "X",
                20: "XX",
                30: "XXX",
                40: "XL",
                50: "L",
                60: "LX",
                70: "LXX",
                80: "LXXX",
                90: "XC",
                100: "C",
                200: "CC",
                300: "CCC",
                400: "CD",
                500: "D",
                600: "DC",
                700: "DCC",
                800: "DCCC",
                900: "CM",
                1000: "M",
                2000: "MM",
                3000: "MMM"
            }
        if num in romans:
            return romans[num]
        num = str(num)
        n = len(num)-1
        roman = ""
        
        for i in range(1,len(num)):
            a = num[:i]
            b = num[i:]
            n = a[i-1]
            if n == "0":
                continue
            zeros = "0"*len(b)
            roman+= romans[int(n+zeros)]
        if int(num[-1]) in romans:
            roman+=romans[int(num[-1])]
        return roman
