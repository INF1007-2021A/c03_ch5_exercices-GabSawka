#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import math 

def convert_to_absolute(number: float) -> float:
    #if number<0:
        #number *=-1
    return number *-1 if number<0 else number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names_list=[]
    for letter in prefixes:
        names_list.append(letter+suffixe)

    return names_list

def is_prime(nb:int)->bool:
    prime = True
    for i in range(2,math.ceil(nb/2)+1):
        if(nb%i==0):
            prime=False
    return prime

def prime_integer_summation() -> int:
    sum=0
    nb_prime =0
    nb=2
    while nb_prime<100:
        if is_prime(nb):
            sum+=nb
            nb_prime+=1
        nb+=1   
    return sum


def factorial(number: int) -> int:
    result=1
    for i in range(1,number+1):
        result*=i
    return result


def use_continue() -> None:
    for i in range(1,10+1):
        if i==5:
            continue
        else:
            print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    status=[]
    for i in range(len(groups)):
        group_status=True
        old_age=False
        gold_age=False
        if(len(groups[i])>10 or len(groups[i])<=3):
            group_status=False   
        else:
            for j in range(len(groups[i])):
                if(groups[i][j]<18):
                    group_status=False
                if(groups[i][j]>70):
                    old_age=True
                if(groups[i][j]==50):
                    gold_age=True
                if(gold_age and old_age):
                    group_status=False
                if(groups[i][j]==25):
                    group_status=True
                    break
        status.append(group_status)
    return status


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
