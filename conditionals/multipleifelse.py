country = input("write your country: ")

if country.capitalize() == 'Canada':
	province = input('write your province:')
	if province.capitalize() in('Alberta','Nunavut','Yukon'):
		tax = 0.05
	elif province.capitalize() == 'Ontario':
		tax = 0.13
	else:
		tax = 0.15
else:
	tax = 0.0

print(tax)
