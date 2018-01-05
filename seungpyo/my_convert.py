import os
from os import walk, getcwd
from PIL import Image
classes = ["Car", "Back"]

def num2filename(n):
  if n in range(1, 10):
    return '000'+str(n)
  elif n in range(10, 100):
    return '00'+str(n)
  elif n in range(100, 1000):
    return '0'+str(n)
  else:
    return str(n)


def generateXML(n, bbox):

  xml = ''
  xml += '''
<annotation>
	<folder>Car1</folder>
	<filename>'''
  xml += num2filename(n) + '.jpg</filename>\n'
  xml += '''
<size>
	<width>320</width>
	<height>240</height>
	<depth>1</depth>
</size>
<segmented>0</segmented>
<object>
	<name>Car</name>
	<pose>Left</pose>
	<truncated>1</truncated>
	<difficult>0</difficult>
	<bndbox>\n
'''
  xml += '		<xmin>'+str(bbox[0])+'</xmin>\n'
  xml += '		<ymin>'+str(bbox[1])+'</ymin>\n'
  xml += '		<xmax>'+str(bbox[0]+bbox[2])+'</xmax>\n'
  xml += '		<ymax>'+str(bbox[1]+bbox[3])+'</ymax>\n'
  xml += '''
	</bndbox>
	</object>
</annotation>
'''


  return xml


size = [320, 240]
with open('groundtruth_rect.txt') as f:
  for i, line in enumerate(f):
    line_vec = line.split(',')
    line_vec = [int(a) for a in line_vec]
    g = open('ann/'+num2filename(i+1)+'.xml', 'a')
    g.write(generateXML(i+1, line_vec))
    g.close()

 



   #WRITE LINE_VEC TO EACH TXT FILE CORRESPONDING TO IMG FILE
