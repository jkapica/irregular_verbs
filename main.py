import os
import sys
import csv
from time import sleep
from random import choice, shuffle


HERE = os.path.dirname(os.path.abspath(__file__))

cols = ["infinitive", "past simple", "past participle", "pl"]


def shuffled(collection):
    col = collection.copy()
    shuffle(col)
    return col


def main(argv):
    verbs = dict()
    
    with open(os.path.join(HERE, 'verbs.csv')) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=cols)
        for i, row in enumerate(reader):
            verbs[i] = row

    loopctl = True
    while verbs and loopctl:
        idx = choice(list(verbs.keys()))
        verb = verbs[idx]
        print(f'\n{idx}>>> {verb["pl"]}?')    
        
        answers = []
        for c in shuffled(cols[:3]):
            print(f"{c}: ", end='')
            answer = input()
            if answer.strip() == 'q':
                loopctl = False
                break
            if answer == verb[c]:
                print("OK")
                answers.append(True)
            else:
                print(f"wrong, correct is: {verb[c]}")
                answers.append(False)

        if all(answers) and len(answers) == 3:
            print(f"{idx}: {', '.join(verb.values())} -> All OK")
            verbs.pop(idx)
        sleep(0.5)

    if loopctl:
        print('BRAVO!\n\nPress enter to finish...')
        input()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
