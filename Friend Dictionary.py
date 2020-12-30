friend_dict={}
while  True:
    try :
        user = input("Friend name: ").lower()
        if user not in friend_dict:
            phone_no=int(input("Phone no : "))
            friend_dict.update({user:phone_no})
        else:
            print("This friend is allready Exist in Your dictonary!")
            break
    except:
        print("Please Enter proper type!")
print("Friend   phoneNo",end="\n\n")
for u,p in sorted(friend_dict.items()): 
    print(u,p)