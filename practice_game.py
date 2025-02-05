print(r'''
    *********************************
    *       WELCOME TO CAVE ESCAPE   *
    *********************************
          ____
         /    \
        /_/  \_\
       (  o  o  )
        \   ^   /
         \_____/
''')

trap1 = r''' 
    You walk into a dim tunnel...
        _____
       /     \
      |  RIP  |
       \_____/
'''

trap2 = r'''
    You stumble into a pit filled with spikes!
        XXXX
       X    X
      X  RIP  X
       X    X
        XXXX
'''

gameOver = r'''
    You're swept away by the current!
        _____
       /     \
      |  GAME |
      |  OVER |
       \_____/
'''

safe = r'''
    You successfully cross the river on your raft!
        _____
       /     \
      |  SAFE |
       \_____/
'''  

win = r'''
    You found the exit and escaped the cave!
        * * * YOU WIN! * * *
           \o/
            |
           / \
'''

invalid = r'''
    Invalid choice. You hesitated too long!
        _____
       /     \
      |  GAME |
      |  OVER |
       \_____/
'''



print("Introduction:\nYou wake up trapped inside a dark, mysterious cave with only one goal—escape. The cave is filled with hidden dangers, secret passages, and strange symbols carved into the walls.")

left_or_right = input("You stand at a fork in the cave tunnel.\nGo Left: the tunnel is narrow and dimly lit.\nGo Right: The tunnel is wider but eerily quiet.\n").lower()

# First choice
if left_or_right == "left":
    print(trap1)
    swim_or_build = input("You reach an underground river with fast currents.\nSwim Across: Risk the strong current.\nBuild a Raft: Gather materials around you to safely cross.\n").lower()
    
    if swim_or_build == "swim across":
        print(gameOver)    

    elif swim_or_build == "build a raft":
        print(safe)  
        gold_or_silver = input("You cross safely and reach two ancient doors:\n- Type 'Gold Door' to enter the golden door.\n- Type 'Silver Door' to enter the silver door.\n").lower()

        if gold_or_silver == "gold door":
            print(win)

        elif gold_or_silver == "silver door":
            print(trap2)

        else:
            print(invalid)
    else:
        print(invalid)                
    
elif left_or_right == "right":
    print(trap2)

else:
    print(invalid)
