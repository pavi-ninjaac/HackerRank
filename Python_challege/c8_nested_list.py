"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Sample Input 

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 

Berry
Harry
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 19:54:35 2020

@author: ninjaac
"""
if __name__ == '__main__':
    student=[]
    score_list=[]
    for _ in range(int(input("enther the number of student"))):
        name = input("enter the name")
        score = float(input("enter the score"))
        score_list.append(score)
        student.append([name,score])
    print(student)
    print(score_list)
    min_score1=min(score_list)
    for i in range(score_list.count(min_score1)):
        score_list.remove(min_score1)
    print(score_list)
    min_score2=min(score_list)
    print(min_score2)
    list_name=[]
    
    for i in student:
        if min_score2==i[1]:
            list_name.append(i[0])
    list_name.sort()
    for i in list_name:
        print(i)
             
