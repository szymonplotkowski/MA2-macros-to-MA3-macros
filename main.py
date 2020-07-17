import xml.dom.minidom
import os
from ma3macro_lib import MA3Macro

filename = 'ma2 macros.xml'

doc = xml.dom.minidom.parse(filename)
ma2macros = doc.getElementsByTagName("Macro")
try:
    os.makedirs('ma3macros')
except OSError as e:
    pass
cwd=os.getcwd()
new_cwd=cwd+'/ma3macros'
print(new_cwd)
os.chdir(new_cwd)
for macro in ma2macros:
        name = macro.getAttribute("name")
        macrolines = macro.getElementsByTagName("text")
        print('Creating file '+name+'.xml containing macro '+name)
        filename = name+'.xml'
        Object = MA3Macro(filename, name)

        for node in macrolines:
            string = node.childNodes
            for node in string:
                line = node.nodeValue
                print('Adding line: '+line)
                Object.macro_line(line)
        Object.macro_end()
        Object.close_file()
