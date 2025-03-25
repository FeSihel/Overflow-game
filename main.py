''' How to play:
Turn on capslock key;
Press D to double | Press G to get current
'''

value = 1
count = 1

print(f"you have {value} dolah.")

M = input("What you want?\n") 
print("(D)ouble it \n(G)et current")

while count < 32:
    if M == "D":
        value *= 2
        count += 1
        print(f"you now have {value} dolah \n level {count}")
        M = input("What you want? D or G\n")
        if count == 32:
            print("OVERFLOW HAS ATTACKED\n GAME OVER\n *ENDING 2*")
            print(f"you got 0 dolah")
            break

    elif M == "G":
        print(f"you got {value} dolah\n GAME OVER\n *ENDING 1*")
        break

    else:
        print("Input D or G")
        M = input("What you want? D or G\n")
