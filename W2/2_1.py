"""Chapter : 2 - item : 1 - roman number
 ส่งมาแล้ว 2 ครั้ง
จงเขียนฟังชั่นแปลง เลขอารบิกเป็นเลขโรมัน และ เลขโรมันเป็นอารบิกโดยที่

M=1000    CM=900    D=500    CD=400,

C=100    XC=90    L=50    XL=40,

X=10    IX=9    V=5    IV=4    I=1

เช่น 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I

(https://roman-numerals.info/)



class translator:

    def deciToRoman(self, num):

        ### Enter Your Code Here ###

    def romanToDeci(self, s):

        ### Enter Your Code Here ###

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))"""
class translator:

    def deciToRoman(self, num):
        res = ""
        table = [
      (1000, "M"),
      (900, "CM"),
      (500, "D"),
      (400, "CD"),
      (100, "C"),
      (90, "XC"),
      (50, "L"),
      (40, "XL"),
      (10, "X"),
      (9, "IX"),
      (5, "V"),
      (4, "IV"),
      (1, "I"),
       ] 
        for cap, roman in table:
           d, m = divmod(num, cap)
           res += roman * d
           num = m

        return res

    def romanToDeci(self, s):
        s = s.replace("XC",'h').replace("XL",'f').replace("IX",'n').replace("IX",'n').replace("CM",'t').replace("CD",'F').replace("IV",'4')
        return s.count('I')+s.count('V')*5 +s.count('n')*9 +s.count('f')*40 +s.count('h')*90 +s.count('X')*10 +s.count('F')*400+ s.count('t')*900 +s.count('M')*1000 +s.count('C')*100 +s.count('L')*50 +s.count('D')*500+s.count('4')*4

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))