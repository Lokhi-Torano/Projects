import random
player_list=["lokhi","satheesh","ramya","aadhi","nithya","kishore","praveen","bharat"]
print("                    LUDO TALENT SHUFFLER")
print(" THE PLAYERS ARE : \n")
for name in range(0,len(player_list)):
    print(name+1,player_list[name],"\n")
def add_players():
    num_mem_add=int(input("enter number of players you wanna add (in numbers) : "))
    for mem in range(0,num_mem_add):
        player=str(input("please enter the name(s) : "))
        player_list.append(player)
    print("players added succesfully")
    shuffle()
def print_players(team_1,team_2):
    print("   ")
    print("first team :\n")
    for i in range(0,len(team_1)):
        print("-+-+-",i+1,". ",team_1[i],"-+-+-\n")
    print("second team :\n")
    for j in range(0,len(team_2)):
        print("-+-+-",j+1,". ",team_2[j],"-+-+-\n")
def remove_players():
    num_mem_delete=int(input("enter number of players you wanna delete (in numbers) : "))
    for mem in range(0,num_mem_delete):
        print(player_list)
        player=str(input("please enter the name(s) : "))
        player_list.remove(player)
    print("players removed successfully")
    print(player_list)
    shuffle()
def shuffle():
    #check_list for 8 members
    if len(player_list)==8:
        #team should have 4 members
        #team_1_empty_list
        team_1=[]
        #team_2_empty_list
        team_2=[]
        #shuffling players
        random.shuffle(player_list)
        #adding team members to team_list
        for i in range(0,int(len(player_list)/2)):
            team_1.append(player_list[i])
        for j in range(int(len(player_list)/2),int(len(player_list))):
            team_2.append(player_list[j])
        print_players(team_1,team_2)
    if len(player_list)<8:
        player_req=8-len(player_list)
        print("please add  ",player_req," for shuffling ....")
        add_players()
    if len(player_list)>8:
        excess_player=len(player_list)-8
        print("please remove ",excess_player,"for shuffling .....")
        remove_players()
print("Options :")
print("1 . Shuffle")
print("2 . Add players")
print("3 . Delete players\n")
mem_query=int(input("do you wanna Shuffle or Add players or Delete players? "))
if mem_query==1:
    shuffle()
if mem_query==2:
    add_players()
if mem_query==3:
    remove_players()
