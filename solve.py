import sys
  
if __name__=="__main__":
  from pjeuler import *
  i = int(sys.argv[1])
  print("Solve ProjectEuler problem "+str(i)+".")
  val = -1
  if i==1:
    val = pjeuler1()
  elif i==2:
    val = pjeuler2()
  if val == -1:
    print("Solution not found.")
  else:
    print("Result is "+str(val)+".")
    
