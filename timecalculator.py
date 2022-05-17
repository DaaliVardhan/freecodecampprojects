#def add_time(start, duration):

def add_time(t1,t2,day=None):
    x=0
    i=0
    week=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    if day:
        i=week.index(day.lower())
        x=week.index(day.lower())

    t1=t1.split(" ")
    t1_hour=t1[0].split(":")[0]
    t1_minute=t1[0].split(":")[1]
    t1_id=t1[1]
    if t1_id=="PM":
        t1_hour=str(int(t1_hour)+12)
    
    #t2=t2.split(" ")
    t2_hour=t2.split(":")[0]
    t2_minute=t2.split(":")[1]

    time_hour=int(t1_hour)+int(t2_hour)
    time_minute=int(t1_minute)+int(t2_minute)
    if time_minute>=60:
        
        time_hour+=time_minute//60
        time_minute=time_minute%60
        
        
        if time_minute<10:
            time_minute="0"+str(time_minute)
        else:
            time_minute=str(time_minute)    
    else:
        if time_minute==0:
            time_minute="0"+str(time_minute)
        else:
            if time_minute<10:
              time_minute="0"+str(time_minute)
            else:
              time_minute=str(time_minute)
   
    id=t1_id
    if time_hour>=24:
        i=i+(time_hour//24)
        time_hour=time_hour%24
  
  
    if time_hour!=0:
        if time_hour<12:
            id="AM"
        else:
            id="PM"

        time_hour=str(time_hour%12)
        if time_hour=="0":
          time_hour="12"
    else:
        time_hour="12"
        id="AM"
        
    

 
    
    
    if day:
        if x==i:
            return (time_hour)+":"+time_minute+" "+id+", "+week[i%7].capitalize()
        elif x+1==i:
            return (time_hour)+":"+time_minute+" "+id+", "+week[i%7].capitalize()+" "+"(next day)"
        else:
            return (time_hour)+":"+time_minute+" "+id+", "+week[i%7].capitalize()+" "+f"({str(i-x)} days later)"
    else:
        if x==i:
            return (time_hour)+":"+time_minute+" "+id
        elif x+1==i:
            return (time_hour)+":"+time_minute+" "+id+" "+"(next day)"
        else:
            return str(time_hour)+":"+time_minute+" "+id+" "+f"({str(i-x)} days later)"

#print(addtime("6:30 PM", "205:12"))




    #return new_time