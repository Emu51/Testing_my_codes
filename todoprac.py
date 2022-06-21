global data,main_data

filename="todoprac.txt"



f=open(filename,'r')

main_data=f.read()

main_data=main_data.split('\n')

main_data=(list(filter(None,main_data)))

datas = list()





class todo_list():

	def __init__(self, item_id=0,description='',date='',place=''):

		self.item_id = item_id

		self.description = description

		self.date = date

		self.place = place




	def write_file(self,list_data):

		f = open(filename, "w")

		all_data = str()

		for data in list_data:

			all_data += data+'\n'

		f.write(all_data)

		f.close()

		return True



	def show_contact(self):
        

		for data in main_data:

			split_data=data.split(',')

		print("Item_Id:",split_data[0])

		print("Description:",split_data[1])

		print("Date :",split_data[2])

		print("Place :",split_data[3])
		



	def add_contact(self):

		item_id=input("Create Item ID :")

		description = input("Description :")

		date =input("Date :")

		place =input("Place :")


		data=item_id+','+description+','+date+','+place+'\n'



		f = open(filename, "a")

		f.write(data)

		f.close()

		print("Item Add")





	def edit_contact(self,no):

		print("Item ID :",no)

		description=input("Description :")

		date=input("Date :")

		place=input("Place :")




		new_value=no+','+description+','+date+','+place



		for data in main_data:

			split_data=data.split(',')

			if no ==split_data[0]:

				main_data[main_data.index(data)] = new_value

				self.write_file(main_data)

				print("Successfully Updated")

				return True

		print("Try Again")	





	def remove_contact(self,no):

		for data in main_data:

			split_data=data.split(',')

			if no==split_data[0]:

				main_data.remove(data)

				break



		if (self.write_file(main_data)):

			print("Successfully Deleted")

		else:

			print("Try Again")

				

				



	def search_id(self,no):
		#print(main_data)

		for data in main_data:

			split_data=data.split(',')

			#print(split_data[0])

			if no==split_data[0]:

				return True



		return False



def menu():

		my_class=todo_list()



    




		choice= int(input(" 1. Add Item \n 2.Update Item \n 3.Delete Item \n 4.Display Item \n 5.Quit \n Enter your Choice"))



		if choice==4:

			my_class.show_contact()



		elif choice==1:

			my_class.add_contact()

		elif choice==2:

			num=input("Item ID :")

			if my_class.search_id(num):

				my_class.edit_contact(num)

			else:

				print("Incorrect Item ID")

				

		elif choice==3:

			num1=input("Item ID for delete :")
			#print(main_data)

			if my_class.search_id(num1):

				my_class.remove_contact(num1)

			else:

				print("Incorrect Item ID")



		elif choice==5:

			print("Thank You")

			quit()



		else:

			print("Invalid Input!!")






class main():

	def __init__(self):

		self	

while True:
	menu()	