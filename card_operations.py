filepath = 'card.txt'

def classification():
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            if "Creature" in line:
                print("This is a Creature")
                if "Human Druid" in line:
                    print("of class Human Druid")
                return 1
            if "Instant" in line:
                print("This is an Instant Spell")
            if "Sorcery" in line:
                print("This is a Sorcery Spell")

classification()
