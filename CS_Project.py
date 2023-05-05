import mysql.connector
'''
'Complete the Word Puzzle'
Program made by - GUNVEER SINGH

© All Rights Reserved
'''
name = input("Enter your Name: ")

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database= "")
mycursor=mydb.cursor()

que = "select points from cs where name = '"+name+"'"

d = mycursor.execute(que)
res = mycursor.fetchall()

total = 0

for elem in res:
    
    total += elem[0]

if total == 0:
    mycursor.execute("insert into cs values('"+name+"','"+str(0)+"')")
    mydb.commit()
    previous = 0
else:
    previous = total


from random import *

print()
print("********************************** Welcome to Vocabulary Improver **********************************")
print()
print()
print("*********************************************    SELECT   **********************************************")
print()
print()
print("EASY ==> 1")
print()
print("MEDIUM ==> 2")
print()
print("HARD ==> 3")
print()

level_choice = input("Enter your choice: ").strip()
print()

file = open(f'WordQuiz_DataFiles//{level_choice}.txt', 'r')

data = file.read()

b = data.split('\n')

file.close()

ques = input('How many questions should be there in the Quiz? : ').strip()
print()

points = 0

for elem in range(int(ques)):
    a = choice(b)
    print((a[0:(len(a) - 2)]) + '_' + a[(len(a) - 1):])
    print()
    inp = input('Enter the missing LETTER: ').strip().lower()
    print()
    if inp == a[(len(a) - 2)]:
        points += 1
        print('You are absolutely RIGHT!')
        print()
        print('------------------------')
    else:
        print('Ohh! Your answer is WRONG!')
        print()
        print(f"The Correct Letter is '{a[(len(a) - 2)]}' and the word is '{a}'")
        print()
        print('------------------------')
        print()
print(f"You scored {points} out of {ques} !")
print()
print("Keep playing this game Daily to improve your Vocabulury!")

sql = "UPDATE cs SET points =%s WHERE Name = %s"
final_points = previous + points
data = (final_points,name)
mycursor.execute(sql,data)
mydb.commit()    
