import commands

room=[]
room2=[]
output = commands.getoutput('sar 1 5')
room = output.split('\n')

for free in room:
    room2 = free.split(" ")
    free_list = list(filter(None, room2))

    if free_list[0] !="Linux":
        if int(free_list[8]) <70 :
            print("bad")
        else:
            print("good")
    else:
        print("result")