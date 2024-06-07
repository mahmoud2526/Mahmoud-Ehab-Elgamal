from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
total_time=0
breaker=1
sec=00
break_count=0
rights=""
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
cont=0
cond=0
#windo
num=0
window=Tk()
def sorce():
    global num,cond,breaker,cont
    if cont==0 :
        if num==0 or num%2==0 and num%8!=0 :

            cont=1
            cond=0
            breaker=0
            window.after(1000,count_Down,1)
        elif num%2!=0 and cont==0:

            cont=1
            cond=0
            breaker=0
            window.after(1000,count_Down,1)
            cont=1

        elif num%8==0 and cont==0:

            breaker=0
            window.after(1000,count_Down,2)



def count_Down(minn):
    global num,sec,cond,min,total_time,breaker,cont,rights
    total_time=minn
    if cond==0:
     min=minn
     cond=1
     cont=1
     breaker=1
    else:
        pass
    if breaker==1 and cont==1:
        window.after(1000,count_Down,minn)

        canva.itemconfig(timer,text=f"{min}:{sec}")

        if sec!=0 or min!=0:
                if sec==0:
                    min=min-1
                    sec=59
                else:
                    sec=sec-1
        if sec==0 and min==0:
            num+=1
            cond=0
            cont=0
            breaker=0
            if num==0 or num%2==0 and num%8!=0 :


                text_place.itemconfig(text,text="Timer")
            elif num%2!=0 and cont==0:


                text_place.itemconfig(text,text="Break")
                rights+="✔"
                lable.config(text=rights)
            elif num%8==0 and cont==0:

                rights+=""
                lable.config(text=rights)
                text_place.itemconfig(text,text="Long")


"""def breaks():
    global min,sec,breaker,break_count
    breaker=1
    if break_count<4:
        min=1
        sec=0
    else:
        min=15
    text_place.itemconfig(text,text="Break")
    window.after(1000,count_Down)
    canva.itemconfig(timer,text=f"{min}:{sec}")
    if sec!=0 or min!=0:
            if sec==0:
                min=min-1
                sec=59
            else:
                sec=sec-1
    if sec==0 and min==0:
        count_Down()
        break_count+=1
        print(break_count)
        rights[break_count-1]="✔"""

def reset_timer():
    global min,sec,breaker,total_time,cond,cont
    min=total_time
    sec=0
    cont=0
    cond=1
    breaker=0
    canva.itemconfig(timer,text=f"{min}:{sec}")



window.config(bg=YELLOW)
window.title("Pomodoro")
window.minsize(600,500)
window.maxsize(600,500)
#canva image
canva=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
photo=PhotoImage(file="tomato.png")
image_phot=canva.create_image(100,112,image=photo)
#timer
timer=canva.create_text(102,132,fill="white",text=f"00:00",font=(FONT_NAME,24,"bold"))


#text place
text_place=Canvas(width=200,height=50,bg=YELLOW,highlightthickness=0)
text=text_place.create_text(100,35,text="Timer",font=(FONT_NAME,40,"bold"),fill=GREEN)
#buttons
start=Button(window,text="Start",bg=GREEN,border=0.5,fg="red",width=6
             ,font=(FONT_NAME,14),command=sorce)
reset=Button(window,text="Reset",bg=GREEN,border=0.5,fg="red",width=6
             ,font=(FONT_NAME,14),command=reset_timer)
#lable
lable=Label(window,text=rights,fg=GREEN,font=(FONT_NAME,20),bg=YELLOW)

#place
canva.place(x=200,y=(500-300)/2)
text_place.place(x=200,y=30)
start.place(x=100,y=400)
reset.place(x=425,y=400)
lable.place(x=275,y=400)
window.mainloop()
