from itertools import permutations
import random
sekv = ["0","1","2","3","4","5","6","7","8","9","a","zgod","mla","pok","skup"]
rn = random.choice(sekv)
global bombb
bombb = "bomb{}.txt".format(rn)
with open(bombb ,"w+") as starter:
    starter.write("Welcome to the bomb experience by HoxX\n")
    starter.close()
    
def RandomGenerator():
    print("[+]Decompression bomb running !\n")
    print("[+]WARNING ! This program takes around 30s to generate 1 gigabyte.\n")
    
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cap_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    decyphers = ["Python","Visited","You","Hahahahah"]

    complete_list = letters + cap_letters + numbers + decyphers
    perm = permutations(complete_list)
    #perm = permutations(list(perm))  if you want the CPU to be at 90% and Memory also.
    #if you dont and you just want to take up space , run the regular thing
    with open(bombb ,mode="a") as file:
        for k in perm:
            file.write(str(k))
    file.close()
        
    RandomGenerator()

try:
    RandomGenerator()
except:
    RandomGenerator()

#       CODE FROM THE VIDEO

"""Hello and welcome !

So I had an idea about making a program like this and now i’ve decided to make it, so i did. It isnt great and it isnt using 100% of what it could be but that’s on purpose, so that you can test it on your PC. For example, generating data into a text file gives us 1gb in cca 30 seconds; You can shorten that time easily, since that part of the program uses around 30% cpu and 20% memory. Meaning you can at least triple it. As far as Memory/CPU slowdown part goes – you cannot improve this much, but you can get it all to a 100% and bug the whole system out. Inspired by a decompression bomb and the one-line-crash bug thing where you make a .sh and into it you put a bunch of () in a correct order and it crashes the whole system.

The code:

import random
import string
from itertools import permutations

def DecompressionThing():
rn = random.choice(string.ascii_lowercase)
global bombb
bombb = “bomb{}.txt”.format(rn)
with open(bombb ,”w+”) as starter:
starter.write(“Welcome to the bomb experience by HoxX\n”)
starter.close()

def RandomGenerator():
    print("[+]Decompression bomb running !\n")
    print("[+]WARNING ! This program takes around 30s to generate 1 gigabyte.\n")


    decyphers = ["Python","Visited","You","Hahahahah","SomeRandomWordsHere"]

    allthestuff = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits) + decyphers
    perm = permutations(allthestuff)

    with open(bombb ,mode="a") as file:
        for k in perm:
            file.write(str(k))
    file.close()

RandomGenerator()
def MemoryThing():
print(“[+] CPU, Memory slowdown running !\n”)
decyphers = [“Python”,”Visited”,”You”,”Hahahahah”]
allthestuff = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits) + decyphers
perm = permutations(allthestuff)
perm = permutations(list(perm))

Thats it !
-Make sure you check out the video if you want to hear another one of my ideas about (sort of) pentesting.
Thank you so much for visiting and have a nice day.
"""
