from zipfile import *

f=ZipFile('images.zip','w',ZIP_DEFLATED)

f.write('1.jpeg')
f.write('2.jpeg')
f.write('3.jpeg')
f.write('4.jpeg')
f.write('5.jpeg')

f.close()
f.close()
f.close()
f.close()
f.close()