"""Chapter : 2 - item : 2 - Spherical
 ส่งมาแล้ว 2 ครั้ง
สร้าง class Spherical โดยต้อง

มี function [changeR , findVolume , findArea]

มี ตัวแปร radius



*สามารถใช้ from math import pi  หรือ math.pi  ได้*

class Spherical:

    def __init__(self,r):

        ### Enter Your Code Here ###

    def changeR(self,Radius):

        ### Enter Your Code Here ###

    def findVolume(self):

        ### Enter Your Code Here ###

    def findArea(self):

        ### Enter Your Code Here ###

    def __str__(self):

        ### Enter Your Code Here ###

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)"""
import math

class Spherical:

    def __init__(self,r):

        self.radius = r

    def changeR(self,Radius):

        self.radius = Radius

    def findVolume(self):
        return math.pi * self.radius * self.radius * self.radius * (4/3)

    def findArea(self):

        return math.pi * self.radius * self.radius * 4

    def __str__(self):

        r = "Radius =" + str(int(self.radius))
        r += " Volumn = " + str(self.findVolume())
        r += " Area = " + str(self.findArea())
        return r


r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)