value = 1
count = 1

print(f"you have {value} dolah. \nwhat you want: \n(D)ouble it \n(G)et current")

M = input("What you want? D or G\n")

while count < 32:
    if M == "D":
        value *= 2
        count += 1
        print(f"you now have {value} dolah \n level {count}")
        M = input("What you want? D or G\n")
        if count == 32:
            value *= -1
            print("OVERFLOW HAS ATTACKED\n GAME OVER\n *ENDING 2*")
            print(f"you got {value} dolah")
            break

    elif M == "G":
        print(f"you got {value} dolah\n GAME OVER\n *ENDING 1*")
        break

    else:
        print("Input D or G")
        M = input("What you want? D or G\n")
