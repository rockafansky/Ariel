import sys
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint
import random
from random import randint, choice
import simpleaudio as sa
from PIL import Image, ImageFilter

def turnPage():
    turn = str(input("Press Enter to continue."))
    if turn != "NO":
        print()
    else:
        sys.exit()

wave_objariel= sa.WaveObject.from_wave_file('arielsong.wav')
wave_objseren = sa.WaveObject.from_wave_file('serensong.wav')
wave_objrelik = sa.WaveObject.from_wave_file('reliksong.wav')

print()
print(".")
print("..")
print("...")
print("....")
print(".....")
print("ARIEL")
print(".....")
print("....")
print("...")
print("..")
print(".")
print()

print("The sun is setting on the town of Burning Rock, a tiny village at the base of a mountain ravaged by sporadic fires.")
turnPage()
print("Legend has it, there's a dragon living in a cave at the top, the cause of the ruined land. Many a hopeful hero has ventured to the top of the mountain to extinguish the flames, but none have returned.")
turnPage()
print("Of course, that's no concern of yours. You make a much safer living as a musician, entertaining the townspeople at the local tavern.")
turnPage()

Ariel = str(input("What is the name of our hero? ")).title()
if Ariel == "":
    Ariel = "Ariel"

if Ariel != "Ariel":
    im = Image.open('niccage.jpg')
    im.show()
    print()
    print("Welcome to the adventure, " + Ariel.title() + ".")
else:
    im = Image.open('niccage.jpg')
    im.show()
    print()
    print("Welcome to the adventure, Ariel.")
print()
turnPage()

print("The night is young. You've just completed your most popular set, an epic musical tale of the conquering heroes slaying magical beasts, but the patrons don't seem to be having it tonight.")
turnPage()
print("SING A DIFFERENT SONG!")
print("A rough bunch, this lot. One of them throws a mug of some foul-smelling drink at you, and it hits the wall behind you with a horrible splash.")
turnPage()
print("You're out of material for tonight. Your boss throws you a desperate look. Looks like you're going to have to improvise.")
turnPage()
print("You reach for your guitar again, and the audience seems to settle. Oh, shit. Shit. Shit. What are you going to sing?")
turnPage()

print("You clear your throat.")
print()
print("THERE ONCE WAS A HERO, WHO LIVED ON THE ISLE OF... ")
a = str(input("Uh, what's a place name? ")).upper()
print("ON THE ISLE OF " + a + ".")
print("AND HER NAME, HER NAME WAS...")
b = str(input("What was her name??? ")).upper()
print(b + "!")
c = str(input)
print("Hey, you're actually pretty good at this. Quick, let's sing a different one.")
print("What about that old English ballad? Do you remember the words?")
c = str(input("First, a place... ")).upper()
d = str(input("A plant? ")).upper()
e = str(input("Another plant. ")).upper()
f = str(input("I think it was another plant... ")).upper()
g = str(input("Another goddamn plant! ")).upper()
h = str(input("What was that adjective? ")).upper()
i = str(input("The girl in the song...What's her relationship to the singer? ")).upper()
j = str(input("Now, a material... ")).upper()
k = str(input("And an article of clothing. ")).upper()
l = str(input("A more specific part of that piece of clothing...")).upper()
m = str(input("Another adjective...")).upper()
n = str(input("A verb...")).upper()
o = str(input("Noun...")).upper()
p = str(input("Now a type of fruit...")).upper()
q = str(input("A man's name...")).upper()
print("That's it!")
turnPage()
print("...")
turnPage()
print("...")
turnPage()
print()
print("This is going to be harder than you thought.")
turnPage()

print("AHEM.")
print("ARE YOU GOING TO " + c + "?")
print(d + ", " + e + ", " + f + ", AND " + g + ".")
print("REMEMBER ME TO ONE THAT LIVES THERE.")
print("FOR ONCE SHE WAS A " + h + " " + i + " OF MINE.")
print()
print("TELL HER TO MAKE ME THE " + j + " " + k + ".")
print(d + ", " + e + ", " + f + ", AND " + g + ".")
print("ONE WITH NO " + l + "S, OF " + m + " NEEDLEWORK.")
print("AND THEN SHE'LL BE A " + h + " " + i + " OF MINE.")
print()
print("TELL HER TO " + n + " IT 'PON YONDER " + o + ".")
print(d + ", " + e + ", " + f + ", AND " + g + ".")
print("THAT NEVER BORE " + p + " SINCE " + q + " WAS BORN.")
print("AND THEN SHE'LL BE A " + h + " " + i + " OF MINE.")
turnPage()

print("BOOOOOOOOOOOO")
print("Oh, gods above, they hate it. Ah, well.")
turnPage()
print("Suddenly, the door of the tavern bursts open. An old man with wild, white hair crosses the threshold. There's a powerful energy about him, one you don't quite understand and don't quite care to.")
turnPage()
print("WHO WILL CLIMB THE MOUNTAIN?")
print("Oh gods he's looking right at you.")
turnPage()
print("WHAT? WHY? The townspeople are confused.")
print("I FEAR WE'VE LOST ANOTHER POOR FOOL TO THE DRAGON.")
print()
who = str(input("Ask him about it? Y/N")).upper()
if who == "N":
    print()
    print("The silence of the crowd seems to anger him. His voice begins to shake.")
    print("I NEED YOUR HELP. PLEASE.")
    print("It seems he isn't angry after all. Just extremely upset.")
    turnPage()
elif who == "Y":
    print()
    print("You ask him who it was.")
print("MY SON LEFT THREE DAYS AGO. HE HAS YET TO RETURN.")
turnPage()
print("IS THERE ANYONE WHO CAN BRING HIM HOME?")
print("The patrons murmur to each other, about dragons and lost causes and dead sons.")
answer = str(input("Will you volunteer? Y/N")).upper()
if answer == "Y":
    print()
    print("You step forward and proclaim that you'll find the man's son.")
    print("He is overjoyed.")
elif answer == "N":
    print()
    print("You pretend to be very interested in the mead-stain on the wall behind you.")
    turnPage()
    print(str(Ariel).upper() + " WILL DO IT!")
    print("Huh? You think a dissatisfied customer just volunteered you for a deadly mission.")
    turnPage()
    print("You try to protest, but it's too late. The man is overjoyed.")
    print("THANK YOU, THANK YOU SO MUCH, BRAVE BARD.")
    turnPage()
print("PLEASE, TAKE THIS. IT HAS MAGICAL PROPERTIES.")
print("He hands you a flute. You haven't played in a very long time.")
im = Image.open('flute.jpg')
im.show()
print("You have acquired a MAGIC FLUTE!")
turnPage()

print("Out into the world you go, armed with a magical flute and your own wits.")
turnPage()
what = str(input("Will you approach the mountain? Y/N")).upper()
if what == "Y":
    print()
    print("You decide to approach the mountain.")
elif what == "N":
    print()
    print("You don't want to go, but it would be kind of silly not to. You took the guy's flute, after all.")
    flute = str(input("Play your new flute? Y/N")).upper()
    if flute == "Y":
        play_obj = wave_objariel.play()
        print()
        print("You play a little tune. Looks like you've still got it.")
        turnPage()
        print("Well, you guess there's only one thing left to do now.")
    if flute == "N":
        print()
        print("Nah, you'll try it out later.")
turnPage()

print("You find your way to a well-traveled trail, and decide to take it.")
turnPage()
print("However, it doesn't last long. After about thirty minutes of hiking, the trail breaks off.")
print("At the place where the trail meets the wild forest, a young girl stands almost motionless.")
talk = str(input(("Talk to her? Y/N"))).upper()
while talk == "N":
    print()
    print("You stand there silently, and she doesn't look at you.")
    print("You're really starting to wonder what she's doing here.")
    talk = str(input(("Talk to her? Y/N"))).upper()
if talk == "Y":
    print()
    print("You ask her what she's looking at.")
    turnPage()
print("HELLO, " + Ariel.upper() + ".")
print("oh shit.")
turnPage()
question = str(input("A. Who are you? B. How do you know my name? C. What are you looking at?")).upper()
while question == "A" or question == "B" or question == "C":
    if question == "A":
        print()
        print("I AM THE SEER.")
        question = str(input("A. Who are you? B. How do you know my name? C. What are you looking at?")).upper()
    if question == "B":
        print()
        print("I'VE BEEN OVERSEEING YOUR QUEST.")
        question = str(input("A. Who are you? B. How do you know my name? C. What are you looking at?")).upper()
    if question == "C":
        print()
        print("YOUR FUTURE.")
        question = str(input("A. Who are you? B. How do you know my name? C. What are you looking at? D. exit")).upper()
if question != "A" and question != "B" and question != "C":
    print()
    print("The silence settles upon the two of you again, and it starts to get kind of awkward.")
    turnPage()
print(Ariel.upper() + ", WOULD YOU PLAY A GAME WITH ME?")
game = str(input("Play a game? Y/N")).upper()
while game == "N":
    print()
    print("OKAY. ALLOW ME TO REEVALUATE YOUR FUTURE.")
    turnPage()
    print("She takes a deep breath, closing her eyes. She opens them again almost immediately.")
    print("THAT'S NOT GOOD AT ALL.")
    turnPage()
    print("YOU NEED SOMETHING FROM ME TO COMPLETE YOUR QUEST. I CAN GIVE IT TO YOU.")
    print("BUT YOU HAVE TO HUMOR ME FIRST.")
    game = str(input("Play a game? Y/N")).upper()
if game == "Y":
    print()
    print("She smiles, and something about it is unsettling. But it's too late to turn back now.")
    turnPage()
    print("She holds out her hand. In it are two six-sided die.")
    print("TAKE ONE OF THESE. WE'LL EACH TAKE TURNS ROLLING UNTIL ONE OF US HITS THIRTY POINTS. BUT IF EITHER OF US ROLLS A 1, OUR SCORE GOES RIGHT BACK TO 0. YOU ALSO HAVE THE OPTION TO SKIP YOUR TURN IF YOU WANT TO.")
    ready = str(input("READY TO PLAY? Y/N")).upper()
    if ready == "N":
        print("TOO BAD! WE'RE STARTING!")
    elif ready == "Y":
        print("GREAT! LET'S BEGIN!")

#the game is Pig #https://en.m.wikipedia.org/wiki/Pig_(dice_game)

arieltotal = 0
seertotal = 0
while (int(arieltotal) < 30) and (int(seertotal) < 30):
    yourturn = str(input("Press Enter to roll, or X to skip your turn.")).upper()
    if yourturn != "X":
        roll = random.randint(1, 6)
        arieltotal += roll
        print("You rolled a " + str(roll) + ".")
        if (roll == 1) and (arieltotal == 1):
            print("Your score is still 0!")
        elif (roll == 1) and (arieltotal != 1):
            arieltotal = 0
            print("Your score went back to 0!")
        else:
            print("Your total score is " + str(arieltotal) + ".")
            if (arieltotal >= 30):
                print("You won!")
                win = arieltotal >= 30
        if (arieltotal < 30):
            herturn = str(input("Now wait for the Seer to roll. Press Enter."))
            seerschoice = random.randint(1,6)
            if (seerschoice < 3):
                print("The Seer skipped her turn. It's your turn now!")
            else:
                herroll = random.randint(1, 6)
                seertotal += herroll
                print("The Seer rolled a " + str(herroll) + ".")
                if (herroll == 1) and (seertotal != 1):
                    seertotal = 0
                    print("Her score went back to 0!")
                elif (herroll ==1) and (seertotal == 1):
                    print("Her score is still 0!")
                else:
                    print("Her total score is " + str(seertotal) + ".")
                    if (seertotal >= 30):
                        print("The Seer won!")
                        win = arieltotal >= 30
    else:
        herturn = str(input("Now wait for the Seer to roll. Press Enter."))
        seerschoice = random.randint(1,6)
        if (seerschoice < 3):
            print("The Seer skipped her turn. It's your turn now!")
        else:
            herroll = random.randint(1, 6)
            seertotal += herroll
            print("The Seer rolled a " + str(herroll) + ".")
            if (herroll == 1) and (seertotal != 0):
                seertotal = 0
                print("Her score went back to 0!")
            elif (herroll ==1) and (seertotal == 0):
                    print("Her score is still 0!")
            else:
                print("Her total score is " + str(seertotal) + ".")
                if (seertotal >= 30):
                    print("The Seer won!")
                    win = arieltotal >= 30

if win == False:
    print()
    print("LOOKS LIKE THIS IS THE END OF THE ROAD.")
    turnPage()
    print("GOODBYE, " + Ariel.upper() + ".")
    print(".....")
    print("....")
    print("...")
    print("..")
    print(".")
    sys.exit()
elif win == True:
    print()
    print("GOOD JOB, YOU'VE BEATEN ME.")
    print("LET'S HOPE YOU HAVE SIMILAR LUCK WITH RELIK.")
    whodat = str(input("A. Who's Relik? B. Let's hope so.")).upper()
    if whodat == "B":
        print()
        print("She nods, and steps aside to let you pass.")
    elif whodat == "A":
        print("WHY, THEY ARE THE DRAGON THAT INHABITS THIS LAND.")
        they = str(input("A. They? There's more than one? B. They? They are neither male nor female?"))
        print("NOT NECESSARILY. THEY WERE ONCE TWO, AND NOW THEY ARE... NOT.")
        turnPage()
        print("IT'S COMPLICATED.")
        ok = str(input("A. Okay! B. Okay. C. Okay..."))

print()
print("BEFORE YOU LEAVE, TAKE THESE. THEY'LL HELP YOU.")
print("The Seer holds out her hand again.")
turnPage()

im = Image.open('dice.jpg')
im.show()
print("You have acquired a pair of MAGIC DICE!")
turnPage()

print("As you get closer to the top of the mountain, you begin to notice the burned ground, the large streaks of charred earth that crisscross the landscape like scars. You're getting much closer to the home of the dragon, almost too close for comfort.")
turnPage()
print("This part of the mountain is very quiet; most of the wildlife has fled to safer lands. You hear no insects or birdcalls, but far in the distance, a human sound registered. It sounds like someone in pain.")
doyougo = str(input("Do you look for the source of the sound? Y/N")).upper()
while doyougo == "N":
    print()
    print("You try to ignore the noise, but as you get closer to your destination, it gets louder and closer.")
    doyougo = str(input("Do you look for the source of the sound? Y/N")).upper()
if doyougo == "Y":
    print()
    print("You seek out the human making the noise. You're in luck.")
turnPage()
print("You spot a knight on the ground, propped up against a boulder.")
sayhello = str(input("Do you approach him? Y/N")).upper()
if sayhello == "N":
    print()
    print("You freeze, hoping he won't see you. But you're too late to find a hiding place.")
    turnPage()
    print("He spots you through the slits in his helmet and pushes back his visor. His face is pallid, his expression desperate.")
    print("P-PLEASE HELP ME!")
elif sayhello == "Y":
    print()
    print("You call out to him. Weakly, he swings up his arm and pushes back his visor. His face is pale and tired.")
    print("IS S-SOMEONE THERE?")
turnPage()
print("You approach quickly and kneel beside him, examining the deep claw marks in his armor. Something raked through that steel like it was butter.")
whodidthis = str(input("A. Who did this to you? B. What is your name? C. I am going to defeat the dragon.")).upper()
while whodidthis == "A" or whodidthis == "B" or whodidthis == "C":
    if whodidthis == "A":
        print()
        print("THAT B-BEAST IN THE CAVE. I WAS S-SUCH A FOOL.")
        turnPage()
        print("You ask him if he fought the dragon, Relik.")
        turnPage()
        print("W-WHAT OTHER DRAGONS ARE THERE OUT HERE?")
        print("He seems to remember something, and lets out a shaky laugh.")
        turnPage()
        print("NO, IT WAS J-JUST THE ONE.")
        whodidthis = str(input("A. Who did this to you? B. What is your name? C. I am going to defeat the dragon.")).upper()
    if whodidthis == "B":
        print()
        print("MY NAME IS S-SEREN GRAYWOOD.")
        turnPage()
        print("He must be that man's son! You tell him.")
        turnPage()
        print("INDEED, I AM SOME MAN'S S-SON.")
        print("Well, you're at least a little bit certain he's the right guy.")
        whodidthis = str(input("A. Who did this to you? B. What is your name? C. I am going to defeat the dragon.")).upper()
    if whodidthis == "C":
        print()
        print("IT IS IMPOSSIBLE. WH-WHO ARE YOU, ANYWAY?")
        print("You tell him your name is " + Ariel.title() + " and you are a musician.")
        whodidthis = str(input("A. Who did this to you? B. What is your name? C. I am going to defeat the dragon. D. exit")).upper()
if whodidthis != "A" and whodidthis != "B" and whodidthis != "C":
    print()
    print("The knight coughs suddenly, and a trickle of blood runs from the corner of his mouth.")
    turnPage()
print(Ariel.upper() + ", PLEASE HELP ME.")
helphim = str(input("Will you help him? Y/N")).upper()
while helphim == "N":
    print()
    print("If you don't stop the bleeding, Seren will surely die.")
    helphim = str(input("Will you help him? Y/N")).upper()
if helphim == "Y":
    print()
print("You decide this is the right moment to pull out your magic flute. This man needs a song of healing.")
turnPage()
print("MY F-FATHER'S FLUTE. THAT W-WON'T WORK ON ME.")
print("You ask him, well, why not?")
turnPage()
print("TH-THIS ARMOR. IT'S RESISTANT TO M-MAGIC.")
print("But not to giant dragon claws, you point out.")
turnPage()
print("This makes him laugh again. It looks painful.")
print("Obviously your next move is to get this armor off so you can perform your song.")
turnPage()
print("As you fumble with the ruined chestplate, you can't quite see where the latch is, but you listen very carefully...")
print("shout = cold")
print("clang = warmer")
print("heartbeat = red hot!")

RECX = random.randint(1, 600)
RECY = random.randint(1,600)
RECWIDTH = 70
RECHEIGHT = 70
WINDOWX = RECX
WINDOWY = RECY
RECX2 = RECWIDTH + 150
RECY2 = RECHEIGHT + 150
RECX3 = RECWIDTH + 300
RECY3 = RECHEIGHT + 300

class DoubleClick(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(WINDOWX, WINDOWY, 600, 600)
        self.setWindowTitle('Double Click')
        self.__inside = False
        self.wave_obj = sa.WaveObject.from_wave_file('WilhelmScream.wav')
        self.wave_obj1 = sa.WaveObject.from_wave_file('ff7.wav')
        self.wave_obj2 = sa.WaveObject.from_wave_file('heartbeat.wav')
        self.wave_obj3 = sa.WaveObject.from_wave_file('sword.wav')
        self.show()

    def __inRect(self,x,y):
     	return (RECX<x<RECX+RECWIDTH and RECY<y<RECY+RECHEIGHT)

    def __inRect2(self, x, y):
        return ((RECX-50)<x<(RECX-50)+RECX2 and (RECY-50)<y<(RECY-50)+RECY2)

    def __inRect3(self, x, y):
        return ((RECX-100)<x<(RECX-100)+RECX3 and (RECY-100)<y<(RECY-100)+RECY3)

    def mouseDoubleClickEvent(self, event):
        self.__inside = False
        if(self.__inRect(event.x(),event.y())):
        	self.__inside = True
        if(self.__inside == True):
            self.play_obj = self.wave_obj1.play()
        elif(self.__inside == False and self.__inRect2(event.x(),event.y())):
            self.play_obj = self.wave_obj2.play()
        elif(self.__inside == False and self.__inRect3(event.x(),event.y())):
            self.play_obj = self.wave_obj3.play()
        else:
            self.play_obj = self.wave_obj.play()
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        grayPen = QPen(QBrush(Qt.gray),0.01)
        qp.setPen(grayPen)
        qp.drawRect(RECX,RECY,RECWIDTH,RECHEIGHT)
        qp.drawRect(RECX-50,RECY-50,RECX2,RECY2)
        qp.drawRect(RECX-100,RECY-100,RECX3,RECY3)
        if (self.__inside):
            textPen = QPen(QBrush(Qt.black),2)
            qp.setPen(textPen)
            qp.drawText(RECX, RECY, "GOT IT!")
        elif (not (self.__inside)):
            textPen = QPen(QBrush(Qt.red),3)
            qp.setPen(textPen)
            qp.drawText(5, 30, "Not quite!")
        qp.end()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = DoubleClick()
  app.exec_()

arielwin = 3

win = arielwin > 1
if win == False:
    print()
    print("You can't manage to find the latch.")
    print("There's no time to defeat the dragon today. You have to take Seren home.")
    print("GAME OVER.")
    sys.exit()
elif win == True:
    print()
    print("You remove Seren's chestplate, revealing the gaping wounds in his torso.")
    print("Then, you take out the flute and begin to play.")
    play_obj = wave_objseren.play()
    turnPage()
print("At first, it's just music. Then, slowly, the slashes begin to close, the skin knitting together again as if it had never been torn. Seren breathes a sigh of relief.")
turnPage()
print("TH-THANK YOU, " + Ariel.upper() + ".")
print("You finish your song, amazed at the flute's power.")
turnPage()
print("H-HOW CAN I REPAY YOU?")
reward = str(input("A. You can go home and let your father know you're safe. B. A weapon might be nice.")).upper()
if reward == "A":
    print()
    print("OF COURSE. B-BUT PLEASE, TAKE THIS AS WELL")
    print("M-MAYBE IT WILL DO YOU MORE G-GOOD THAN IT DID ME.")
elif reward == "B":
    print()
    print("OF COURSE. HERE, T-TAKE MY SWORD.")
    print("M-MAYBE IT WILL DO YOU MORE G-GOOD THAN IT DID ME.")
elif reward != "A" and reward != "B":
    print()
    print("You say nothing. Seren holds out his sword.")
    print("PLEASE, T-TAKE THIS. MAYBE IT WILL HELP YOU M-MORE THAN IT HELPED ME.")
im = Image.open('sword.jpg')
im.show()
print("You have acquired a MAGIC SWORD!")

print("You see Seren off, making sure he finds the path that will lead him back to Burning Rock, back to his father. Then, armed with your flute, dice, and sword, you approach the dragon's cave alone.")
turnPage()
print("Immediately, you see them, and you understand. They are a massive, golden beast with enormous talons and great scaly wings. They regard you coldly with eyes that glow like molten metal. However, you notice that their head is slightly off-center. On the other side of their broad shoulders is a terrible scar.")
turnPage()
print("BACK FOR MORE, HERO?")
reliktalk = str(input("A. I am not a hero. I am " + Ariel.title() + " and I am a musician B. What happened to your other head? C. I have come to defeat you.")).upper()
while reliktalk == "A" or reliktalk == "B" or reliktalk == "C" or reliktalk == "D":
    if reliktalk == "A":
        print()
        print("A BARD? YOU MUST BE JOKING.")
        print("To prove it, you take out your magic flute. Relik regards you with a toothy grin. You hear the sibilant sound of reptilian laughter from their remaining head.")
        turnPage()
        print("DON'T WASTE MY TIME, " + Ariel.upper() + ". PLAY YOUR MUSIC ELSEWHERE.")
        reliktalk = str(input("A. I am not a hero. I am " + Ariel.title() + " and I am a musician B. What happened to your other head? C. Please stop destroying the wildnerness. D. I have come to defeat you.")).upper()
    elif reliktalk == "B":
        print()
        print("I WAS DEFEATED BY THE HERO OF BURNING ROCK, MY OTHER HALF DESTOYED.")
        print("You remember hearing this story. In fact, you remember telling this story. Singing it, even.")
        turnPage()
        print("WE HAD NEVER HARMED A SOUL.")
        reliktalk = str(input("A. I am not a hero. I am " + Ariel.title() + " and I am a musician B. What happened to your other head? C. Please stop destroying the wildnerness. D. I have come to defeat you.")).upper()
    elif reliktalk == "C":
        print()
        print("I WILL NOT REST UNTIL THE HERO OF BURNING ROCK CHALLENGES ME AGAIN. EITHER SHE FINISHES THE JOB AND TAKES MY OTHER HEAD, OR I WILL TAKE HERS.")
        print("But the Hero of Burning Rock died years ago. You offer up this piece of history to Relik.")
        turnPage()
        print("VERY WELL. IF THE HERO WILL NOT SHOW HERSELF, THEN ALL OF BURNING ROCK WILL PAY FOR MY LONELINESS.")
        reliktalk = str(input("A. I am not a hero. I am " + Ariel.title() + " and I am a musician B. What happened to your other head? C. Please stop destroying the wildnerness. D. I have come to defeat you.")).upper()
    elif reliktalk == "D":
        print()
        print("IT WOULD BE MOST AMUSING TO SEE YOU TRY, BARD.")
        reliktalk = str(input("A. I am not a hero. I am " + Ariel.title() + " and I am a musician B. What happened to your other head? C. Please stop destroying the wildnerness. D. I have come to defeat you. E. exit")).upper()
if reliktalk != "A" and reliktalk != "B" and reliktalk != "C" and reliktalk != "D":
    print()
    print("Relik regards your silence as a challenge. They rise to their full height, and terrified as you are, you're beyond the point of no return.")

arielHP = 100
relikHP = 100
while (int(arielHP) > 0) and (int(relikHP) > 6):
    print()
    yourturn = str(input("Strike with: A. Flute B. Dice C. Sword")).upper()
    if yourturn == "A":
        music = random.randint(1, 6)
        relikHP -= music
        arielHP += music
        print("You play Relik a song on your magic flute. They take " + str(music) + " damage.")
        if (relikHP > 7):
            print("Relik's total HP is " + str(relikHP) + ".")
            print("Inspired by your musical talent, you regain " + str(music) + " HP.")
    elif yourturn == "B":
        roll = 2 * random.randint(1, 6)
        relikHP -= roll
        print("You roll your dice for a total of " + str(roll) + ".")
        print("Relik takes " + str(roll) + " damage.")
        if (relikHP > 7):
            print("Relik's total HP is " + str(relikHP) + ".")
    elif yourturn == "C":
        swordplay = random.randint (1,4)
        if (swordplay > 2):
            strike = random.randint(1,20)
            relikHP -= strike
            print("You swing your sword at Relik. It hits!")
            print("He takes " + str(strike) + " damage.")
            if (relikHP > 7):
                print("Relik's total HP is " + str(relikHP) + ".")
        else:
            print("You swing your sword at Relik. You miss!")
            print("Relik's total HP is still " + str(relikHP) + ".")
    elif yourturn != "A" or "B" or "C":
        print("You fumble with your weapons, not knowing which to choose. You're out of time!")
    if (relikHP > 7):
        print()
        histurn = str(input("It's Relik's turn to strike. Press Enter."))
        relikschoice = random.randint(1, 4)
        if (relikschoice == 1):
            bite = random.randint(1,6)
            arielHP -= bite
            print("Relik snaps at you with their fangs. You take " + str(bite) + " damage.")
            if (arielHP > 0):
                print("Your total HP is " + str(arielHP) + ".")
            elif (arielHP <= 0):
                print("You lost!")
                print("GOODBYE, " + Ariel.upper() + ".")
                print(".....")
                print("....")
                print("...")
                print("..")
                print(".")
                sys.exit()
        elif (relikschoice == 2):
            claw = 2 * random.randint(1, 6)
            arielHP -= claw
            print("Relik takes a swing at you with their claws. You take " + str(claw) + " damage.")
            if (arielHP > 0):
                print("Your total HP is " + str(arielHP) + ".")
            elif (arielHP <= 0):
                print("You lost!")
                print("GOODBYE, " + Ariel.upper() + ".")
                print(".....")
                print("....")
                print("...")
                print("..")
                print(".")
                sys.exit()
        elif (relikschoice > 2):
            flame = random.randint (1,4)
            if (flame > 2):
                firedamage = random.randint(1,20)
                arielHP -= firedamage
                print("Relik breathes fire at you. It burns!")
                print("You take " + str(firedamage) + " damage.")
                if (arielHP > 0):
                    print("Your total HP is " + str(arielHP) + ".")
                elif (arielHP <= 0):
                    print("You lost!")
                    print("GOODBYE, " + Ariel.upper() + ".")
                    print(".....")
                    print("....")
                    print("...")
                    print("..")
                    print(".")
                    sys.exit()
            else:
                print("Relik breathes fire at you, but you manage to dodge!")
                print("Your total HP is still " + str(arielHP) + ".")

relikHP = 2
while (int(relikHP) <= 6) and (int(arielHP) > 0):
    print()
    print("Relik hits the floor with a thud that shakes the walls of the cave.")
    approach = str(input("Approach them? Y/N")).upper()
    if approach == "N":
        print()
        print("You turn to leave the cave, but hear the dragon's voice behind you.")
    elif approach == "Y":
        print()
        print("You approach the once-mighty dragon. They regard you with one tired, golden eye.")
        turnPage()
    print("FINISH ME.")
    finishhim = str(input("Finish them? Y/N")).upper()
    if finishhim == "Y":
        print()
        print("You bring down your sword. The beast takes a shuddering breath and then is silent.")
        relikHP = 666
        print("Relik's HP is now 0 You have won.")
    elif finishhim == "N":
        print()
        print("You simply stare at them. The eye before you narrows.")
        turnPage()
        print("WHY AREN'T YOU DOING ANYTHING?")
        turnPage()
        print("JUST KILL US.")
        killhim = str(input("Kill them? Y/N")).upper()
        if killhim == "Y":
            print()
            print("You bring down your sword. The beast takes a shuddering breath and then is silent.")
            relikHP = 666
            print("Relik's HP is now 0. You have won.")
        elif killhim == "N":
            print()
            print("You reach for the weapons slung across your back...")
            print("FINALLY.")
            turnPage()
            print("...and pull out your magic flute.")
            turnPage()
            playsong = str(input("Play them a song? Y/N")).upper()
            while playsong == "N":
                print()
                print("You give Relik a whack with your flute. They look unimpressed.")
                playsong = str(input("Play them a song? Y/N")).upper()
            if playsong == "Y":
                print()
                print("You play Relik a song on your magic flute. It's lovely and sad.")
                play_obj = wave_objrelik.play()
                turnPage()
                print("As you play, the dragon regains HP, their wounds closing, the spark of life returning to their eyes.")
                turnPage()
                relikHP = 50
                print("When you're finished, Relik folds their claws on the ground in front of you.")
                print("With their chin resting on the floor, you are almost at eye-level.")
                turnPage()
                print("YOU HAVE SPARED US. WHY?")

answer = str(input("A. In exchange for my mercy, I want yours. B. You need not live half a life. C. Take this flute.")).upper()
while answer == "A" or answer == "B" or answer == "C":
    if answer == "A":
        print()
        print("You ask Relik to let you leave the cave safely, and to leave the mountain alone so that the wildlife may return.")
        answer = str(input("A. In exchange for my mercy, I want yours. B. You need not live half a life. C. Take this flute. D. exit")).upper()
    if answer == "B":
        print()
        print("You tell Relik that they are a most magnificent creature all on their own.")
        print("It may hurt to remember that they were once half of a pair, but nothing can be done.")
        answer = str(input("A. In exchange for my mercy, I want yours. B. You need not live half a life. C. Take this flute. D. exit")).upper()
    if answer == "C":
        print()
        print("You place your flute at their feet. You tell them it is a gift that heals. You hope it will help them heal, too.")
        answer = str(input("A. In exchange for my mercy, I want yours. B. You need not live half a life. C. Take this flute. D. exit")).upper()
if answer != "A" or answer != "B" or answer != "C":
    print()
    print("You give them a nod and take your leave of the cave.")
    print("You expect to be incinerated in a column of flame as you exit, but no fire comes.")
    turnPage()
    print("The mountain never burns again.")
    print(".....")
    print("....")
    print("...")
    print("..")
    print(".")
