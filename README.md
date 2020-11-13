# ExamsQuiz
Create a random quiz in latex and ASCII format
## How to install
Open a terminal and type:

`git clone https://github.com/dodogabrie/ExamsQuiz.git`

## How to use

### Create chapter folders

You need to create the folder of the chapters of your course in the folder "domande". The chapter's name have to be preceded by the number of the chapter himself like "1_chapname".

### Create your first question

Run "pycrea.py" to write your first question in the following way:

`python3 pycrea.py n`

Where n need to be replaced with the number of the chapter in which you wanna put your question (this will search for the folder that you create in the previous step).

After that just follow the instruction on screen and at the end you'll see a dummy file in the chapter folder with your question. 

### Create your random sequence

You can choose if create an ascii quiz without leaving your terminal or if you want to write the sequence in the latex file.

#### ASCII sequence

Run the file "py_quiz.py" in the following way:

`python3 py_quiz.py -c chapters -n numquestion`

- chapters: the numbers of the chapter folders or the names of the folders themeselves (you can pass more folder here)
- numquestion: the number of question that you wanna generate.

#### LaTex sequence

Run the file "tex_quiz.py" in the same way as the previous one:

`python3 tex_quiz.py -c chapters -n numquestion`

This will write in the "esame"'s folder the file "domande.tex" which contains the question that you chose.

# Structure Example

After that you'll have folder like this one:

.
 * [LICENSE](./LICENSE)
 * [domande](./domande)
   * [1_termo](./domande/1_termo)
     * [termo1.tex](./domande/1_termo/termo1.tex)
     * [termo2.tex](./domande/1_termo/termo2.tex)
     * [termo3.tex](./domande/1_termo/termo3.tex)
     * [termo4.tex](./domande/1_termo/termo4.tex)
     * [termo5.tex](./domande/1_termo/termo5.tex)
   * [2_ensemble](./domande/2_ensemble)
 * [esame](./esame)
   * [domande.tex](./esame/domande.tex)
   * [master.tex](./esame/master.tex)
 * [IO_gestion.py](./IO_gestion.py)
 * [pycrea.py](./pycrea.py)
 * [py_quiz.py](./py_quiz.py)
 * [tex_quiz.py](./tex_quiz.py)

