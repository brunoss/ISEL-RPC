# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v07
# ===============================

#original
def f( a_list ):
   a_list = [ str( x ).upper() for x in a_list ]
   while True:
      v = input( '? > ' )
      if v.upper() in a_list or v == 'quit' or v == 'exit': break
      print( v.upper() )

#a)
def g_1( a_list ):
#Oh Snap! I cheated by changing two lines of code! The original list input is more useful than converting all elements to string
   while True:
      v = input( '? > ' )
      if len([n for n in a_list if isinstance(n, int) and n % 2 == 0]) != 0 or v == 'quit' or v == 'exit': 
          break
      print( v.upper() )

#b)
#this is is silly and not any different from the original

#5b)
def average(aList):
    return sum(aList) / len(aList)

if __name__ == "__main__":
   a_list = [ 'o', 1, 33, 'hello' ]
   print(a_list)
   g_1(a_list)
   a_list.append(2)
   print(a_list)
   g_1(a_list)
   
print( "ANOTHER LINE IN THE END!" )


def g( x ):
   if x % 2 == 0: print( "EVEN" )
   else: print( "ODD" )

