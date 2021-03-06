#-*- coding: utf-8 -*-
#Venom.
from resources.lib.gui.contextElement import cContextElement
from resources.lib.gui.guiElement import cGuiElement
import urllib
import logger
from resources.lib.config import cConfig
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.pluginHandler import cPluginHandler
import xbmc
import xbmcgui
import xbmcplugin

class cGui:

    SITE_NAME = 'cGui'
    CONTENT = 'files'

    def addMovie(self, sId, sFunction, sLabel, sIcon, sThumbnail, sDesc, oOutputParameterHandler = ''):
        cGui.CONTENT = "movies"
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setMeta(1)
        oGuiElement.setDescription(sDesc)
        
        oOutputParameterHandler.addParameter('sFav', oGuiElement.getFunction())
        self.__createContexMenuWatch(oGuiElement, oOutputParameterHandler)
        self.__createContexMenuWriteFav(oGuiElement, oOutputParameterHandler)

        self.addFolder(oGuiElement, oOutputParameterHandler)
        
        
    def addTV(self, sId, sFunction, sLabel, sIcon, sThumbnail, sDesc, oOutputParameterHandler = ''):
        cGui.CONTENT = "tvshows"
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setMeta(2)
        oGuiElement.setDescription(sDesc)
        
        oOutputParameterHandler.addParameter('sFav', oGuiElement.getFunction())
        self.__createContexMenuWatch(oGuiElement, oOutputParameterHandler)
        self.__createContexMenuWriteFav(oGuiElement, oOutputParameterHandler)
        
        self.addFolder(oGuiElement, oOutputParameterHandler)
        
    def addMisc(self, sId, sFunction, sLabel, sIcon, sThumbnail, sDesc, oOutputParameterHandler = ''):
        cGui.CONTENT = "files"
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setMeta(0)
        oGuiElement.setDescription(sDesc)
        
        oOutputParameterHandler.addParameter('sFav', oGuiElement.getFunction())
        self.__createContexMenuWatch(oGuiElement, oOutputParameterHandler)
        self.__createContexMenuWriteFav(oGuiElement, oOutputParameterHandler)
        
        self.addFolder(oGuiElement, oOutputParameterHandler)
        
    def addFav(self, sId, sFunction, sLabel, sIcon, sUrl, oOutputParameterHandler = ''):
        cGui.CONTENT = "files"
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setMediaUrl(sUrl)
        oGuiElement.setMeta(0)
        
        self.__createContexMenuDelFav(oGuiElement, oOutputParameterHandler)
        
        self.addFolder(oGuiElement, oOutputParameterHandler)     
    
    
    def addDir(self, sId, sFunction, sLabel, sIcon, oOutputParameterHandler = ''):
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(sId)
        oGuiElement.setFunction(sFunction)
        oGuiElement.setTitle(sLabel)
        oGuiElement.setIcon(sIcon)
        oGuiElement.setMeta(0)
        
        oOutputParameterHandler.addParameter('sFav', oGuiElement.getFunction())
        
        self.addFolder(oGuiElement, oOutputParameterHandler)       
    
    def addFolder(self, oGuiElement, oOutputParameterHandler=''):
        sItemUrl = self.__createItemUrl(oGuiElement, oOutputParameterHandler)
        oListItem = self.createListItem(oGuiElement)
        
        oListItem = self.__createContextMenu(oGuiElement, oListItem)
       
        
        sPluginHandle = cPluginHandler().getPluginHandle();

        xbmcplugin.addDirectoryItem(sPluginHandle, sItemUrl, oListItem, True, oGuiElement.getCount())

    def createListItem(self, oGuiElement):
        #oPath = cPluginHandler().getRootArt()
        oListItem = xbmcgui.ListItem(oGuiElement.getTitle(), oGuiElement.getTitleSecond(), oGuiElement.getIcon())
        oListItem.setInfo(oGuiElement.getType(), oGuiElement.getItemValues())
        oListItem.setThumbnailImage(oGuiElement.getThumbnail())

        aProperties = oGuiElement.getItemProperties()
        for sPropertyKey in aProperties.keys():
            oListItem.setProperty(sPropertyKey, aProperties[sPropertyKey])
        
        return oListItem

    def __createContexMenuWatch(self, oGuiElement, oOutputParameterHandler= ''):
        oContext = cContextElement()
        oContext.setFile('cGui')
        oContext.setSiteName(oGuiElement.getSiteName())
        oContext.setFunction('setWatched')
        oContext.setTitle('[COLOR azure]Marquer vu/Non vu[/COLOR]')

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sTitle', oGuiElement.getTitle())
        oOutputParameterHandler.addParameter('sId', oGuiElement.getSiteName())
      
        oContext.setOutputParameterHandler(oOutputParameterHandler)

        oGuiElement.addContextItem(oContext)


    def __createContexMenuDelFav(self, oGuiElement, oOutputParameterHandler= ''):

        oContext = cContextElement()
        oContext.setFile('cFav')
        oContext.setSiteName('cFav')
        oContext.setFunction('delFavourites')
        oContext.setTitle('[COLOR red]Supprimer Marque-Page[/COLOR]')

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sTitle', oGuiElement.getTitle())
        oOutputParameterHandler.addParameter('sId', oGuiElement.getSiteName())
        oOutputParameterHandler.addParameter('siteUrl', oGuiElement.getMediaUrl())
      
        oContext.setOutputParameterHandler(oOutputParameterHandler)

        oGuiElement.addContextItem(oContext)           
    
    def __createContexMenuWriteFav(self, oGuiElement, oOutputParameterHandler= ''):
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        sFav = oInputParameterHandler.getValue('sFav')
        
        oContext = cContextElement()
        oContext.setFile('cFav')
        oContext.setSiteName('cFav')
        oContext.setFunction('writeFavourites')
        oContext.setTitle('[COLOR teal]Marque-page[/COLOR]')

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sTitle', oGuiElement.getTitle())
        oOutputParameterHandler.addParameter('sId', oGuiElement.getSiteName())
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sFav', sFav)
      
        oContext.setOutputParameterHandler(oOutputParameterHandler)

        oGuiElement.addContextItem(oContext)

        return
    
    
    def __createContextMenu(self, oGuiElement, oListItem):
        sPluginPath = cPluginHandler().getPluginPath();
        aContextMenus = []

        if (len(oGuiElement.getContextItems()) > 0):
            for oContextItem in oGuiElement.getContextItems():                
                oOutputParameterHandler = oContextItem.getOutputParameterHandler()
                sParams = oOutputParameterHandler.getParameterAsUri()
                sTest = '%s?site=%s&function=%s&%s' % (sPluginPath, oContextItem.getFile(), oContextItem.getFunction(), sParams)                
                aContextMenus+= [ ( oContextItem.getTitle(), "XBMC.RunPlugin(%s)" % (sTest,),)]

            oListItem.addContextMenuItems(aContextMenus)
            #oListItem.addContextMenuItems(aContextMenus, True)

        oContextItem = cContextElement()
        oContextItem.setFile('cFav')
        oContextItem.setSiteName('cFav')
        oContextItem.setTitle('[COLOR teal]Voir Marque-page[/COLOR]')
        oContextItem.setFunction('getFavourites')
        oOutputParameterHandler = oContextItem.getOutputParameterHandler()
        sParams = oOutputParameterHandler.getParameterAsUri()
        sTest = '%s?site=%s&function=%s&contextFav=true&%s' % (sPluginPath, oContextItem.getFile(), oContextItem.getFunction(), sParams)
        aContextMenus+= [ ( oContextItem.getTitle(), "XBMC.Container.Update(%s)" % (sTest,),)]
        oListItem.addContextMenuItems(aContextMenus)
            
        if  oGuiElement.getTrailerUrl(): 
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('sHosterIdentifier', 'youtube')
                oOutputParameterHandler.addParameter('sMediaUrl', oGuiElement.getTrailerUrl())
                oOutputParameterHandler.addParameter('sFileName', oGuiElement.getTitle())
                oContextItem = cContextElement()
                oContextItem.setFile('cHosterGui')
                oContextItem.setSiteName('cHosterGui')
                oContextItem.setTitle('[COLOR azure]Bande Annonce[/COLOR]')
                oContextItem.setFunction('play')
                oContextItem.setOutputParameterHandler(oOutputParameterHandler)
                
                oOutputParameterHandler = oContextItem.getOutputParameterHandler()
                sParams = oOutputParameterHandler.getParameterAsUri()
                sTest = '%s?site=%s&function=%s&%s' % (sPluginPath, oContextItem.getFile(), oContextItem.getFunction(), sParams)
                aContextMenus+= [ ( oContextItem.getTitle(), "XBMC.RunPlugin(%s)" % (sTest,),)]
                oListItem.addContextMenuItems(aContextMenus)
        
        return oListItem
        
    def __ContextMenu(self, oGuiElement, oListItem):
        sPluginPath = cPluginHandler().getPluginPath();
        aContextMenus = []

        if (len(oGuiElement.getContextItems()) > 0):
            for oContextItem in oGuiElement.getContextItems():                
                oOutputParameterHandler = oContextItem.getOutputParameterHandler()
                sParams = oOutputParameterHandler.getParameterAsUri()
                sTest = '%s?site=%s&function=%s&%s' % (sPluginPath, oContextItem.getFile(), oContextItem.getFunction(), sParams)                
                aContextMenus+= [ ( oContextItem.getTitle(), "XBMC.RunPlugin(%s)" % (sTest,),)]

            oListItem.addContextMenuItems(aContextMenus)
            #oListItem.addContextMenuItems(aContextMenus, True)

        return oListItem
     
    def __ContextMenuPlay(self, oGuiElement, oListItem):
        sPluginPath = cPluginHandler().getPluginPath();
        aContextMenus = []

        if (len(oGuiElement.getContextItems()) > 0):
            for oContextItem in oGuiElement.getContextItems():                
                oOutputParameterHandler = oContextItem.getOutputParameterHandler()
                sParams = oOutputParameterHandler.getParameterAsUri()
                sTest = '%s?site=%s&function=%s&%s' % (sPluginPath, oContextItem.getFile(), oContextItem.getFunction(), sParams)                
                aContextMenus+= [ ( oContextItem.getTitle(), "XBMC.RunPlugin(%s)" % (sTest,),)]

            oListItem.addContextMenuItems(aContextMenus)
            #oListItem.addContextMenuItems(aContextMenus, True)

        return oListItem

    def setEndOfDirectory(self):
        iHandler = cPluginHandler().getPluginHandle()
        xbmcplugin.setPluginCategory(iHandler, "")
        xbmcplugin.setContent(iHandler, cGui.CONTENT)
        xbmcplugin.addSortMethod(iHandler, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(iHandler, True)

    def updateDirectory(self):
	xbmc.executebuiltin("Container.Refresh")
    
    def setWatched(self):
        oGuiElement = cGuiElement()
        oInputParameterHandler = cInputParameterHandler()

        sTitle = oInputParameterHandler.getValue('sTitle')
        sId = oInputParameterHandler.getValue('sId')

        #oGuiElement.setTitle(sTitle)
        #oGuiElement.setSiteName(sId)
        oGuiElement.setWatched(sId, sTitle)
        xbmc.executebuiltin( 'Container.Refresh' )

    def __createItemUrl(self, oGuiElement, oOutputParameterHandler=''):
        if (oOutputParameterHandler == ''):
            oOutputParameterHandler = cOutputParameterHandler()
                    
        sParams = oOutputParameterHandler.getParameterAsUri()
        sPluginPath = cPluginHandler().getPluginPath();

        if (len(oGuiElement.getFunction()) == 0):
            sItemUrl = '%s?site=%s&title=%s&%s' % (sPluginPath, oGuiElement.getSiteName(), urllib.quote_plus(oGuiElement.getTitle()), sParams)
        else:
            sItemUrl = '%s?site=%s&function=%s&title=%s&%s' % (sPluginPath, oGuiElement.getSiteName(), oGuiElement.getFunction(), urllib.quote_plus(oGuiElement.getTitle()), sParams)
        return sItemUrl

    def showKeyBoard(self, sDefaultText=''):
        logger.info('showKeyboard')
        keyboard = xbmc.Keyboard(sDefaultText)
        keyboard.doModal()
        if (keyboard.isConfirmed()):
            sSearchText = keyboard.getText()
            if (len(sSearchText)) > 0:
                return sSearchText

        return False

    def openSettings(self):
        cConfig().showSettingsWindow()

    def showNofication(self, sTitle, iSeconds=0):
        if (cConfig().isDharma() == False):
            return

	if (iSeconds == 0):
            iSeconds = 1000
	else:
            iSeconds = iSeconds * 1000
        
        xbmc.executebuiltin("Notification(%s,%s,%s)" % (cConfig().getLocalizedString(30308), (cConfig().getLocalizedString(30309) % str(sTitle)), iSeconds))

    def showError(self, sTitle, sDescription, iSeconds=0):
        if (cConfig().isDharma() == False):
            return

	if (iSeconds == 0):
            iSeconds = 1000
	else:
            iSeconds = iSeconds * 1000

        xbmc.executebuiltin("Notification(%s,%s,%s)" % (str(sTitle), (str(sDescription)), iSeconds))

    def showInfo(self, sTitle, sDescription, iSeconds=0):
        if (cConfig().isDharma() == False):
            return

	if (iSeconds == 0):
            iSeconds = 1000
	else:
            iSeconds = iSeconds * 1000

        xbmc.executebuiltin("Notification(%s,%s,%s)" % (str(sTitle), (str(sDescription)), iSeconds))
