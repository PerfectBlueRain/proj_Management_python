__author__ = '1002475'

from xml.dom.minidom import parse, parseString

class BookMgr:
    def __init__(self):
        self.val = 0


    # XML file -> DOM
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

