import configparser

def getLocator(section, key):
    reader=configparser.ConfigParser()
    reader.read()