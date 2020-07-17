
class MA3Macro:

    #===================================================================================================

    """- __init__  - INPUT: ( filename (string), macroname (string) ) ; EFFECT: Initialize MA2macro object and generate file with proper MA2 Macro XML syntax header"""

    def __init__ (self, filename='default_macro_name.xml', macroname='Created with MA3MBL4P'):
        self.__filename = filename
        self.__macroname = macroname

        with open(self.__filename, "w+") as __macro:
            __macro.write('<?xml version="1.0" encoding="utf-8"?>\n')
            __macro.write('<GMA3 DataVersion="1.1.4.2">\n')
            __macro.write('\t<Macro Name="'+self.__macroname+'" Guid="00 00 00 00 84 67 00 00 45 D8 12 FB 41 CE 11 C4">\n')
            return
    #===================================================================================================

    """- macro_line -INPUT: ( macro line number (int), macro command (string) ) ; EFFECT: append proper "Macro line" syntax to filename definied in object"""

    def macro_line (self, macroline='default_macro_line'):
        self.__macroline = macroline
        with open(self.__filename , "a") as __macro:
            __macro.write('\t \t <MacroLine Command="'+self.__macroline+'" />\n')
            return

    #===================================================================================================
    """- macro_end - INPUT: () ; EFFECT: append proper "macro end" syntax to filename definied in object"""
    def macro_end(self):
        with open(self.__filename, "a") as __macro:
            __macro.write('\t</macro>\n')
            return


    # ==================================================================================================
    """- close _file - INPUT: () ; EFFECT append proper "End of file" syntax to filename definied in object and closes file object """

    def close_file(self):
        with open(self.__filename, "a") as __macro:
            __macro.write('</GMA3>')
            __macro.close()
            return

    #====================================================================================================
    #Setters and getters

    def set_filename (self, filename):
        self.__filename = filename
        return

    def get_filename (self):
        return self.__filename

    def get_macroline (self):
        return self.__macroline

#========================================================================================================


