bread = 0
pb = 0
jelly = 0
# I have all the ingredients.
if bread >= 2 and pb >= 1 and jelly >= 1:
	if jelly <= pb and jelly*2 <= bread:
		print "I can make {0} peanut butter and jelly sandwiches.".format(jelly)
		if jelly < pb:
			if pb <= bread / 2:
				print "I can make {0} peanut butter sandwiches. Buy jelly.".format(pb - jelly)
				if pb < bread/2:
					print "Buy pb too."
				elif pb * 2 > bread:
					print "Buy bread too."
			elif bread / 2 < pb:
				print "I can make {0} peanut butter sandwiches. Buy jelly and bread.".format((bread/2)-jelly)
	elif pb < jelly and pb*2 <= bread:
		print "I can make {0} peanut butter and jelly sandwiches. Buy more pb.".format(pb)
		if jelly < bread/2:
			print "Buy more jelly too."
		elif jelly > bread/2:
			print "Buy more bread too."
	elif bread / 2 < pb and bread / 2 < jelly:
		print "I can make {0} peanut butter and jelly sandwiches. Buy more bread.".format(bread/2)
		if bread % 2 == 1:
			print "I can make an open-face pbj sandwich, too."
elif bread >= 2 and pb >= 1 and jelly == 0:
	print "I can make a peanut butter sandwich. Buy jelly."
else:
	print "No lunch for me."
	if bread < 2:
		print "Buy bread."
	if pb == 0:
		print "Buy pb."
	if jelly == 0:
		print "Buy jelly."
