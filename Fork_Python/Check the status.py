def check_status(a, b, flag):
   if (flag==False and a>0 and not (b>0) or (flag==False and b>0 and not (a>0)) or (flag==True and a<0 and b<0)):
       return True
   else :
       return False
