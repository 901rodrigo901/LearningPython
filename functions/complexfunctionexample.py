
#Here we are setting force uppercase equal to
#true by deffect
def get_initial(name, force_uppercase =True):
	if force_uppercase:
		initial = name[0:1].upper()
	else:
		initial = name[0:1].lower()
	return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)
# i am just sending one parameter in a function 
# with 2 parameter because get_initial has a 
# value true by defect

#I can call the function get_initial in this other way
#get_initial(force_uppercase=False,name = first_name)
# in that wat the order of the parameter could by any
print('Your initial is:' + first_name_initial)
