'''
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
'''


import CourseClass as cc
def main():

   #1) Creat an instance of the Coure object

   adv_python = cc.Course('MIS 4322 - Advanced Python', '250309', 4, 'open')



   students = ['John','James','Jill','Jack','Joanne']
#2) create an instance of the Register object for each student in the students list using a for loop 
   registration_list = []
   number = 0 
   for s in students:
      student = cc.Register(s, adv_python.get_crn())
      registration_list.append(student)
      

#3) print student name, course name, CRN number, and seats left for each iteration using ONLY get methods



   if adv_python.get_status() == 'open':
      print()
      print("Student Name: ", student.get_name())
      print("Course Number: ", adv_python.get_name())
      print("CRN: ", adv_python.get_crn())
      print("Seats Left: ", adv_python.update_seat_count())
   else:
      print("Sorry" , student.get_name(), "registration is closed for" , adv_python.get_name())

  
    
main()



        
    
    
