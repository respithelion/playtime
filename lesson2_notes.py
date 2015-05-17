# attendees = ["Mariah", "Rose", "Michelle"]
# print attendees[1]
# number_of_attendees = len(attendees)
# attendees.append("Sarah")
# print attendees
# attendees_ages = []
# attendees_ages.append(28)
# attendees_ages[0] = 29
# print attendees_ages

days_of_week = ["Monday", "Tuesday"]
days_of_week.append("Wednesday")
days_of_week.append("Thursday")
days_of_week.append("Friday")
days_of_week.append("Saturday")
days_of_week.append("Day of rest")

days_of_week[2] = "Hump Day"

# day = days_of_week.pop(3)

months = ["January", "February"]
months.extend(["March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
months.pop(7)
months.insert(0, "August")

# address = "2055 North Vermont Street, Arlington, VA 22207"
# address_as_list = address.split(" ")
# print address_as_list

# print "January" in months
# print "Tuesday" in months

# NW_addresses = []
# NE_addresses = []
# SE_addresses = []
# SW_addresses = []

# address1 = raw_input("What's your address?")
# address2 = raw_input("What's the second address?")
# address3 = raw_input("What's the third address?")

# list_of_addresses = [address1, address2, address3]

# for address in list_of_addresses:
# 	if "NW" in address:
# 		NW_addresses.append(address)
# 	if "NE" in address:
# 		NE_addresses.append(address)
# 	if "SE" in address:
# 		SE_addresses.append(address)
# 	if "SW" in address:
# 		SW_addresses.append(address)

# quadrants = ["NW", "NE", "SE", "SW"]


# print "There are {0} NW Addresses.".format(len(NW_addresses))
# if len(NW_addresses) >= 1:
# 	print "The addresses are: {0}.".format(NW_addresses)

# print "\n There are {0} NE Addresses.".format(len(NE_addresses))
# if len(NE_addresses) >= 1:
# 	print "The addresses are: {0}.".format(NE_addresses)

# print "\n There are {0} SE Addresses.".format(len(SE_addresses))
# if len(SE_addresses) >= 1:
# 	print "The addresses are: {0}.".format(SE_addresses)

# print "\n There are {0} SW Addresses.".format(len(SW_addresses))
# if len(SW_addresses) >= 1:
# 	print "The addresses are: {0}.".format(SW_addresses)

# print range(5)

# for number in range(10):
# 	print number

# for flower in range(5):
# 	print flower

# for day in days_of_week:
# 	print day

# for month in months:
# 	print month
# 	for week in range(1,5):
# 		print "Week {0}".format(week)
# 		for day in days_of_week:
# 			print day

# for index, day in enumerate(days_of_week):
# 	print index, day

# days_of_week[0] = "Fidel's Day of Rest"

# print days_of_week

states = ["Massachusetts", "Florida", "Virginia"]
state_abbreviations = ["MA", "FL", "VA"]

for state_abbreviation, state in zip(state_abbreviations, states):
	print state_abbreviation, state
