# made by dylan h., not me


playerhp = 100
enemyhp = 100
turn = 0

from random import *

while playerhp > 0 and enemyhp > 0:

    while turn == 0 and playerhp > 0:
        paction = raw_input('attack or heal? ')

        if paction == 'attack':
            edamage = randint(10, 20)
            enemyhp -= edamage
            print "You attack and do %s damage. The enemy has %s hp left" % (edamage, enemyhp)
            turn += 1


        if paction == 'heal':
            pheal = randint(10, 20)
            playerhp += pheal
            print "You recover %s hp. You now have %s hp." % (pheal, playerhp)
            turn += 1

    while turn == 1 and enemyhp > 0:
        eaction = randint(1, 2)

        if eaction == 1:
            pdamage = randint(10, 10)
            playerhp -= pdamage
            print "The enemy attacks and does %s damage. You have %s hp left." % (pdamage, playerhp)
            turn -= 1


        if eaction == 2:
            eheal = randint(10, 20)
            enemyhp += eheal
            print "The enemy recovers %s hp. It now has %s hp" % (eheal, enemyhp)
            turn -= 1




if playerhp <= 0:
    print "Game over, you lose"


if enemyhp <= 0:
    print "Game over, you win"
