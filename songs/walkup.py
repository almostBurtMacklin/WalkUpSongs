from tkinter import *
from tkinter import ttk
import os

globala = int(0)
jos = globala
eli = globala
cal = globala
cha = globala
bla = globala
rew = globala
owe = globala
log = globala
tyl = globala
ben = globala
fer = globala
jef = globala
ian = globala
bur = globala
bri = globala
hol = globala
job = globala
nel = globala
noa = globala
hom = globala
vis = globala



window= Tk()

##root = Tk()
##photo = PhotoImage(file = 'F:/ panther.jpg')
##w = Label(root, image=photo)
##w.pack()
##ent = Entry(root)
##ent.pack()
##ent.focus_set() 

#filename = PhotoImage(file = 'IMG_4211')
window.title("KCC Baseball Walk Up Songs")
window.geometry('890x400')
window['background'] = 'royal blue'
#background_label = Label(top, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

nb = ttk.Notebook(window)
nb.grid(column=1, row=0) #, columnspan = 100, rowspan= 100, sticky='NESW')

s = ttk.Style()
s.configure('.', font=('Helvetica', 12), background = 'white')

page1 = ttk.Frame(nb)
nb.add(page1, text= 'Walk up Songs Varsity')


page2 = ttk.Frame(nb)
nb.add(page2, text= 'Pre-Game')

page3 = ttk.Frame(nb)
nb.add(page3, text= 'Walk Up Songs JV')

#lbl = Label(window, text="KCC BASEBALL", padx=1, pady=1)
#lbl.grid(column=0 , row=1)
#lbl['background'] = '#ffffff'

def btn1():
   global eli
   songsEli = ['BoomBoom_Empty.wav', 'OppositeOfAdults.wav' , 'Swerv.wav']
   if eli == 0:
            os.system("start ./songs/" + songsEli[eli] +" ")
            eli = int(eli + 1)
   elif eli == 1:
            os.system("start ./songs/"  + songsEli[eli] +" ")
            eli = int(eli + 1)
   elif eli == 2:
            os.system("start ./songs/"  + songsEli[eli] +" ")
            eli = 0

btn1 = Button(page1, text= "0", command = btn1, height = 2, width = 5, bd= 5, bg = 'gold' )
btn1.grid(column=1, row=2, padx=5, pady=5)


def btn2():
   global jos
   songsJos = [ 'AllTheAbove.wav' , 'HOF.wav' , 'Fabolous.wav' ]
   if jos == 0:
            os.system("start ./songs/" + songsJos[jos] +" ")
            jos = int(jos + 1)
   elif jos == 1:
            os.system("start ./songs/" + songsJos[jos] +" ")
            jos = int(jos + 1)
   elif jos == 2:
            os.system("start ./songs/" + songsJos[jos] +" ")
            jos = 0    
            
btn2 = Button(page1, text= "1", command = btn2 , height = 2, width = 5, bd= 5, bg = 'gold' )
btn2.grid(column=2, row=2, padx=5, pady=5)


def btn3():
   global cal
   songsCal = ['Marmalade.wav' , 'LoveYouBetter.wav', 'Ways.wav' ]
   if cal == 0:
            os.system("start ./songs/" + songsCal[cal] +" ")
            cal = int(cal + 1)
   elif cal == 1:
            os.system("start ./songs/" + songsCal[cal] +" ")
            cal = int(cal + 1)
   elif cal == 2:
            os.system("start ./songs/" + songsCal[cal] +" ")
            cal = 0       
            
btn3 = Button(page1, text= "3", command = btn3 , height = 2, width = 5, bd= 5, bg = 'gold' )
btn3.grid(column=3, row=2, padx=5, pady=5)

def btn4():
   global cha
   songsCha = ['SpaceJam.wav' , 'Super.wav', 'Spanish.wav' ]
   if cha == 0:
            os.system("start ./songs/" + songsCha[cha] +" ")
            cha = int(cha + 1)
   elif cha == 1:
            os.system("start ./songs/" + songsCha[cha] +" ")
            cha = int(cha + 1)
   elif cha == 2:
            os.system("start ./songs/" + songsCha[cha] +" ")
            cha = 0
            
btn4 = Button(page1, text= "4", command = btn4, height = 2, width = 5, bd= 5, bg = 'gold' )
btn4.grid(column=4, row=2 , padx=5, pady=5)



def btn5():
   global bla
   songsBla = ['ateam.wav' , 'skywalker.wav', 'goosebumps.wav' ]
   if bla == 0:
            os.system("start ./songs/" + songsBla[bla] +" ")
            bla = int(bla + 1)
   elif bla == 1:
            os.system("start ./songs/" + songsBla[bla] +" ")
            bla = int(bla + 1)
   elif bla == 2:
            os.system("start ./songs/" + songsBla[bla] +" ")
            bla = 0
btn5 = Button(page1, text= "5", command = btn5, height = 2, width = 5, bd= 5, bg = 'gold' )
btn5.grid(column=5, row=2, padx=5, pady=5)



def btn6():
   global jef
   songsJef = ['sandstorm.wav' , 'Stole.wav', 'mortalkombat.wav' ]
   if jef == 0:
            os.system("start ./songs/" + songsJef[jef] +" ")
            jef = int(jef + 1)
   elif jef == 1:
            os.system("start ./songs/" + songsJef[jef] +" ")
            jef = int(jef + 1)
   elif jef == 2:
            os.system("start ./songs/" + songsJef[jef] +" ")
            jef = 0
btn6 = Button(page1, text= "6", command = btn6, height = 2, width = 5, bd= 5, bg = 'gold' )
btn6.grid(column=6, row=2, padx=5, pady=5)


def btn7():
   os.system("start ./songs/WhateverItTakes.wav")
   
btn7 = Button(page1, text= "7", command = btn7, height = 2, width = 5, bd= 5, bg = 'gold' )
btn7.grid(column=7, row=2, padx=5, pady=5)


def btn8():
   global owe
   songsOwe = ['WavinFlag.wav' , 'Fortnite.wav' ]
   if owe == 0:
            os.system("start ./songs/" + songsOwe[owe] +" ")
            owe = int(owe + 1)
   elif owe == 1:
            os.system("start ./songs/" + songsOwe[owe] +" ")
            owe = 0
            
btn8 = Button(page1, text= "8", command = btn8, height = 2, width = 5, bd= 5, bg = 'gold' )
btn8.grid(column=8, row=2, padx=5, pady=5)


def btn9():
   global log
   songsLog = ['NoGood.wav', 'WantYou.wav' , 'StayinAlive.wav' ]
   if log == 0:
            os.system("start ./songs/" + songsLog[log] +" ")
            log = int(log + 1)
   elif log == 1:
            os.system("start ./songs/" + songsLog[log] +" ")
            log = int(log + 1)
   elif log == 2:
            os.system("start ./songs/" + songsLog[log] +" ")
            log = 0 
btn9 = Button(page1, text= "9", command = btn9, height = 2, width = 5, bd= 5, bg = 'gold' )
btn9.grid(column=9, row=2, padx=5, pady=5)


def btn10():
   os.system("start ./songs/Congratulations.wav")
btn10 = Button(page1, text= "10", command = btn10, height = 2, width = 5, bd= 5, bg = 'gold' )
btn10.grid(column=10, row=2, padx=5, pady=5)


def btn11():
   global fer
   songsFer = ['Godsplan.wav' , 'primetime.wav','MansNotHot.wav' ]
   if fer == 0:
            os.system("start ./songs/" + songsFer[fer] +" ")
            fer = int(fer + 1)
   elif fer == 1:
            os.system("start ./songs/" + songsFer[fer] +" ")
            fer = int(fer + 1)
   elif fer == 2:
            os.system("start ./songs/" + songsFer[fer] +" ")
            fer = 0
btn11 = Button(page1, text= "11", command = btn11 , height = 2, width = 5, bd= 5, bg = 'gold' )
btn11.grid(column=11, row=2 , padx=5, pady=5)


def btn12():
   global bur
   songsBur = ['MayWeAll.wav' , 'X.wav', 'DeadOrAlive.wav' ]
   if bur == 0:
            os.system("start ./songs/" + songsBur[bur] +" ")
            bur = int(bur + 1)
   elif bur == 1:
            os.system("start ./songs/" + songsBur[bur] +" ")
            bur = int(bur + 1)
   elif bur == 2:
            os.system("start ./songs/" + songsBur[bur] +" ")
            bur = 0
btn12 = Button(page1, text= "12", command = btn12, height = 2, width = 5, bd= 5, bg = 'gold' )
btn12.grid(column=12, row=2, padx=5, pady=5)


def btn13():
   global bri
   songsBri = [  'lights.wav', 'slow.wav','congratulations.wav' ]
   if bri == 0:
            os.system("start ./songs/" + songsBri[bri] +" ")
            bri = int(bri + 1)
   elif bri == 1:
            os.system("start ./songs/" + songsBri[bri] +" ")
            bri = int(bri + 1)
   elif bri == 2:
            os.system("start ./songs/" + songsBri[bri] +" ")
            bri = 0
btn13 = Button(page1, text= "17", command = btn13, height = 2, width = 5, bd= 5, bg = 'gold' )
btn13.grid(column=1, row=3, padx=5, pady=5)


def btn14():
   global hol
   songsHol = ['hookedOnAFelling.wav' , 'HitItHard.wav', 'AnitNoMountain.wav' ]
   if hol == 0:
            os.system("start ./songs/" + songsHol[hol] +" ")
            hol = int(hol + 1)
   elif hol == 1:
            os.system("start ./songs/" + songsHol[hol] +" ")
            hol = int(hol + 1)
   elif hol == 2:
            os.system("start ./songs/" + songsHol[hol] +" ")
            hol = 0
btn14 = Button(page1, text= "24", command = btn14 , height = 2, width = 5, bd= 5, bg = 'gold' )
btn14.grid(column=2, row=3, padx=5, pady=5)

def btn15():
   global job
   songsJob = ['comewith.wav','Forever.wav' , 'Portland.wav'  ]
   if job == 0:
            os.system("start ./songs/" + songsJob[job] +" ")
            job = int(job + 1)
   elif job == 1:
            os.system("start ./songs/" + songsJob[job] +" ")
            job = int(job + 1)
   elif job == 2:
            os.system("start ./songs/" + songsJob[job] +" ")
            job = 0
            
btn15 = Button(page1, text= "27", command = btn15 , height = 2, width = 5, bd= 5, bg = 'gold' )
btn15.grid(column=3, row=3, padx=5, pady=5)

def btn16():
   global nel
   songsNel = ['NONAME.wav' , 'Destiny.wav', 'WeBeenHere.wav' ]
   if nel == 0:
            os.system("start ./songs/" + songsNel[nel] +" ")
            nel = int(nel + 1)
   elif nel == 1:
            os.system("start ./songs/" + songsNel[nel] +" ")
            nel = int(nel + 1)
   elif nel == 2:
            os.system("start ./songs/" + songsNel[nel] +" ")
            nel = 0
            
btn16 = Button(page1, text= "29", command = btn16 , height = 2, width = 5, bd= 5, bg = 'gold' )
btn16.grid(column=4, row=3, padx=5, pady=5)

def btn17():
   global noa
   songsNoa = ['Laso.wav' , 'Enough.wav', 'Element.wav' ]
   if noa == 0:
            os.system("start ./songs/" + songsNoa[noa] +" ")
            noa = int(noa + 1)
   elif noa == 1:
            os.system("start ./songs/" + songsNoa[noa] +" ")
            noa = int(noa + 1)
   elif noa == 2:
            os.system("start ./songs/" + songsNoa[noa] +" ")
            noa = 0
            
btn17 = Button(page1, text= "32", command = btn17 , height = 2, width = 5, bd= 5, bg = 'gold' )
btn17.grid(column=5, row=3, padx=5, pady=5)

#def btn18():  
   #os.system("start ./songs/AllNight.wav") 
#btn18 = Button(page1, text= "18", command = btn18 , height = 2, width = 5, bd= 5, bg = 'gold' )
#btn18.grid(column=6, row=3, padx=5, pady=5)

#def btn19():
   #global jos
   #songsJos = [ 'AllTheAbove.wav' , 'HOF.wav' , 'Fabolous.wav' ]
   #if jos == 0:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 1:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 2:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = 0    
            
#btn19 = Button(page1, text= "19", command = btn19 , height = 2, width = 5, bd= 5, bg = 'gold' )
#btn19.grid(column=7, row=3, padx=5, pady=5)


#def btn20():
   #global jos
   #songsJos = [ 'AllTheAbove.wav' , 'HOF.wav' , 'Fabolous.wav' ]
   #if jos == 0:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 1:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 2:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = 0    
            
#btn20 = Button(page1, text= "20", command = btn20 , height = 2, width = 5, bd= 5, bg = 'gold' )
#btn20.grid(column=8, row=3, padx=5, pady=5)

#def btn21():
   #global jos
   #songsJos = [ 'AllTheAbove.wav' , 'HOF.wav' , 'Fabolous.wav' ]
   #if jos == 0:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 1:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 2:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = 0    
            
#btn21 = Button(page1, text= "21", command = btn21 , height = 2, width = 5, bd= 5, bg = 'gold' )
#btn21.grid(column=9, row=3, padx=5, pady=5)

#def btn22():
   #global jos
   #songsJos = [ 'AllTheAbove.wav' , 'HOF.wav' , 'Fabolous.wav' ]
   #if jos == 0:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 1:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 2:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = 0    
            
#btn22 = Button(page1, text= "22", command = btn22 , height = 2, width = 5, bd= 5, bg = 'gold' )
#btn22.grid(column=10, row=3, padx=5, pady=5)

#def btn23():
   #global jos
   #songsJos = [ 'AllTheAbove.wav' , 'HOF.wav' , 'Fabolous.wav' ]
   #if jos == 0:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 1:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 2:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = 0    
            
#btn23 = Button(page1, text= "23", command = btn23 , height = 2, width = 5, bd= 5, bg = 'gold' )
#btn23.grid(column=11, row=3, padx=5, pady=5)

#def btn24():
   #global jos
   #songsJos = [ 'AllTheAbove.wav' , 'HOF.wav' , 'Fabolous.wav' ]
   #if jos == 0:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 1:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = int(jos + 1)
   #elif jos == 2:
            #os.system("start ./songs/" + songsJos[jos] +" ")
            #jos = 0    
            
#btn24 = Button(page1, text= "24", command = btn24 , height = 2, width = 5, bd= 5, bg = 'gold' )
#btn24.grid(column=12, row=3, padx=5, pady=5)

#def btn1():
   #os.system("start ./songs/MLBonFOXFullTheme.mp3")   
#btn1 = Button(page2, text= "INTROS", command = btn1, height = 2, width = 25, bd= 5, bg = 'gold' )
#btn1.grid(column=1, row=1, padx=5, pady=5)

def btn2():
   os.system("start ./songs/star.mp3")   
btn2 = Button(page2, text= "Star Spanangled Banner", command = btn2, height = 2, width = 25, bd= 5, bg = 'gold' )
btn2.grid(column=2, row=1, padx=5, pady=5)

def btn3():
   os.system("start ./songs/WeReadyPreGameRumble.mp3")   
btn3 = Button(page2, text= "Pre-Game", command = btn3, height = 2, width = 25, bd= 5, bg = 'gold' )
btn3.grid(column=3, row=1, padx=5, pady=5)


def btn4():
   global hom
   songsHom = ['homerunsong.mp3' , 'homerunlock.wav', 'goosebumps.wav' ]
   if hom == 0:
      os.system("start ./songs/" + songsHom[hom] +" ")
      hom = int(hom + 1)
   elif hom == 1:
      os.system("start ./songs/" + songsHom[hom] +" ")
      hom = int(0)  
btn4 = Button(page2, text= "Home Run", command = btn4, height = 2, width = 25, bd= 5, bg = 'gold' )
btn4.grid(column=4, row=1, padx=5, pady=5)

def btn5():
   global vis
   songsVis = ['littleless.wav' , 'nobody.wav', 'jeopardy.mp3' ]
   if vis == 0:
            os.system("start ./songs/" + songsVis[vis] +" ")
            vis = int(vis + 1)
   elif vis == 1:
            os.system("start ./songs/" + songsVis[vis] +" ")
            vis = int(vis + 1)
   elif vis == 2:
            os.system("start ./songs/" + songsVis[vis] +" ")
            vis = 0
btn5 = Button(page2, text= "Mound Visit", command = btn5, height = 2, width = 25, bd= 5, bg = 'gold' )
btn5.grid(column=1, row=2, padx=5, pady=5)

def btn6():
   os.system("start ./songs/Locksley.mp3")
btn6 = Button(page2, text= "Panthers Win!!", command = btn6, height = 2, width = 25, bd= 5, bg = 'gold' )
btn6.grid(column=2, row=2, padx=5, pady=5)

def btn7():
   os.system("start ./songs/Locksley.mp3")
btn7 = Button(page2, text= "4th Inning Song", command = btn7, height = 2, width = 25, bd= 5, bg = 'gold' )
btn7.grid(column=3, row=2, padx=5, pady=5)

def btn8():
   os.system("start ./songs/Locksley.mp3")
btn8 = Button(page2, text= "Top 7th Inning Song", command = btn8, height = 2, width = 25, bd= 5, bg = 'gold' )
btn8.grid(column=4, row=2, padx=5, pady=5)

def btn9():
   os.system("start ./songs/canyoufeelit7thInning.mp3")
btn9 = Button(page2, text= "Comeback Song", command = btn9, height = 2, width = 25, bd= 5, bg = 'gold' )
btn9.grid(column=1, row=3, padx=5, pady=5)


window.mainloop()

