# Beginning: This is a quiz to ask you if you're more like Taylor Swift's 'Lover' album or her 'reputation' album. 
lover_points = 0
reputation_points = 0

#Middle: Now is where all of the code is

answer = input("Which color is your favorite? A) pink B) black")
if answer == "A":
    lover_points += 1
elif answer == "B":
    reputation_points += 1

 
answer = input("What do you do on a friday night? A) hang out with friends B) party!!")
if answer == "A":
    lover_points += 1
elif answer == "B":
    reputation_points += 1


answer = input("Which do you prefer, A) Valentines day B) New Years Eve")
if answer == "A":
    lover_points += 1
elif answer == "B":
    reputation_points += 1


answer = input("Which do you prefer, A) Christmas B) Halloween")
if answer == "A":
    lover_points += 1
elif answer == "B":
    reputation_points += 1


answer = input("Cat or Snake? A) Cat B) Snake")
if answer == "A":
    lover_points += 1
elif answer == "B":
    reputation_points += 1

#End: Results 

if lover_points > reputation_points:
    print("You are more like the album 'Lover'! You're soft, sweet and love to hang out with friends.")
elif reputation_points > lover_points: 
    print("You are more like the album 'reputation'! You're hard on the outside but you're a big softie on the inside. You love to be by yourself, but may allow for some quality time with close friends")

