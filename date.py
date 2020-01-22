import commands

room =[]
output = commands.getoutput('date')
room=output.split(' ')

if room[4]=="JST":
	print("Good")


