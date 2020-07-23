# MA2 macros to MA3 macros
 Python script that reads MA2 xml macrofile and spits directory full of MA3 ready macro files.
 

HOW TO:\
-Download whole repo and unzip.\
-Put XML file with Your macros in script folder.\
-Rename XML File to 'ma2 macros.xml'\
-Run script (*.exe or main.py)\
-Enjoy Your new directory 'ma3macros' full of new files

KNOWN ISSUES:\
-Macronames that contains characters illegal for filenames (ex. < >) causes crash.\
 Workaround: open 'ma2 macros.xml' with some file editor and batch-change that chars for something different.

FAQ:\
Q: Why its returning multiple files instead of one?\
A: For now MA3 is not capable to import 'multiple macros' file.

Q: Is it magical tool that will rewrite whole logic of my complex macros and repair things that are not implemented?\
A: No... its not. It will cut all the macros to single files and reparse 'old' MA2 xml to new MA3 xml format. Its just stupid tool that takes old macroline and pack it to format readable for new console. If some comands/syntax is not implemented or are changed in MA3 then You have to find workaround for yourself.
