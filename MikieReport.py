print("Put in how many calls Mikie made:")
calls_Dialed = input(int())
print("\nPut in how many Act! entries Mike did:")
act_Input = input(int())

if int(calls_Dialed) > 70 and int(act_Input) > 120:
        print("Good work all round!")
elif not int(calls_Dialed) > 70 and int(act_Input) > 120:
    print("You need to make more calls!")
elif int(calls_Dialed) > 70 and not int(act_Input) > 120:
    print("You need to work on your data entry!")
else:
    print("What happened today?")


