
# -*- coding: cp1251 -*-

# -*- coding: utf-8 -*-
from unicodedata import normalize
import random

def checker1(num):
    if num % 3 == 0: 
        print("����� ������� �� 3")
    else: 
        print("����� �� ������� �� 3")

def delitel(num):    
    if flags == True:
        num = int(num)
        x = num / 100
        x = str(x)
        final = x + " �����, ������� ����������"
        print (final)
    else:
        print("��� �� �����, � ����� �����")
        
    if num != 0 and flags == True:
        num = int(num)
        x = num / 100
        x = str(x)
        final = x + " �����, ������� ����������"
        print (final)
    else:
        print("0 ���� ������")

def magicChecker(dateCheck):
   day, month, year = map(int, dateCheck.split("."))
   
   if day * month == (year % 100):
       print("���� ����������")
   else:
       print("���� �� ����������")
    
def bileter(bilet):
    x = len(bilet)
    y = x / 2
    y = int(y)
    firPart = bilet[0:y]
    secPart = bilet[y: x]
    sumFirPart = sum(int(char) for char in firPart)
    sumSecPart = sum(int(char) for char in secPart)
    if sumFirPart == sumSecPart:
        print("����� ����������")
    else:
        print("����� �� ����������")

while True:
  
    checker = False
    primaryChoice = input("����� ������� ��� �������� : \n1)\n2)\n3)\n4)\n5) - �����\n����� : ")
    if [num for num in primaryChoice if num not in ".,/*-+1234567890"]: checker = True
    if checker == True:
        print("��� ������")
        break
    primaryChoice = int(primaryChoice)
    
    if primaryChoice == 1:
        print("������� ����� ��� �������� ��� ������� �� 3 : ")
        num = input()
        num = int(num)
        checker1(num)
        
    if primaryChoice == 2:
        print("������� �����, ������� ����� ������ �����")
        num = input("������ ������� 0 ��� �� ����� : ")
        num = str(num)
        for char in num:
            if char < '0' or char > '9':
                flags = False
            else:
                flags = True 
        delitel(num)
        
    if primaryChoice == 3:
        flags = False
        dateCheck = input("������� ���� �� ������� ��.��.���� ")
        magicChecker(dateCheck)
    
    if primaryChoice == 4:
        bilet = input("������� ����� ������ ")
        x = len(bilet)
        if x % 2 != 0:
            print("����� ����� ������ ������ ���� ������")
        else:
            bileter(bilet)
    if primaryChoice == 5:
        break