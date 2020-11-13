import sys
import os
import random
import argparse                                 # Make --help description

_DESCRIPTION = 'Generate a number (-n) of quest of chosen argument (-c) in file domande.tex'


def execute(chap, n):

    exam = 'esame/domande.tex'
    MAIN_DIR = 'domande/'
    folders = [name for name in os.listdir(MAIN_DIR) if os.path.isdir(os.path.join(MAIN_DIR, name))]
    list_folders = []
    list_quest = []
    all_quest = []
    for c in chap:
        for f in folders:
            num = ''.join([n for n in f if n.isdigit()])
            if c==f or c==num:
                list_folders.append(f)
                folders.remove(f)
    
    for fold in list_folders:
        dir_quest = MAIN_DIR + fold
        quest = [f for f in os.listdir(dir_quest) if os.path.isfile(os.path.join(dir_quest, f))]
        aux_q = []
        for q in quest:
            aux_q.append(q)
        all_quest.append(aux_q)


    for i in range(n):
        print(len(list_folders))
        bool = True
        while bool:
            if len(list_folders)==0:
                print('Hai selezionato tutte le domande.')
                bool = False
            else:
                # Generate random number for folder index
                rnd1 = random.randint(0,len(list_folders)-1) 
                # choose random folder
                dir_quest = MAIN_DIR + list_folders[rnd1]
                # find the question in that folder
                quest = all_quest[rnd1]
                #quest = [f for f in os.listdir(dir_quest) if os.path.isfile(os.path.join(dir_quest, f))]
                if len(quest)==0:
                    list_folders.remove(list_folders[rnd1])
                    all_quest.remove(all_quest[rnd1])
                else:
                    # generate another random numb for quest index
                    rnd2 = random.randint(0,len(quest)-1)
                    print(f'ho pescato {quest[rnd2]}')
                    with open(dir_quest + '/' +  quest[rnd2], 'r') as qfh:
                        list_quest.append(qfh.read())
                        all_quest[rnd1].remove(quest[rnd2])
                    bool = False
   
    with open(exam, 'w') as efh:
        for question in list_quest:
            print(question, file=efh)
    

if __name__ == '__main__':                      # Per fare un modulo con più librerie (mie)
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    parser.add_argument('-chap','-c', nargs='+', help="Number or Name of the folder in 'quest/'", required=True)
    parser.add_argument('-num_quest','-n', help="Number of question to randomize", required=True, type=int)
    args = parser.parse_args()
    execute(args.chap, args.num_quest)

