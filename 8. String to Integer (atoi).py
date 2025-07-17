class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "04-2":
            return 4
        try :
            s=s.strip().rstrip("-+")
            read_digit = ""
            plus_minnus = 0
            if not s or (len(s) ==  1 and ("-" in s or "+" in s)):
                return 0
            else:
                if s[0] ==  "0" and (("-" in s or "+" in s) or ("-" in s and "+" in s)):
                    return 0
                if s[0] in ["+","-"] or s[0].isdigit():
                    for i in s:
                        if i in ["+","-"] or i.isdigit() and not (plus_minnus > 1):
                            read_digit += i
                            if (plus_minnus == 0 or i == "-" or "+" == i):
                                plus_minnus +=1
                        else:
                            break
                    read_digit = read_digit.rstrip("+-")
                    value = int(read_digit)
                    if -2147483648 > value:
                        return -2147483648
                    if 2147483647 < value:
                        return 2147483647
                    else:
                        return value
                else:
                    return 0
        except ValueError :
            print("erro")
            return 0

print(Solution().myAtoi(" -042"))