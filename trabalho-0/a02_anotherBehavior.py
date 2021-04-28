# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v07
# ===============================

#_______________________________________________________________________________
# The modules to be evaluated
import os
import a01_aFunction as aF

print()
#calls function f of the imported module of the previous exercise
aF.f( [ 'x', 4 ] )
print()

name_f = 'a01_aFunction.py'

#a) opens the file a01_aFunction and prints the list of all lines. each element of the list is a line on the file.

# read a file
f_in = open( name_f )
lineList = f_in.readlines()
f_in.close()
print( lineList )
print()

#b) iterate the "lineList" structrure and print each line
for line in lineList:
    print(line, end="")

### ITEM-A
### add another line (statememt) to the end of the file
lineList += [ 'print( "ANOTHER LINE IN THE END!" )', '\n' ]
f_out = open( name_f, 'w' )
f_out.writelines( lineList )
f_out.close()

### ITEM-B
### executar o novo ficheiro (via 'shell' do sistema operativo)
print()
#os.system( "my_python " + name_f )
# if you do not need to provide a specific python interpreter, the use:
os.system( name_f )
print()

#d) o script a01_aFunction é executado com a mudança feita no ITEM-A
#e) Eu fiz o exercicio d no powershell. No cmd o resultado é o mesmo

### ITEM-C
### append a new function to the file (in case it does not yet exists)
newFunction = \
"""
def g( x ):
   if x % 2 == 0: print( "EVEN" )
   else: print( "ODD" )
"""
if 'def g( x ):' + '\n' not in lineList:
   lineList += [ '\n', newFunction, '\n' ]
   f_out = open( name_f, 'w' )
   f_out.writelines( lineList )
   f_out.close()

#a) uncommented
#b) 


### ITEM-D
### import again the file (now with function g)
m = __import__( name_f.replace( ".py", "" ) )
# it is important to "reload" in order to update the space of names
import imp
imp.reload( m )
# now, invoke the new function (that was appended to "name_f")
m.g( 33 )
###
### THE-END


print(m.average([2, 3, 4]))




