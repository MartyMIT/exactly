###################################
### Exactly - with Dan Lassiter ###
###################################

#Import
import pygame, random, csv
from pygame.locals import*
pygame.font.init()
pygame.init()

#Geometry
W,H=850,850
res=(W,H)
cposW=W/2
cposH=H/2
cpos=W/2,H/2
radius=8

#Range of values for `n'
num=[7]
#num=[6,7,8]

#Output
manip='exactly'
name=raw_input("Subject: ")
age=raw_input("Age: ")
sexe=raw_input("Gender (M/F): ")
blind=raw_input("Color blindness (Y/N): ")
data_directory='data'
output_file = data_directory + '/' + manip + '_' + name + '.txt'
out = open(output_file, 'at')
print >>out, "Sujet Age Gender Blind Block Essai Structure Nombre_X Identifiable Colored_dots Couleur_cible Couleur_filler Nombre_caseN Couleurcible_caseN Nombre_caseS Couleurcible_caseS Nombre_caseE Couleurcible_caseE Nombre_caseO Couleurcible_caseO Distance Expected_value Condition Response Response_time"

#Instructions
#instru_1='instru_1.jpg'
#instru_2='instru_2.jpg'

#Areas
z=3.5
area=(W/z,H/z,W-2*W/z,H-2*H/z)
cposareaW=area[2]/2
cposareaH=area[3]/2
x=3.5
subareaW=area[2]/x
subareaH=area[3]/x
y=10
caseN=(cposareaW-subareaW/2,cposareaH/y,subareaW,subareaH)
caseS=(cposareaW-subareaW/2,cposareaH+(cposareaH-cposareaH/y-subareaH),subareaW,subareaH)
caseE=(cposareaW/y,cposareaH-subareaH/2,subareaW,subareaH)
caseO=(cposareaW+(cposareaW-cposareaW/y-subareaW),cposareaH-subareaH/2,subareaW,subareaH)
dicearea=(0,0,subareaW,subareaH)
z=4
answerarea=(W/z,H-H/4,W-2*W/z,H/12)
answerbar=(answerarea[0]+answerarea[2]/20,answerarea[1]+answerarea[3]/5,answerarea[2]-2*answerarea[2]/20,answerarea[3]-3*answerarea[3]/4)
right=answerbar[0]+answerbar[2]
left=answerbar[0]

#Colors
black=(0,0,0)
white=(255,255,255)
grey=(211,211,211)
darkgrey=(102,102,102)
red=(205, 38, 38) 
blue=(92,172,238)
yellow=(238,201,0)
green=(34,139,34)
purple=(154,50,205) 
orange=(255,165,0) 
bg=white
fg=black
targetcolors=["red","blue","black"]
fillercolors=["red","blue","black","yellow","green"]

#Font
style="Arial"
pts1=32
pts2=25

#Durations
durblank=1000

#Dictionaries
dots_dic={"0":[0],"1":[5],"2":[3,7],"3":[3,5,7],"4":[1,3,7,9],"5":[1,3,5,7,9],"6":[1,3,4,6,7,9]}

options={
    "6":{
        "6":[(3,3),(4,2),(5,1),(2,2,2),(4,1,1)],
        "7":[(4,3),(5,2),(3,3,1),(4,2,1)],
        "8":[(4,4),(5,3),(6,2),(3,3,2),(4,3,1),(4,2,2)],
        "9":[(4,5),(6,3),(3,3,3),(4,3,2)]
        },
    "7":{
        "6":[(3,3),(4,2),(5,1),(2,2,2),(4,1,1)],
        "7":[(3,4),(5,2),(6,1),(3,2,2),(5,1,1)],
        "8":[(4,4),(6,2),(5,3),(3,3,2),(4,2,2)],
        "9":[(5,4),(6,3),(3,3,3),(4,3,2),(5,2,2)],
        "10":[(5,5),(6,4),(3,4,3),(4,4,2)]
        },
      "8":{
        "6":[(3,3),(4,2),(5,1),(2,2,2),(4,1,1)],
        "7":[(3,4),(5,2),(6,1),(3,2,2),(5,1,1)],
        "8":[(4,4),(6,2),(5,3),(3,3,2),(4,2,2)],
        "9":[(5,4),(6,3),(3,3,3),(4,3,2),(5,2,2)],
        "10":[(5,5),(6,4),(3,4,3),(4,4,2)],
        "11":[(6,5),(3,3,5),(4,3,4),(6,4,1)]
        }
        }


#Functions
def item(sentence_item):
    items=[]
    for modifier in ["exactly", "less-than", "more-than", "no-less-than", "no-more-than"]:
        for n in num:
            if modifier=="exactly":
                for i in [n-3,n-2,n-1,n,n,n,n+3,n+2,n+1,n+3,n+2,n+1]: #range(n-3,n+4)
                    ITEM ={"modifier":modifier,
                           "numeral":n,
                           "colored_dots":i,
                           "group_dots":"NA"}
                    picture_item(ITEM)
                    sentence_item(ITEM)
                    items.append(ITEM)
            else:
                for i in [n-3,n-2,n-1,n,n+3,n+2,n+1]:
                    ITEM ={"modifier":modifier,
                           "numeral":n,
                           "colored_dots":i,
                           "group_dots":"NA"}
                    picture_item(ITEM)
                    sentence_item(ITEM)
                    items.append(ITEM)
    return items

def item2(sentence_item):
    items=[]
    for modifier in ["only1", "only2"]:
        for n in num:
            for i in [n,n,n,n+3,n+2,n+1]:
                ITEM ={"modifier":modifier,
                       "numeral":n,
                       "colored_dots":i,
                       "group_dots":"NA"}
                picture_item(ITEM)
                sentence_item(ITEM)
                items.append(ITEM)
    return items

def picture_item(ITEM):
    #COLORS
    targetcolor=random.choice(targetcolors)
    fillercolors.remove(targetcolor)
    fillercolor=random.choice(fillercolors)
    fillercolors.append(targetcolor)
    
    #DICE
    dice=["caseN","caseS","caseO","caseE"]
    random.shuffle(dice)
    ITEM["picture"]={"target_color":targetcolor,
                    "filler_color":fillercolor,
                    dice[0]:{"dots":random.randint(1,6), "target_color":0},
                    dice[1]:{"dots":random.randint(1,6), "target_color":0},
                    dice[2]:{"dots":random.randint(1,6), "target_color":0},
                    dice[3]:{"dots":random.randint(1,6), "target_color":0}
                    }
        
    #GROUP NOT AVAILABLE
    if ITEM["colored_dots"] < 6:
        ITEM["picture"][dice[0]]["dots"] = ITEM["colored_dots"]
        ITEM["picture"][dice[0]]["target_color"] = 1
        
    #elif ITEM["colored_dots"] >= ITEM["numeral"]:
    else:
        option=random.choice(options[str(ITEM["numeral"])][str(ITEM["colored_dots"])])
        for x in range(len(option)):
            ITEM["picture"][dice[x]]["dots"]=option[x]
            ITEM["picture"][dice[x]]["target_color"]=1

def phrase_item1(ITEM):
    if ITEM["modifier"]=="exactly":
        sentence="Exactly "+str(ITEM["numeral"])+" dots are "+ITEM["picture"]["target_color"]+"." 
    elif ITEM["modifier"]=="less-than":
        sentence="Less than "+str(ITEM["numeral"])+" dots are "+ITEM["picture"]["target_color"]+"."
    elif ITEM["modifier"]=="more-than":
        sentence="More than "+str(ITEM["numeral"])+" dots are "+ITEM["picture"]["target_color"]+"."
    elif ITEM["modifier"]=="no-less-than":
        sentence="No less than "+str(ITEM["numeral"])+" dots are "+ITEM["picture"]["target_color"]+"."
    elif ITEM["modifier"]=="no-more-than":
        sentence="No more than "+str(ITEM["numeral"])+" dots are "+ITEM["picture"]["target_color"]+"."
    ITEM["sentence"]=sentence

def phrase_item2(ITEM):
    if ITEM["modifier"]=="exactly":
        sentence="The number of "+ITEM["picture"]["target_color"]+" dots is exactly "+str(ITEM["numeral"])+"."
    elif ITEM["modifier"]=="less-than":
        sentence="The number of "+ITEM["picture"]["target_color"]+" dots is less than "+str(ITEM["numeral"])+"."
    elif ITEM["modifier"]=="more-than":
        sentence="The number of "+ITEM["picture"]["target_color"]+" dots is more than "+str(ITEM["numeral"])+"."
    elif ITEM["modifier"]=="no-less-than":
        sentence="The number of "+ITEM["picture"]["target_color"]+" dots is no less than "+str(ITEM["numeral"])+"."
    elif ITEM["modifier"]=="no-more-than":
        sentence="The number of "+ITEM["picture"]["target_color"]+" dots is no more than "+str(ITEM["numeral"])+"."
    ITEM["sentence"]=sentence

def phrase_item3(ITEM):
    if ITEM["modifier"]=="only1":
        sentence="Only "+str(ITEM["numeral"])+" dots are "+ITEM["picture"]["target_color"]+"." 
    elif ITEM["modifier"]=="only2":
        sentence="The number of "+ITEM["picture"]["target_color"]+" dots is only "+str(ITEM["numeral"])+"."
    ITEM["sentence"]=sentence


def draw(ITEM):
    #DISPLAY SENTENCE
    police=pygame.font.SysFont(style, pts1)
    surf_text=police.render(ITEM["sentence"], 1, fg)
    textP=surf_text.get_rect()
    textP.center=[cposW, H/4]
    surf.fill(bg)
    surf.blit(surf_text,textP)

    #DISPLAY BACKGROUND
    answerareasubsurf=surf.subsurface(answerarea)
    pygame.draw.rect(surf, grey, answerarea,1)
    answerareasubsurf.fill(grey)
    p=15
    pol=pygame.font.SysFont(style, pts2)
    answer_no=pol.render("False", 1, fg)
    answer_yes=pol.render("True", 1, fg)
    no=answer_no.get_rect()
    yes=answer_yes.get_rect()
    no.center=[(answerarea[0]+answerarea[2]/p),(answerarea[1]+2*answerarea[3]/3)]
    yes.center=[(answerarea[0]+answerarea[2]-answerarea[2]/p),(answerarea[1]+2*answerarea[3]/3)]
    surf.blit(answer_no,no)
    surf.blit(answer_yes,yes)
    surfbar=surf.subsurface(answerbar)
    pygame.draw.rect(surf,red, answerbar,1)

    #DISPLAY DICE
    subsurf=surf.subsurface(area)
    pygame.draw.rect(surf, fg, area,3)
    pygame.draw.rect(subsurf, fg, caseN,2)
    pygame.draw.rect(subsurf, fg, caseS,2)
    pygame.draw.rect(subsurf, fg, caseE,2)
    pygame.draw.rect(subsurf, fg, caseO,2)
    caseNsurf=subsurf.subsurface(caseN)
    caseSsurf=subsurf.subsurface(caseS)
    caseEsurf=subsurf.subsurface(caseE)
    caseOsurf=subsurf.subsurface(caseO)
    surf_dico={"caseN":caseNsurf,"caseS":caseSsurf,"caseE":caseEsurf,"caseO":caseOsurf}

    #DRAW DOTS
    for x in ["N","S","E","O"]:
        if ITEM["picture"]["case"+x]["target_color"]==0: color=couleur(ITEM["picture"]["filler_color"])
        else: color=couleur(ITEM["picture"]["target_color"])
        surface=surf_dico["case"+x]
        for i in dots_dic[str(ITEM["picture"]["case"+x]["dots"])]:
            x=dicearea[2]/4+((i-1)%3)*(dicearea[2]/4)
            y=dicearea[3]/4+((i-1)/3)*(dicearea[3]/4)
            coord_i=(int(x),int(y))
            pygame.draw.circle(surface,color,coord_i,radius)

    #GRADUAL MEASURES
    mouse=pygame.mouse.get_pos()
    fin=mouse[0]
    if mouse[0] >= right:
            fin=right
    elif mouse[0] <= left:
            fin=left
    barre=(answerbar[0],answerbar[1],fin-answerbar[0],answerbar[3])
    surfevaluation=surf.subsurface(barre)
    pygame.draw.rect(surfevaluation,red, barre,1)
    surfevaluation.fill(red)


def play(ITEM):
    response=0
    rt=0
    no_response_yet=True
    t0=pygame.time.get_ticks()
    while no_response_yet==True:
        draw(ITEM)
        pygame.display.flip()
        for ev in pygame.event.get():           
            if ev.type == KEYDOWN and ev.key == K_ESCAPE:
                pygame.quit()
                out.close()
            elif ev.type == MOUSEBUTTONDOWN:
                rt=pygame.time.get_ticks() - t0
                m=pygame.mouse.get_pos()
                if m[0] >= right: response=100
                elif m[0] <= left: response=0
                elif left<m[0]<right: response=float(m[0]-answerbar[0])/float(answerbar[2])*100
                no_response_yet=False
    return response,rt


def couleur(X):
    Y=0
    if X == "red":
        Y=red
    elif X == "blue":
        Y=blue
    elif X == "yellow":
        Y=yellow
    elif X == "green":
        Y=green
    elif X == "purple":
        Y=purple
    elif X == "orange":
        Y=orange
    elif X == "black":
        Y=black
    elif X == "grey":
        Y=darkgrey  
    return Y


def blank(X):
    pygame.mouse.set_visible(False)
    surf.fill(bg)
    pygame.display.flip()
    pygame.time.wait(X)
    pygame.mouse.set_visible(True)


def procedure(X):
    pygame.mouse.set_visible(False)
    instruction=True
    image=pygame.image.load(X)
    imagepos=image.get_rect()
    imagepos.center=[cposW, cposH]
    surf.blit(image,imagepos)
    pygame.display.flip()
    while instruction==True:
        for ev in pygame.event.get():
            pygame.event.clear()       
            if ev.type==KEYDOWN:
                if ev.key==K_SPACE:
                    instruction=False
                    pygame.mouse.set_visible(True)

    
def displaytext(surf, police, bg, fg, pos, text):
    t = police.render(text, 1, fg)
    textpos = t.get_rect()
    textpos.centerx, textpos.centery= pos
    surf.blit(t, textpos)


def display_instructions(d1, d2, d3):
    pygame.mouse.set_visible(False)
    done = False
    while not done:
        police=pygame.font.SysFont("Arial", 36) # police instructions
        surf.fill(bg)
        displaytext(surf, police, bg, fg, (W/2, H/2 - 120), d1)
        displaytext(surf, police, bg, fg, (W/2, H/2), d2)
        displaytext(surf, police, bg, fg, (W/2, H/2 + 120), d3)
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type==KEYDOWN and ev.key == K_SPACE:
                done = True
                pygame.mouse.set_visible(True)

def data(ITEM):
    #PROPRETIES OF SENTENCES AND PICTURES
    modifier=ITEM["modifier"]
    numeral=ITEM["numeral"]
    group=ITEM["group_dots"]
    colored_dots=ITEM["colored_dots"]
    couleur_cible=ITEM["picture"]["target_color"]
    couleur_filler=ITEM["picture"]["filler_color"]
    nombre_caseN=ITEM["picture"]["caseN"]["dots"]
    couleurcible_caseN=ITEM["picture"]["caseN"]["target_color"]
    nombre_caseS=ITEM["picture"]["caseS"]["dots"]
    couleurcible_caseS=ITEM["picture"]["caseS"]["target_color"]
    nombre_caseE=ITEM["picture"]["caseE"]["dots"]
    couleurcible_caseE=ITEM["picture"]["caseE"]["target_color"]
    nombre_caseO=ITEM["picture"]["caseO"]["dots"]
    couleurcible_caseO=ITEM["picture"]["caseO"]["target_color"]

    #DISTANCE AND TRUTH-VALUE
    distance=colored_dots - numeral
    condition="None"
    if distance < 0: condition="Inferior"
    elif distance==0: condition="Equal"
    elif distance > 0:condition="Superior"

    expected_value="None"
    if modifier=="exactly":
        if distance < 0:expected_value="FALSE" 
        elif distance==0:expected_value="TRUE"
        elif distance > 0:expected_value="?"
    elif modifier=="less-than":
        if distance >= 0:expected_value="FALSE"
        else:expected_value="TRUE" 
    elif modifier=="more-than":
        if distance <= 0:expected_value="FALSE"
        else:expected_value="TRUE"
    elif modifier=="no-less-than":
        if distance >= 0:expected_value="TRUE"
        else:expected_value="FALSE"
    elif modifier=="no-more-than":
        if distance <= 0:expected_value="TRUE"
        else:expected_value="FALSE"
    elif modifier in ["only1","only2"]:
        if distance==0:expected_value="TRUE"
        else:expected_value="FALSE"
        
    return modifier, numeral, group, colored_dots, couleur_cible, couleur_filler, nombre_caseN, couleurcible_caseN, nombre_caseS, couleurcible_caseS, nombre_caseE, couleurcible_caseE, nombre_caseO, couleurcible_caseO, distance, expected_value, condition    
       
def experiment(ITEM,BLOCK):
    trial=0
    random.shuffle(ITEM)
    for i in ITEM:
        X=play(i)
        Y=data(i)
        trial +=1
        print >>out,name,age,sexe, blind, BLOCK,trial,Y[0],Y[1],Y[2],Y[3],Y[4],Y[5],Y[6],Y[7],Y[8],Y[9],Y[10],Y[11],Y[12],Y[13],Y[14],Y[15],Y[16], X[0],X[1]
                                                
try:
    mode=pygame.FULLSCREEN
    surf=pygame.display.set_mode((res), mode)
    
    '''
    Instructions
    '''
#    procedure(instru_1)
#    procedure(instru_2)
    
    '''
    BLOC 1: Exactly n As are Bs.
    '''
    stim=item(phrase_item1)
    block=1
    d1="Part I"
    d2="          "
    d3="Press Spacebar to start the experiment"
    display_instructions(d1,d2,d3)
    experiment(stim,block)

    '''
    BLOC 2: The number of ABs is exactly n.
    '''
    stim=item(phrase_item2)
    block=2
    d1="Part II"
    d2="          "
    d3="Press Spacebar to continue"
    display_instructions(d1,d2,d3)
    experiment(stim,block)

    '''
    BLOC 3: Only (in progress)
    '''
    stim=item2(phrase_item3)
    block=3
    d1="Part III"
    d2="A few more trials..."
    d3="Press Spacebar to continue"
    display_instructions(d1,d2,d3)
    experiment(stim,block)
    
    '''
    THANKS
    '''
    d1="The experiment is now finished."
    d2="Thanks again for participating in this study!"
    d3="Press Spacebar to quit"
    display_instructions(d1, d2, d3)
    
finally:
    pygame.quit()
    out.close()
