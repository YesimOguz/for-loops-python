#use loops when you have to repeat an action multiple times

#A program that multiplies all the numbers in the by 3

#we cant say 'list' for a variable name.because python understand it as a code.
lst = [1,3,5,7,9,11]
for number in lst:
    result = number*3
     print(result)
#if we dont put a place before print ,it will give the last result.because print is not in loop, the last operation was 11*3.so result wil be 33
#if we want to creat a list with results;
lst = [1,3,5,7,9,11]
lst_times_3 = []
for number in lst:
    result = number*3
    #print(result)
    lst_times_3.append(result)
print(lst_times_3)
#if we put print in loop,it wil give result step by step.

#a program that adds 2 all the numbers 
lst = [2,4,6,8,10,12]
lst_add_5 = []
for number in lst:
    result=number+5
    lst_add_5.append(result)
print(lst_add_5)


#a program searches for whether or notaspecified fruit is in the basket
basket = ['oranges','plumps','apples','mangoes']
for fruit in basket:
    if fruit == 'plumps':
         print('found it!')
         #if we put here break it will give result untill plumps
         #if we put here continue it will be same result withot pu anything
         #if we delete print('found it!) an write continue,it will pass plumps and give other fruits.
    else:
        print(fruit)

ages = [0,4,8,-1,5,-3]
for age in ages:
    if age>0:
        print(age)
    elif age==0:
        print(age)
    elif age<0:
        age=0
        continue or break



   


    





    
