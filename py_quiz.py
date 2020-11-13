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

    # Creo una matrice delle risposte  
    for fold in list_folders:
        dir_quest = MAIN_DIR + fold
        # Prelevo le domande dalla cartella
        quest = [f for f in os.listdir(dir_quest) if os.path.isfile(os.path.join(dir_quest, f))]
        aux_q = []
        for q in quest:
            aux_q.append(q)
        all_quest.append(aux_q)


    for i in range(n):
        bool = True
        while bool:
            if len(list_folders)==0:
                print('Hai esaurito le domande nel database.')
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
                    with open(dir_quest + '/' +  quest[rnd2], 'r') as qfh:
                        list_quest.append(qfh.read())
                        all_quest[rnd1].remove(quest[rnd2])
                    bool = False
  
    print('\n\nINIZIO DEL QUIZ:')
    print('Le domande alle quali devi rispondere sono le seguenti:\n')
    for i, question in enumerate(list_quest):
        string = 'question  '
        aux_index = question.find(string) + len(string)
        print(f'1. {question[aux_index:]}')
    

if __name__ == '__main__':                      # Per fare un modulo con più librerie (mie)
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    parser.add_argument('-chap','-c', nargs='+', help="Number or Name of the folder in 'quest/'", required=True)
    parser.add_argument('-num_quest','-n', help="Number of question to randomize", required=True, type=int)
    args = parser.parse_args()
    execute(args.chap, args.num_quest)

