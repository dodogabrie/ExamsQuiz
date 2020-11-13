def new_quest():
    """Create of new exams question"""
    bigloop = True
    while bigloop:
        quest_tmp = input('Write the new question below:\n')
        print(f'Do you Want to insert the following question?\nQuest: {quest_tmp}')
        loop = True
        patient = 0
        while loop:
            yn = input('Do you want to proceed writing, undo or redo [y/n/r]: ')
            if yn=='y':
                quest=quest_tmp
                bigloop=False
                loop=False
            else:
                if yn=='n':
                    quest=0
                    bigloop=False
                    loop=False
                else: 
                    if yn=='r':
                        loop=False
                    else:
                        patient+=1
                        if patient>=5:
                            print('ARE YOU DRUNK?')
                            loop=False
                        else:
                            print("Please insert just 'y' or 'n'...")
    return quest



