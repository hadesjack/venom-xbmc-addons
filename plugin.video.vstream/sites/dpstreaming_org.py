#-*- coding: utf-8 -*-
#Venom.
from resources.lib.gui.hoster import cHosterGui
from resources.lib.handler.hosterHandler import cHosterHandler
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.util import cUtil
import re

SITE_IDENTIFIER = 'dpstreaming_org'
SITE_NAME = 'dpstreaming.org'

URL_MAIN = 'http://dpstreaming.org/'

def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://dpstreaming.org/category/films/')
    __createMenuEntry(oGui, 'showMovies', 'Films', '', '', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://dpstreaming.org/category/films-en-exclus/')
    __createMenuEntry(oGui, 'showMovies', 'Films Exclus', '', '', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    __createMenuEntry(oGui, 'showGenre', 'Films Genres', '', '', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://dpstreaming.org/category/series-tv/')
    __createMenuEntry(oGui, 'showMovies', 'Series', '', '', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    __createMenuEntry(oGui, 'showAZ', 'Series A-Z', '', '', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://dpstreaming.org/category/mangas/')
    __createMenuEntry(oGui, 'showMovies', 'Mangas', '', '', oOutputParameterHandler)
    
            
    oGui.setEndOfDirectory()

def __createMenuEntry(oGui, sFunction, sLabel, sThumbnail, sDesc, oOutputParameterHandler = ''):
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setFunction(sFunction)
    oGuiElement.setTitle(sLabel)
    oGuiElement.setThumbnail(sThumbnail)
    oGuiElement.setDescription(cUtil().removeHtmlTags(sDesc))
    oGui.addFolder(oGuiElement, oOutputParameterHandler)
 
def showAZ():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
 
    liste = []
    liste.append( ["0-9","http://dpstreaming.org/category/series-tv/0-9/"] )
    liste.append( ["A-B-C","http://dpstreaming.org/category/series-tv/a-b-c/"] )
    liste.append( ["D-E-F","http://dpstreaming.org/category/series-tv/d-e-f/"] )
    liste.append( ["G-H-I","http://dpstreaming.org/category/series-tv/g-h-i/"] )
    liste.append( ["J-K-L","http://dpstreaming.org/category/series-tv/j-k-l/"] )
    liste.append( ["M-N-O","http://dpstreaming.org/category/series-tv/m-n-o/"] )
    liste.append( ["P-Q-R","http://dpstreaming.org/category/series-tv/p-q-r/"] )
    liste.append( ["S-T-U","http://dpstreaming.org/category/series-tv/s-t-u/"] )
    liste.append( ["V-W-X-Y-Z","http://dpstreaming.org/category/series-tv/v-w-x-y-z/"] )
                
    for sTitle,sUrl in liste:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        __createMenuEntry(oGui, 'showMovies', sTitle, '', '', oOutputParameterHandler)
       
    oGui.setEndOfDirectory() 
    
def showGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
 
    liste = []
    liste.append( ['Action','http://dpstreaming.org/category/films/action/'] )
    liste.append( ['Animation','http://dpstreaming.org/category/films/animation/'] )
    liste.append( ['Arts Martiaux','http://dpstreaming.org/category/films/arts-martiaux/'] )
    liste.append( ['Aventure','http://dpstreaming.org/category/films/aventure-films/'] )
    liste.append( ['Biopic','http://dpstreaming.org/category/films/biopic/'] )
    liste.append( ['Comedie','http://dpstreaming.org/category/films/comedie/'] )
    liste.append( ['Comedie Dramatique','http://dpstreaming.org/category/films/comedie-dramatique/'] )
    liste.append( ['Documentaire','http://dpstreaming.org/category/films/documentaire/'] )
    liste.append( ['Drame','http://dpstreaming.org/category/films/drame/'] )
    liste.append( ['Espionnage','http://dpstreaming.org/category/films/espionnage/'] )   
    liste.append( ['Famille','http://dpstreaming.org/category/films/famille/'] )
    liste.append( ['Fantastique','http://dpstreaming.org/category/films/fantastique/'] )
    liste.append( ['Guerre','http://dpstreaming.org/category/films/guerre/'] )
    liste.append( ['Historique','http://dpstreaming.org/category/films/historique/'] )
    liste.append( ['Horreur','http://dpstreaming.org/category/films/horreur/'] )
    liste.append( ['Musical','http://dpstreaming.org/category/films/musical/'] )
    liste.append( ['Policier','http://dpstreaming.org/category/films/policier/'] )
    liste.append( ['Romance','http://dpstreaming.org/category/films/romance/'] )
    liste.append( ['Science-Fiction','http://dpstreaming.org/category/films/science-fiction/'] )
    liste.append( ['Spectacle','http://dpstreaming.org/category/films/spectacle/'] )
    liste.append( ['Thriller','http://dpstreaming.org/category/films/thriller/'] )
    liste.append( ['Western','http://dpstreaming.org/category/films/western/'] )
    liste.append( ['VOSTFR','http://dpstreaming.org/category/films/vostfr-films/'] )
    liste.append( ['Bluray','http://dpstreaming.org/category/films/bluray-1080p-720p/'] )
    liste.append( ['Bluray 3D','http://dpstreaming.org/category/films/bluray-3d/'] )
                
    for sTitle,sUrl in liste:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        __createMenuEntry(oGui, 'showMovies', sTitle, '', '', oOutputParameterHandler)
       
    oGui.setEndOfDirectory() 


def showMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('[Streaming]', '').replace('[Telecharger]', '')
    sPattern = '<img width=".+?" height=".+?" src="([^<]+)" class="postim wp-post-image".+?<h2><a href="([^<]+)" rel="bookmark" .+?>([^<]+)</a></h2></div>.+?<p>(.+?)<a href=".+?">.+?</a></p>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[1]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(aEntry[2]))
            oOutputParameterHandler.addParameter('sThumbnail', str(aEntry[0]))
            if '/series-tv/' in sUrl:
                __createMenuEntry(oGui, 'showSeries', aEntry[2], aEntry[0], aEntry[3], oOutputParameterHandler)
            elif '/mangas/' in sUrl:
                __createMenuEntry(oGui, 'mangaHosters', aEntry[2], aEntry[0], aEntry[3], oOutputParameterHandler)
            else:
                __createMenuEntry(oGui, 'showHosters', aEntry[2], aEntry[0], aEntry[3], oOutputParameterHandler)
            
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            __createMenuEntry(oGui, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', '', '', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showSeries():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('<strong>Téléchargement VOSTFR','').replace('<strong>Téléchargement VF','').replace('<strong>Téléchargement','')
 
    sPattern = '<span style="color: #33cccc;"><strong>([^<]+)|<p style="text-align: center;">([^<]+)<a (.+?)</p>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        for aEntry in aResult[1]:
            if aEntry[0]:
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
                oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
                oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
                __createMenuEntry(oGui, 'showSeries', '[COLOR red]'+str(aEntry[0])+'[/COLOR]', sThumbnail, '', oOutputParameterHandler)
            else:
                sTitle = sMovieTitle+' - '+aEntry[1]
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', str(aEntry[2]))
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
                __createMenuEntry(oGui, 'serieHosters', sTitle, sThumbnail, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    sPattern = '<a class="page larger" href="(.+?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return aResult[1][0]

    return False
    

def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('<iframe src="http://ads.affbuzzads.com','')


    sPattern = '<iframe src="([^<]+)" frameborder'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            sHosterUrl = str(aEntry)
            #oHoster = __checkHoster(sHosterUrl)
            oHoster = cHosterGui().checkHoster(sHosterUrl)
        
            if (oHoster != False):
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail) 

    oGui.setEndOfDirectory()
    
    
def mangaHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('<iframe src="http://ads.affbuzzads.com','')


    sPattern = '<p style="text-align: center;">([^<]+)<a href="([^<]+)" target="_blank">.+?</a></p>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            sHosterUrl = str(aEntry[1])
            #oHoster = __checkHoster(sHosterUrl)
            oHoster = cHosterGui().checkHoster(sHosterUrl)
        
            if (oHoster != False):
                sTitle = sMovieTitle+' - '+aEntry[0]
                oHoster.setDisplayName(sTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail) 

    oGui.setEndOfDirectory()
    
def serieHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    sPattern = 'href="([^<]+)" target="_blank">.+?</a>'
    oParser = cParser()
    aResult = oParser.parse(sUrl, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            sHosterUrl = str(aEntry)
            #oHoster = __checkHoster(sHosterUrl)
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            
            if (oHoster != False):
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail) 

    oGui.setEndOfDirectory()
    