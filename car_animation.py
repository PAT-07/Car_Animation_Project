from tkinter import*
import time
import pygame
import sys
import pygame
pygame.mixer.init()
#final 
#pygame.mixer.music.load("carsound.mp3")
#pygame.mixer.music.play()

master=Tk()

w=Canvas(master, width=1000, height=1000,bg="#33BEFF")
w.pack()

#background
def firstslide():
    
    line1=w.create_text(500,350,fill="white",font=("Times New Roman",50),text="sometimes")
    k=True
    a=500
    while k:
    
        w.move(line1,5,0)
        a=a+5
        master.update()
        time.sleep(0.02)
        if a>=1200:
            k=False
    secondslide()            
def secondslide():
    line2=w.create_text(280,350,fill="white",font=("Times New Roman",30),text="sometimes,you need a car in \nyour trip to a new country...")

    image1=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image1.PNG')
    airport=w.create_image(500,150,image=image1,anchor=NW)

    xspeed1=5#speed of first img
    xspeed2=-0.04#speed of line2
    k2=True
    b=500
   
    while k2:
            w.move(line2,xspeed2,0)
            pos2=w.coords(line2)
            if pos2[0]<=276:
                xspeed2=-50
                
            w.move(airport,xspeed1,0)
            b=b+5
            pos1=w.coords(airport)
            if pos1[0]>=630:
                xspeed1=0.1
                if pos1[0]>=635:
                    xspeed1=100
                master.update()
                time.sleep(0.05)
            

            if b>=960:
                thirdslide()
                break
                
            if b>1250:
                k2=False
   
           
def thirdslide():
    image2=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image2.PNG')
    photoimage2=w.create_image(600,200,image=image2,anchor=NW)
    xspeed1=5#speed img
    k3=True
    c=500
    w.create_polygon(10,300,500,300,500,400,10,400,fill="#33BEFF")
    line2=w.create_text(280,350,fill="white",font=("Times New Roman",30),text="sometimes,you need a car in \nyour trip to a new country...")
    xspeed2=-0.04#speed of line2
    while k3:
            w.move(line2,xspeed2,0)
            pos2=w.coords(line2)
            if pos2[0]<=276.5:
                xspeed2=-100
            
            w.move(photoimage2,xspeed1,0)
            c=c+5
            pos2=w.coords(photoimage2)
            if pos2[0]>=630:
                xspeed1=0.2
                if pos2[0]>=645:
                    
                    xspeed1=100
                master.update()
                time.sleep(0.05)

            if c>=1000:
                fourthslide()
                break
                
            if c>1250:
                k3=False
            

def fourthslide():
    

    image3=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image3.PNG')
    photoimage3=w.create_image(200,250,image=image3,anchor=NW)

    xspeed1=-5#speed of first img
    
    k4=True
    d=500
   
    while k4:
           
            w.move(photoimage3,xspeed1,0)
            d=d+5
            pos1=w.coords(photoimage3)
            if pos1[0]<=70:
                xspeed1=-0.1
                if pos1[0]<=65:
                    xspeed1=-100
                master.update()
                time.sleep(0.05)



            if d>=1000:
                fifthslide()
                break
                
            if d>1250:
                k4=False

def fifthslide():
    line3=w.create_text(440,120,fill="white",font=("Times New Roman",30),text="sometimes,you need a bigger car in your land trip ")

    image4=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image4.PNG')
    photoimage4=w.create_image(30,50,image=image4,anchor=NW)

    yspeed1=5#img speed
    yspeed2=0.04#speed of line2
    k2=True
    b=500
   
    while k2:
            w.move(line3,0,yspeed2)
            pos2=w.coords(line3)
            if pos2[1]>=123.5:
                yspeed2=40
                
            w.move(photoimage4,0,yspeed1)
            b=b+5
            pos1=w.coords(photoimage4)
            if pos1[1]>=250:
                yspeed1=0.1
                if pos1[1]>=255:
                    yspeed1=100
                master.update()
                time.sleep(0.05)


            if b>=1100:
                sixthslide()
                break
                
            if b>1250:
                k2=False

def sixthslide():
    image5=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image5.PNG')
    photoimage5=w.create_image(200,250,image=image5,anchor=NW)

    xspeed1=-5#speed of first img
    
    k4=True
    d=500
   
    while k4:
           
            w.move(photoimage5,xspeed1,0)
            d=d+5
            pos1=w.coords(photoimage5)
            if pos1[0]<=70:
                xspeed1=-0.1
                if pos1[0]<=65:
                    xspeed1=-100
                master.update()
                time.sleep(0.05)     

            if d>=1000:
                seventhslide()
                break
                
            if d>1250:
                k4=False

def seventhslide():
    t=True
    line2=w.create_text(440,100,fill="white",font=("Times New Roman",30),text="sometimes,you need a special car for your business")
    xspeed2=0.04#speed of line2

    image6=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image6.PNG')
    photoimage6=w.create_image(50,300,image=image6,anchor=NW)

    xspeed1=0.5#speed img
    k3=True
    c=510
    d=510
    xspeed6=-20#speed of client
    while t:
            w.move(line2,xspeed2,0)
            pos2=w.coords(line2)
            if pos2[0]>=450.5:
                xspeed2=80
            
            w.move(photoimage6,xspeed1,0)
            
            pos2=w.coords(photoimage6)
            if pos2[0]>=70:
                xspeed1=0.2
                if pos2[0]>=80:
                    xspeed1=1000
                    if pos2[0]>=770:
                       image6b=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image6b.PNG')
                       photoimage6b=w.create_image(80,300,image=image6b,anchor=NW)

                       image6c=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image6c.PNG')
                       photoimage6c=w.create_image(500,350,image=image6c,anchor=NW)

                       image6d=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image6d.PNG')
                       photoimage6d=w.create_image(1000,350,image=image6d,anchor=NW)

                       if pos2[0]>=9000:
                           
                           while t:
                               w.move(photoimage6d,xspeed6,0)
                               pos6=w.coords(photoimage6d)
                               if pos6[0]<=630:
                                   xspeed6=-0.01
                                   if pos6[0]<=629:
                                       xspeed6=0.01
                                       time.sleep(1)
                                       w.move(photoimage6c,1000,0)
                                       w.move(photoimage6d,1000,0)

                                       image6e=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image6e.PNG')
                                       photoimage6e=w.create_image(520,350,image=image6e,anchor=NW)
                                       
                                     
                                       t=True
                                       x1=100
                                       y1=800
                                       x2=200
                                       y2=900
                                       
                                       while t:
                                            for i in range(1):
                                                w.create_oval(x1,y1,x2,y2,fill="#33BEFF",outline="deep sky blue")
                                                x1-=5
                                                y1-=5
                                                x2+=5
                                                y2+=5
                                                c+=5
                                                d+=5
                                                master.update()
                                                time.sleep(0.00005)
                                            if x2>=1250:
                                                t=False
                                          
                               master.update()
                               time.sleep(0.05)
                               
                               
                
                master.update()
                time.sleep(0.05)
          
            
    eighthslide()
                
            
         
def eighthslide():
    
    image7=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image7.PNG')
    photoimage7=w.create_image(200,250,image=image7,anchor=NW)

    xspeed1=-5#speed of first img
    
    k4=True
    d=500
   
    while k4:
           
            w.move(photoimage7,xspeed1,0)
            d=d+5
            pos1=w.coords(photoimage7)
            if pos1[0]<=80:
                xspeed1=-0.1
                if pos1[0]<=77:
                    xspeed1=-1000
                master.update()
                time.sleep(0.05)



            if d>=960:
                ninethslide()
                break
                
            if d>1250:
                k4=False

def ninethslide():
    line3=w.create_text(440,120,fill="white",font=("Times New Roman",30),text="sometimes,you need a stronger car in your long trip ")

    image7b=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image7b.PNG')
    photoimage7b=w.create_image(30,50,image=image7b,anchor=NW)

    yspeed1=9#img speed
    yspeed2=0.04#speed of line2
    k2=True
    b=500
   
    while k2:
            w.move(line3,0,yspeed2)
            pos2=w.coords(line3)
            if pos2[1]>=122:
                yspeed2=80
                
            w.move(photoimage7b,0,yspeed1)
            b=b+5
            pos1=w.coords(photoimage7b)
            if pos1[1]>=230:
                yspeed1=0.1
                if pos1[1]>=233:
                    yspeed1=100
                master.update()
                time.sleep(0.05)

            if b==1100:
                tenthslide()
                #time.sleep(10)
                #sys.exit()
                
            if b>1250:
                k2=False


def tenthslide():
    t=True
    line2=w.create_text(440,100,fill="white",font=("Times New Roman",30),text="sometimes,you need a prettier car for your love..")
    xspeed2=0.04#speed of line2

    image8=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image8.PNG')
    photoimage8=w.create_image(70,300,image=image8,anchor=NW)

    xspeed1=0.9#speed img
    k3=True
    c=510
    d=510
    xspeed8e=-15#speed of couple
    while t:
            w.move(line2,xspeed2,0)
            pos2=w.coords(line2)
            if pos2[0]>=450.5:
                xspeed2=80
            
            w.move(photoimage8,xspeed1,0)
            c=c+5
            pos2=w.coords(photoimage8)
            if pos2[0]>=70:
                xspeed1=0.2
                if pos2[0]>=73:
                    xspeed1=1000
                    if pos2[0]>=770:
                       image8b=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image8b.PNG')
                       photoimage8b=w.create_image(80,330,image=image8b,anchor=NW)

                       image8c=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image8c.PNG')
                       photoimage8c=w.create_image(370,380,image=image8c,anchor=NW)
                       if pos2[0]>=9000:
                        
                           xspeed8c=15#speed of person
                           while t:
                               w.move(photoimage8c,xspeed8c,0)
                               pos8c=w.coords(photoimage8c)
                               if pos8c[0]>=385:
                                   xspeed8c=20
                                   if pos8c[0]>=1200:
                                       w.move(photoimage8b,1000,0)

                                       image8d=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image8d.PNG')
                                       photoimage8d=w.create_image(80,320,image=image8d,anchor=NW)

                                       image8e=PhotoImage(file='C:\\Users\\praty\\OneDrive\\Desktop\\Tkinter\\image8e.PNG')
                                       photoimage8e=w.create_image(1200,323,image=image8e,anchor=NW)
                                       pos8e=w.coords(photoimage8e)
                                      
                                   if pos8c[0]>=1300:
                                       while t:
                                           w.move(photoimage8e,xspeed8e,0)
                                           pos8e=w.coords(photoimage8e)
                                           if pos8e[0]<=479:
                                                xspeed8e=0.01
                                           
                                                
                                                x1=500
                                                y1=300
                                                x2=510
                                                y2=310
                                                while t:
                                                    for i in range(1):
                                                        w.create_oval(x1,y1,x2,y2,fill="palegreen3",outline="deep sky blue")
                                                        x1-=20
                                                        y1-=20
                                                        x2+=20
                                                        y2+=20
                                                        c+=25
                                                        d+=25
                                                        master.update()
                                                        time.sleep(0.03)
                                                        if x2>=1250:
                                                            t=False
                                                  
                                                 
                                                        master.update()
                                                        time.sleep(0.05)

                                           master.update()
                                           time.sleep(0.05)
                               master.update()
                               time.sleep(0.05)
                master.update()
                time.sleep(0.05)
            if c>=1250:
                t=False
                
            if c>=1190:
                eleventhslide()
                
      
                
def eleventhslide():
    line=w.create_text(450,130,fill="blue4",text="There is a solution for every need",font=("Times",40))
    
    line=w.create_text(470,230,fill="white",text="EUROPCAR",font=("arial",80,"bold"))
   
    w.create_polygon(40,330,920,330,460,290,fill="yellow",smooth="True")
    line=w.create_text(450,400,text="Moving          way",fill="white",font=("Times",34))
    line=w.create_text(480,400,text="your",fill="yellow",font=("Times",34))
    t=True
    
    while t:                     
            x1=1200
            y1=1100
            x2=1400
            y2=1300
            while t:
                
                for i in range(1):
                    w.create_oval(x1,y1,x2,y2,fill="gold",outline="palegreen3")
                    x1-=8
                    y1-=8
                    x2+=8
                    y2+=8
                   
                    master.update()
                    time.sleep(0.0008)
                if x2>=3150:
                    t=False
            if x2>=2500:
                line=w.create_text(490,200,fill="blue4",text="EUROPCAR",font=("arial",80,"bold"))
                line=w.create_text(480,330,text="Car Rental in Italy ",fill="purple1",font=("Times",40))
                line=w.create_text(480,400,text="www.europcar.in",fill="blue4",font=("Times",40))
                line=w.create_text(480,460,text="Mob: 9821883478",fill="blue4",font=("Times",30))
                line=w.create_text(480,500,text="Tel: 9178956432",fill="blue4",font=("Times",30))
            
                break;
                #sys.exit()
                
           
#def twelthslide():
firstslide()
