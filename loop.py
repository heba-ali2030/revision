
# import constant

# print(constant.PI)
# print(constant.GRAVIRTY)


## for loop
# list= ['heba', 'hna', 'hala', 'hager']
# for name in list:
#     print (name[2])


# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# sum=0
# for i in numbers:
#     sum= i+ sum
# print(sum)


# print (range (10))
# print (list(range (0,10,2)))


# Program to iterate through a list using indexing

# fruits = ['orange', 'banana', 'apple']

# iterate over the list using index
# for i in fruits:
#     print("I like", i)
# else:
#     print('No items left.')

# for i in range(len(fruits)):
#     print("I like", fruits[i])

# program to display student's marks from record
# student_name = 'James'

# marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

# for student in marks:
#     if student == student_name:
#         print(student, marks[student])
#         break
# else:
#     print('No entry with that name found.')


# number= int(input(' choose a number to begin with: '))

# sum=0
# i= 1
# while i <= number:
#     sum= sum + i
#     i= i + 1
#     print(sum)
# else:
#     print('your trials for adding are over ')

# string= ('sringidihrgit')
# for letter in string:
#     if letter== 'i':
#         print(string.replace('i', str(string.index('i'))))
#         continue
#     print(letter)

# print('The end')



# clothes = 'available'
# shoes = None

# def shopping (x):
#     if x == clothes:
#         print (clothes)
#     else:
#         print(shoes)

# shopping (clothes)
# shopping (shoes)

# def absolute_value(num):
#     """This function returns the absolute
#     value of the entered number"""

#     if num >= 0:
#         print(num)
#     else:
#         return -num


# absolute_value(2)

# print(absolute_value(-4))

# def greet(name, msg= 'How do you do ? '):

#     print ('hello', name + ' , ' + msg )

# greet('heba', 'good morning')
# greet ('hala')

def greet (*names):
    #     *= asterisk
    ''' this is when you don't know number of arguements'''

    for name in names:
        print('hello', name)

greet('heba', 'hala', 'hager', 'hna')

