
# -*- coding: cp1251 -*-

# -*- coding: utf-8 -*-
from unicodedata import normalize
import random

def checker1(num):
    if num % 3 == 0: 
        print("Число делится на 3")
    else: 
        print("Число не делится на 3")

def delitel(num):    
    if flags == True:
        num = int(num)
        x = num / 100
        x = str(x)
        final = x + " Число, которое получилось"
        print (final)
    else:
        print("Это не число, а нужно число")
        
    if num != 0 and flags == True:
        num = int(num)
        x = num / 100
        x = str(x)
        final = x + " Число, которое получилось"
        print (final)
    else:
        print("0 тоже нельзя")

def magicChecker(dateCheck):
   day, month, year = map(int, dateCheck.split("."))
   
   if day * month == (year % 100):
       print("Дата магическая")
   else:
       print("дата не магическая")
    
def bileter(bilet):
    x = len(bilet)
    y = x / 2
    y = int(y)
    firPart = bilet[0:y]
    secPart = bilet[y: x]
    sumFirPart = sum(int(char) for char in firPart)
    sumSecPart = sum(int(char) for char in secPart)
    if sumFirPart == sumSecPart:
        print("Билет счастливый")
    else:
        print("Билет не счастливый")

while True:
  
    checker = False
    primaryChoice = input("Выбор задания для проверки : \n1)\n2)\n3)\n4)\n5) - Выход\nВыбор : ")
    if [num for num in primaryChoice if num not in ".,/*-+1234567890"]: checker = True
    if checker == True:
        print("Так нельзя")
        break
    primaryChoice = int(primaryChoice)
    
    if primaryChoice == 1:
        print("Введите число для проверки для деления на 3 : ")
        num = input()
        num = int(num)
        checker1(num)
        
    if primaryChoice == 2:
        print("Введите число, которое будет делить сотню")
        num = input("Нельзя вводить 0 или не число : ")
        num = str(num)
        for char in num:
            if char < '0' or char > '9':
                flags = False
            else:
                flags = True 
        delitel(num)
        
    if primaryChoice == 3:
        flags = False
        dateCheck = input("Введите дату по правилу ДД.ММ.ГГГГ ")
        magicChecker(dateCheck)
    
    if primaryChoice == 4:
        bilet = input("Введите номер билета ")
        x = len(bilet)
        if x % 2 != 0:
            print("Число чисел всегда должно быть четным")
        else:
            bileter(bilet)
    if primaryChoice == 5:
        break