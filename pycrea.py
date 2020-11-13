import sys
import os
import argparse                                 # Make --help description
import IO_gestion 
_DESCRIPTION = 'Write a new question in a question folder file'

def execute(chap):
    MAIN_DIR = 'domande/'
    # Estraggo la cartella se l'utente passa un numero
    folders = [name for name in os.listdir(MAIN_DIR) if os.path.isdir(os.path.join(MAIN_DIR, name))]
    for f in folders:
        num = ''.join([n for n in f if n.isdigit()])
        if chap==num:
            chap=f

    file_path = MAIN_DIR + chap

    # Get the new question
    try:
        quest = IO_gestion.new_quest()
        assert type(quest)==str
    except:
        print('Process stopped')

    # extracting file names in file_path into the list "files"
    files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
    # Find and remove the first number that broke the algorithm
    aux_index = file_path.find('_') + 1
    aux_name = file_path[aux_index:]

    # creating new file name with a final number ( the higher in the folder + 1 )
    if len(files)==0: # if there aren't files then it will create "final_folder1" (final folder is the last folder in file_path)
        namefile = aux_name + '1'
    else: # Else I search for the highest number in the names of files and add to those 1, creating the name "final_folder(n+1)"
        a = 0
        for f in files:
            num = ''.join([n for n in f if n.isdigit()])
            if int(num)>a:
                a = int(num)
        num = a+1
        namefile = aux_name + str(num)
    # Write the new question in the file_path
    f = open(os.path.join(file_path, f'{namefile}.tex'), "w")
    f.write(r"\question")
    f.write(f"  {quest}\n")
    #f.write(r"\end{questionblock}")
    f.close()

if __name__ == '__main__':                      # Per fare un modulo con più librerie (mie)
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    parser.add_argument('chap', help='Chapter number or name (suggestion: 1 or 1_firstfolder)')
    args = parser.parse_args()
    execute(args.chap)

