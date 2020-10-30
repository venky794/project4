import requests
import json

BASE_URL='http://127.0.0.1:8000/'
END_POINT='crud/'

def get_single_data():
	id=input('enter the id : \t')
	data={}
	if id is not None:
		data={'id':id}
	response=requests.get(BASE_URL+END_POINT,data=json.dumps(data))
	print(response.json())
	print(response.status_code)



def get_total_data(id=None):

	data={}
	if id is not None:
		data={'id':id}
	response=requests.get(BASE_URL+END_POINT,data=json.dumps(data))
	print(response.json())
	print(response.status_code)


def create_data():
	eno=int(input('enter the employee number :\t'))
	ename=input('enter the employee name : ')
	esalary=int(input('enter the employee salary :\t'))
	eaddress=input('enter the employee address : \t')
	created_data={'eno':eno,'ename':ename,'esalary':esalary,'eaddress':eaddress}

	response=requests.post(BASE_URL+END_POINT,data=json.dumps(created_data))
	print(response.json())
	print(response.status_code)



def update_partial_data():
	id=input('enter the id : \t')
	update_data = {'id':id ,'esalary':85000,'eaddress':'bangalore'}
	response = requests.put(BASE_URL+END_POINT,data=json.dumps(update_data))
	print(response.json())
	print(response.status_code)



def update_total_data():
	id=input('enter the id : \t')

	eno=int(input('enter the employee number :\t'))
	ename=input('enter the employee name : ')
	esalary=int(input('enter the employee salary :\t'))
	eaddress=input('enter the employee address : \t')
	updated_data={'id':id,'eno':eno,'ename':ename,'esalary':esalary,'eaddress':eaddress}

	response = requests.put(BASE_URL+END_POINT,data=json.dumps(updated_data))
	print(response.json())
	print(response.status_code)



def delete_data():
	id=input('enter the id : \t')
	emp_data={'id':id}	

	response=requests.delete(BASE_URL+END_POINT,data=json.dumps(emp_data))
	print(response.json())
	print(response.status_code)




if __name__ == '__main__':
	print('select the options below you want-->[get_single_data, get_total_data,create_data,update_partial_data,update_total_data,delete_data]')
	
	options=input('enter the options:\t')
	if options=='get_single_data':
		get_single_data()
	elif options=='get_total_data':
		get_total_data()
	elif options=='create_data':
		create_data()
	elif options=='update_partial_data':
		update_partial_data()
	elif options=='update_total_data':
		update_total_data()
	elif options=='delete_data':
		delete_data()
	else:
		print("Please provide valid option")


















