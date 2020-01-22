import commands

room=[]
room2=[]
output = commands.getoutput('free-m')
room = output.split('\n')

for free in room:
    room2=free.split(" ")
    free_list = list(filter(None, room2))

    if free_list[0] !="total":
        if int(free_list[2])/int(free_list[1])*100 >60 :
            print("bad")
        else:
            print("good")
    else:
        print("result")