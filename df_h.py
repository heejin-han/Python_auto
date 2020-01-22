import commands

room=[]
room2=[]
output = commands.getoutput('df -h')
room = output.split('\n')

for line in room:
    room2=line.split(" ")
    c_list = list(filter(None, room2))
    test = c_list[4].split("%")
    if room2[0] == "Use":
        print("%s  Use" % c_list[0])
    elif int(test[0]) > 60:
        print("%s condition is bad" % c_list[0])
    else:
        print("%s condition is Good" % c_list[0])

