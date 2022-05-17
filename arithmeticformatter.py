def arithmetic_arranger(problems,args=False):
  if len(problems)>5:
    return "Error: Too many problems."
  first=""
  second=""
  third=""
  fourth=""
  arr=[]
  for i in problems:
    arr.append(i.split(" "))     
  for i in range(len(arr)):
    print(arr[i][1])
    if (arr[i][1]=="+" or arr[i][1]=="-"):
      
    
      gap=max(len(arr[i][0]),len(arr[i][2]))
      if gap>4:
        return "Error: Numbers cannot be more than four digits."
      else:
        
        first+=arr[i][0].rjust(gap+2)
        second+=arr[i][1]+" "+arr[i][2].rjust(gap)
        third+="-"*(gap+2)
        try:
          fourth+=str(eval(problems[i])).rjust(gap+2)
        except:
          return "Error: Numbers must only contain digits."
        
        if i==len(arr)-1:
          first+="\n"
          second+="\n"
          if args==True:
            third+="\n"
          
          #fourth+="\n"
        else:
          first+="    "
          second+="    "
          third+="    "
          fourth+="    "
      if args==False:
        arranged_problems=first+second+third
      else:
        arranged_problems=first+second+third+fourth
    else:
      return "Error: Operator must be '+' or '-'."
    
  

  return arranged_problems

    