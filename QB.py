import os
import random
import csv
from csv import writer

print("Console app for an IT academy")

file_name='Information.csv'
with open(file_name,mode='w') as file:
	writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['ID', 'Name', 'Course', 'Paid ','Remaining amount'])
while (True):
	print('\n1.Enquiry about courses')
	print('2.Registering for course')
	print('3.See students details')
	print('4.Delete student')
	print('5.Exit')
	ch=int(input('Enter the choice !'))
	if ch==1:
		myfile=open('course.txt')
		print(myfile.read())
		a=int(input('Which course do you want to enquire?\nPlease enter the number to choose the course \n'))
		if a==1:
			python=open('python.txt')
			print(python.read())
		elif a==2:
			java=open('java.txt')
			print(java.read())
		elif a==3:
			javascript=open('javascript.txt')
			print(javascript.read())
		elif a==4:
			csharp=open('C#.txt')
			print(csharp.read())
		elif a==5:
			oops=open('C++.txt')
			print(oops.read())
		else:
			print('Wrong Choice!')

	elif ch==2:
		i = random.randint(0,1000)
		name=input('Enter your full name:')
		course=input('Enter your course:')
		payment=int(input('Enter your payment:'))
		rem_amt=20000-payment

	   #adding new rows

		if((course=='python') or (course=='java') or (course=='javascript') or (course=='C#') or (course=='C++')):
			from csv import writer
			def append_list_as_row(file_name, list_of_elem):
				with open(file_name, 'a', newline='') as write_obj:
					csv_writer = writer(write_obj)
					csv_writer.writerow(list_of_elem)

			row_contents=[i,name,course,payment,rem_amt]
			append_list_as_row('Information.csv',row_contents)
			print("Registered successfully !")
		else:
			print("Course not available")
	#reading informations about students
	elif ch==3:
		print('students details:\n')
		with open('Information.csv') as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				print(row)
	elif ch==4:
		fh_r=open('Information.csv','r')
		fh_w=open('temp.csv','w')
		uid=int(input('Enter id that you want to delete:'))

		s=''
		while(s):
			s=fh_r.readline()
			L=s.split(",")
			if len(s)>0:
				if int(L[0])!=uid:
					fh_w.write(s)

		fh_w.close()
		fh_r.close()
		
		os.remove('Information.csv')
		os.rename('temp.csv','Information.csv')
		print("Deleted successfully")
		
	

	elif ch==5:
		exit()

	else:
		print("Wrong Choice!")

