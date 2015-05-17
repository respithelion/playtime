# gender = 'f'
# if gender == 'f':
# 	print "Welcome to Hear Me Code!"
students = 10
capacity = 50
if students < capacity:
	print "Keep recruiting"	
else:
	print "End ticket signups"

teaching_assistants = 5
if teaching_assistants == 0:
	print "None? Uh oh!"
elif teaching_assistants < students / 5:
	print "Keep recruiting TAs"
else:
	print "Aren't the TAs great though?"

volunteers = 10
goal = 50
if volunteers > goal:
	print "Great job. You are exceeding goal!"
elif volunteers == goal:
	print "Good job. You met goal!"
else:
	print "Keep up the effort."

article = '...'

men_quoted = article.count(" he said'")
women_quoted = article.count(" she said")

if men_quoted == 0 and women_quoted == 0:
	print "Neither men nor women were quoted."
else: 
	if men_quoted > women_quoted:
		print "More men than women were quoted."
	elif women_quoted > men_quoted:
		print "More women than men were quoted."
	else:
		print "Women and men were quoted equally."

if women_quoted == 0 or men_quoted > women_quoted * 2:
	print """No women were quoted, or twice as many quotes came form men."""
