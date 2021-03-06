#-*- coding: utf-8 -*-
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.config import cConfig
from resources.hosters.hoster import iHoster
from resources.lib import util
import re,urllib

class cHoster(iHoster):

    def __init__(self):
        self.__sDisplayName = 'Facebook'
        self.__sFileName = self.__sDisplayName
        self.__sHD = ''

    def getDisplayName(self):
        return  self.__sDisplayName

    def setDisplayName(self, sDisplayName):
        self.__sDisplayName = sDisplayName + ' [COLOR skyblue]'+self.__sDisplayName+'[/COLOR]'

    def setFileName(self, sFileName):
        self.__sFileName = sFileName

    def getFileName(self):
        return self.__sFileName

    def getPluginIdentifier(self):
        return 'facebook'

    def setHD(self, sHD):
        self.__sHD = ''

    def getHD(self):
        return self.__sHD

    def isDownloadable(self):
        return True

    def isJDownloaderable(self):
        return True

    def getPattern(self):
        return '';
        
    def __getIdFromUrl(self, sUrl):
        return ''

    def setUrl(self, sUrl):
        self.__sUrl = str(sUrl)

    def checkUrl(self, sUrl):
        return True

    def getUrl(self):
        return self.__sUrl

    def getMediaLink(self):
        return self.__getMediaLinkForGuest()

    def __getMediaLinkForGuest(self):

        qua =[]
        url = []
        api_call = ''

        oRequest = cRequestHandler(self.__sUrl)
        sHtmlContent = oRequest.request()
        sPattern = '((?:h|s)d)_src:"([^"]+)"' 
        oParser = cParser()
        aResult = oParser.parse(sHtmlContent, sPattern)
        

        if (aResult[0] == True):
            for aEntry in aResult[1]:
                qua.append(str(aEntry[0]))
                url.append(str(aEntry[1]))
                
            # Si une seule url
            if len(url) == 1:
                api_call = url[0]
            # si plus de une
            elif len(url) > 1:
            # Afichage du tableau
                ret = util.VScreateDialogSelect(qua)
                if (ret > -1):
                    api_call = url[ret]

        if (api_call):
            return True, api_call

        return False , False