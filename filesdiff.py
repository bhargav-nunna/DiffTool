#Author: Bhargav Nunna
#filesdiff.py
#contact for more info bhargav.vmf33@gmail.com

import math
import sys
import xml.etree.cElementTree as ET

file1=str(sys.argv[1])
file2=str(sys.argv[2])

path1=[ ]
name1=[ ]
hash1=[ ]
size1=[ ]
sigorg1=[ ]
sigcntime1=[ ]
sigexptime1=[ ]

tree1 = ET.ElementTree(file=file1)
root1 = tree1.getroot()

for child in root1:
	name1.append(child[0].text)
	path1.append(child[1].text)
	hash1.append(child[2].text)
	size1.append(child[3].text)
	if(child[-1].tag=='signature'):
		sigorg1.append(child[4][0].text)
		sigcntime1.append(child[4][1].text)
		sigexptime1.append(child[4][1].text)
	else:
		sigorg1.append('0')
		sigcntime1.append('0')
		sigexptime1.append('0')

path2=[ ]
name2=[ ]
hash2=[ ]
size2=[ ]
sigorg2=[ ]
sigcntime2=[ ]
sigexptime2=[ ]

tree2 = ET.ElementTree(file=file2)
root2 = tree2.getroot()

for child in root2:
	name2.append(child[0].text)
	path2.append(child[1].text)
	hash2.append(child[2].text)
	size2.append(child[3].text)
	if(child[-1].tag=='signature'):
		sigorg2.append(child[4][0].text)
		sigcntime2.append(child[4][2].text)
		sigexptime2.append(child[4][2].text)
	else:
		sigorg2.append('0')
		sigcntime2.append('0')
		sigexptime2.append('0')

i=len(path1)
j=len(path2)

target=open('diffout.xml','w')
target.write('<contents>')

for m in range(i):
	found=0
	for n in range(j):
		if(path1[m]==path2[n]):
			found=1
			if(size1[m]!= size2[n]):
				target.write('<file diff="changed">')
			else:
				target.write('<file diff="none">')
			target.write('<name>'+name1[m]+'</name>')
			target.write('<path>'+path1[m]+'</path>')
			target.write('<hash>'+hash1[m]+'</hash>')
			target.write('<size>'+size1[m]+'</size>')
			if(sigorg1[m]!='0'):
				target.write('<organization>'+str(sigorg1[m])+'</organization>')
				target.write('<countertime>'+str(sigcntime1[m])+'</countertime>')
				target.write('<expiration>'+str(sigexptime1[m])+'</expiration>')
			target.write('</file>')
	if(found==0):
		target.write('<file diff="added">')
		target.write('<name>'+name1[m]+'</name>')
		target.write('<path>'+path1[m]+'</path>')
		target.write('<hash>'+hash1[m]+'</hash>')
		target.write('<size>'+size1[m]+'</size>')
		if(sigorg1[m]!='0'):
			target.write('<organization>'+str(sigorg1[m])+'</organization>')
			target.write('<countertime>'+str(sigcntime1[m])+'</countertime>')
			target.write('<expiration>'+str(sigexptime1[m])+'</expiration>')
		target.write('</file>')


for m in range(j):
	found=0
	for n in range(i):
		if(path2[m]==path1[n]):
			found=1
	if(found==0):
		target.write('<file diff="deleted">')
		target.write('<name>'+name2[m]+'</name>')
		target.write('<path>'+path2[m]+'</path>')
		target.write('<hash>'+hash2[m]+'</hash>')
		target.write('<size>'+size2[m]+'</size>')
		if(sigorg2[m]!='0'):
			target.write('<organization>'+str(sigorg2[m])+'</organization>')
			target.write('<countertime>'+str(sigcntime2[m])+'</countertime>')
			target.write('<expiration>'+str(sigexptime2[m])+'</expiration>')
		target.write('</file>')

target.write('</contents>')

target.close()