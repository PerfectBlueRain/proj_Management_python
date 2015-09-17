__author__ = 'torres'
#-*- coding: utf-8-*-

from xml.dom.minidom import parse, parseString

class BookMgr:
    def __init__(self):
        self.val = 0


    # 1. load data : XML file -> DOM
    def LoadXMLFromFile(self, filePath):
        print("...file path is : " + filePath)

        # file open
        try:
            fd_xml = open(filePath)
        except IOError:
            print("[error] invalid file name or path")
            return None  # 예외시 retrun
        else:
            print("[complete] XML file open")

        # XML parse
        try:
            data_dom = parse(fd_xml) # XML parse
        except Exception:
            print("[error] XML loading fail!")
        else:
            print("[complete] XML loading compelte")
            return data_dom  # success

        return None

    # 2. print raw data (XML format <- DOM)
    def PrintDOMtoXML(self, booksDoc):
        print("...booksDoc(DOM data) to XML format and print")

        if self._checkDocument(booksDoc):
            print( booksDoc.toxml() )


    ## check data is None or not
    def _checkDocument(self, booksDoc):
        if booksDoc == None:
            print("[error] booksDoc data is empty")
            return False
        return True

