import ffvideo
import os, sys, re
from ffvideo import VideoStream
import pynav
from pynav import Pynav 
from PIL import Image
import tempfile

"""
  Une promesse pour M.Couture( alias, <X> in near future ) de faire un wavelet sur un ensemble d'image pour
  extraire :
  1 - les contours les plus fins pour l'auto-découpage et un traceur de forme finie pour serializer en .SVG
  2 - Extraires les les palettes les plus génerique avec les wavelet les plus grossier, permettant
  3 - le <<Blendage, coloriage, traitement et superposition>> d'image par une conversion local au lieu
  de unie dans la gestion de superposition et montages d'images...

  Cet essais à pour but la détection des formes et des éclats de soleil... Peu-être utiliser pour la
  détection des formes humaines debout ( hints: les humains possède un gyroscope qui re-équilibre
  l'humain selon sa position sur terre... un plug-ins dans vlc dans le mode video en montre la présence
  dans le déplacement de vecteur et montre que la plupart des video pornos disponibles sous les réseaux
  Videotron et Bell, démontre quels sont presques toutes filmé sur notres latitudes (45 et 55deg) )
"""

"""
  Don't forget the Property Order... It's getting conflict only when a superseding property is used
  when another property is being used or will be involved in next operations.
"""
class VideoImportHandler( object ):
  StrStreamFileName  = None
  VidImportFrameSize = None
  FrameMode          = None
  VideoAliasName     = None
  VideoAliasID       = None
  FrameName          = None
  FrameId            = None
  FrameGetterName    = None
  LoadFileName       = None
  vs                 = None
  vsF                = None
  DisplayBufferList  = list()
  DisplayBufferLineLength = None
  ShowModule         = None
  ShowModuleAttr     = None
  ShowModuleAttrDisplay   = None
  VideoHandler       = None
  

  GetterAssociatedName={ 'VideoStream':{
            'no' :{ 'pattern':[0,'no','get_frame_no','frame_no'] ,   'attr':('get_frame_no')     },
            'pts':{ 'pattern':[1,'pts','get_frame_pts','frame_pts'] ,'attr':('get_frame_at_pts') },
            'sec':{ 'pattern':[2,'sec','get_frame_sec','frame_sec'] ,'attr':('get_frame_at_sec') } },
                         're':{
            'file':{ 'pattern':[re.compile(r'(?ui)(/|[a-zA-Z]:)')], 'attr':('open') },
            'url':{ 'pattern':[re.compile(r'(?ui)(http://|url://)')], 'attr':('Pynav') } } }

  DictDisplay={
    1:{ 'display':('Codec           : %s'),   'attr':['codec_name' ], 'type':('str') },
    2:{ 'display':('Frame-Rate      : %s'),   'attr':['framerate'  ], 'type':('str') },
    3:{ 'display':('Duration        : %.2f'), 'attr':['duration'   ], 'type':('float') },
    4:{ 'display':('Filename        : %s'),   'attr':['filename'   ], 'type':('str') },
    5:{ 'display':('Frame size      : %dx%d'),'attr':['frame_width',  'frame_height'],'type':('int') },
    6:{ 'display':('Size per frame  : %s'),   'attr':['frame_size' ], 'type':('str') },
    7:{ 'display':('Frame_mode      : %s'),   'attr':['frame_mode' ], 'type':('str') },
    8:{ 'display':('Frame scale     : %s'),   'attr':['scale_mode' ], 'type':('str') } } 

  class VideoImportHandlerError( Exception ):
    MsgShow='Error Occur:\n'
    def __init__(self, value):
      Exception.__init__( self, self.MsgShow % ( value ) )
    
  class VideoImportHandlerFrameQueryWarning( Warning ):
    MsgShow='Can not understand what is this type of FrameQuery : %s'
    def __init__(self, value):
      Warning.__init__( self, self.MsgShow % ( value ) )

  class VideoImportHandlerLoaderWarning( Warning ):
    MsgShow='Can not open incorrect FileName : %s'
    def __init__(self, value):
      Warning.__init__( self, self.MsgShow % ( value ) )
      
  def GetVideoAlias( self ):
    return self.VideoAliasID

  def SetVideoAlias( self, value ):
    self.VideoAliasName=value
    self.VideoAliasID=getattr( self , self.VideoAliasName )
    print "\t[ Set VideoAlias, Name :%s , ID: %s ]" % ( self.VideoAliasName , self.VideoAliasID )

  PropertyVideoAlias=property( GetVideoAlias , SetVideoAlias )

  def SetFrameIndexCurrentTest( self, value, identityTest='len', DefaultAttr = 'get_frame_at_sec' ):
    self.CurrentTest=getattr( __builtins__, identityTest )( value )
    print "Set Frame provide %d argument." % ( self.CurrentTest )
    if self.CurrentTest == 1:
      """
        Only attribuying only the time sequence by unit of ( get_frame_at_sec ) to Property.
      """
      self.CurrentVideoAlias=self.PropertyVideoAlias
      self.FrameName, self.FrameGetterName, self.StatementCanQuery=value, DefaultAttr, True

    if self.CurrentTest == 2:
      """
        Only attribuying only the time sequence and VideoAlias
      """
      self.FrameName, self.CurrentPropertyVideoAlias = value
      self.PropertyVideoAlias = self.CurrentPropertyVideoAlias
      self.FrameGetterName, self.StatementCanQuery = DefaultAttr, True

    if self.CurrentTest == 3:
      """
        Only attribuying only the time sequence, VideoAlias and the Attribute of Unit Query
      """
      self.FrameName, self.CurrentPropertyVideoAlias, self.GetterNameQuery , = value 
      self.PropertyVideoAlias, self.StatementCanQuery = self.CurrentPropertyVideoAlias , True
      self.StatementGetterResidute=1

  def SetFrameIndexValue( self, value ):
    self.CurrentPropertyVideoAlias=None
    self.SetFrameIndexCurrentTest( value )
    
  def SetFrameQueryAttr( self , KeyMain='VideoStream', DefaultGroupTest=['no','pts','sec'], defaultItemKey='pattern', defaultAttrKey='attr' ):
    print "\t[ Set Frame Query Attribute ]"
    if self.StatementGetterResidute == 1:
      for ItemKey in self.GetterAssociatedName.keys():
        if ItemKey in DefaultGroupTest :
          if self.GetterNameQuery in self.GetterAssociatedName[KeyMain][ItemKey][defaultItemKey]:
            self.FrameGetterName=self.GetterAssociatedName[KeyMain][ItemKey][defaultAttrKey]
            self.StatementCanQuery=True

  def GetFrame( self ):
    return self.FrameId

  def SetFrame( self, value ):
    print "\t[ Set Frame ]"
    self.CurrentVideoAlias        = None
    self.GetterNameQuery          = None
    self.StatementGetterResidute  = 0
    self.StatementCanQuery        = False
    """ """ 
    self.SetFrameIndexValue( value )
    self.SetFrameQueryAttr( )
    if not self.StatementCanQuery :
      raise self.VideoImportHandlerFrameQueryWarning, self.GetterNameQuery 
    else:
      self.CurrentVideoAlias = self.PropertyVideoAlias
      setattr( self, 'FrameId', getattr( self.CurrentVideoAlias, self.FrameGetterName )( self.FrameName ) )
            
  PropertyFrame=property( GetFrame, SetFrame )

  def GetShow( self ):
    CurrentFrame=self.PropertyFrame
    """
      This normally query Image.fromstring, or VideoHandler.fromstring
    """
    return getattr( getattr( self.VideoHandler, self.ShowModuleAttr )( CurrentFrame.frame_mode, CurrentFrame.size, CurrentFrame.data ), self.ShowModuleAttrDisplay )()

  def SetShow( self, value ):
    print "\t[ Set Display Frame engine ]"
    self.ShowModule, self.ShowModuleAttrLoad, self.ShowModuleAttrDisplay  = value
    print "ShowModule: %s\nShowModuleAttrLoad: %s\nShowModuleAttrDisplay: %s\n" % ( self.ShowModule, self.ShowModuleAttrLoad, self.ShowModuleAttrDisplay )

  PropertyShow=property( GetShow, SetShow )

  def print_info_parser( self, DefaultDisplayKey='display', DefaultAttrKey='attr', DefaultTypeKey='type' ):
    self.CurrentVidAlias = self.PropertyVideoAlias
    for ItemTupleKey in self.DictDisplay.keys():
      PatternDisplay=self.DictDisplay[ItemTupleKey][DefaultDisplayKey]
      AttrObj=self.DictDisplay[ItemTupleKey][DefaultAttrKey]
      TypeAttr=self.DictDisplay[ItemTupleKey][DefaultTypeKey]
      newList=list()
      for ItemAttr in AttrObj:
        ValueAttr=getattr( self.CurrentVidAlias, ItemAttr )
        TypeValueAffect=getattr( __builtins__, TypeAttr )( ValueAttr )
        newList.append( TypeValueAffect )
      self.DisplayBufferList.append( PatternDisplay % tuple( newList ) )

  def print_info_get_max_line( self ):
    self.DisplayBufferLineLength=0
    for Item in self.DisplayBufferList:
      IntCurrent=len(Item)
      if self.DisplayBufferLineLength < IntCurrent:
        self.DisplayBufferLineLength=IntCurrent
    
  def print_info( self  ):
    self.DisplayBufferList=list()
    self.print_info_parser( )
    self.print_info_get_max_line( )
    print '-' * self.DisplayBufferLineLength
    for ItemLine in self.DisplayBufferList:
      print ItemLine
    print '-' * self.DisplayBufferLineLength

  def GetLoad( self ):
    return self.print_info( )

  def SetLoaderMeth( self, value, KeyTest ):
    if value == 'Pynav':
      print "Url Method detection within FileName Calling."
      self.UrlHandler=pynav.Pynav()
      self.TempUrl=tempfile.NamedTemporaryFile( 'w+', -1, 'PilVideo', 'temp', None, False )
      self.TempUrl.file.write( self.UrlHandler.go( getattr( self, KeyTest ) ) )
      setattr( self, KeyTest, TempUrl.name )
      self.TempUrl.file.close()
      
  def SetLoad( self, value ):
    print "\t[ Set Loader ]"
    if len(value) == 1:
      self.LoadFileName = value
    if len(value) == 2:
      self.LoadFileName, self.VidImportFrameSize = value
    if len(value) == 3:
      self.LoadFileName, self.VidImportFrameSize, self.FrameMode = value

    for ItemRegExpTest in self.GetterAssociatedName['re'].keys():
      for ItemRegPerList in self.GetterAssociatedName['re'][ItemRegExpTest]['pattern']:
        RegExpTestHandler=ItemRegPerList
        print "Filtering with Pattern: %s:< %s ; %s >" % ( RegExpTestHandler,self.StrStreamFileName , self.LoadFileName )
        if RegExpTestHandler.match( self.StrStreamFileName ):
          self.SetLoaderMeth( self.GetterAssociatedName['re'][ItemRegExpTest]['attr'], 'StrStreamFileName' )
          self.vsF  = VideoStream( self.StrStreamFileName, frame_size=self.VidImportFrameSize , frame_mode=self.FrameMode )
        if RegExpTestHandler.match( self.LoadFileName ):
          self.SetLoaderMeth( self.GetterAssociatedName['re'][ItemRegExpTest]['attr'], 'LoadFileName' )
          self.vs = VideoStream( self.LoadFileName ) 
        
      
    
  PropertyLoad=property( GetLoad, SetLoad )

  def Load( self ):
    if not self.StrStreamFileName == None:
      if not self.VidImportFrameSize == None:
        if not self.FrameMode == None:
          print "StrStreamFileName:%s, VidImportFrameSize:%s, FrameMode:%s" % ( self.StrStreamFileName, self.VidImportFrameSize, self.FrameMode )
          self.PropertyLoad = self.StrStreamFileName, self.VidImportFrameSize, self.FrameMode
        else:
          print "StrStreamFileName:%s, VidImportFrameSize:%s" % ( self.StrStreamFileName, self.VidImportFrameSize )
          self.PropertyLoad = self.StrStreamFileName, self.VidImportFrameSize
      else:
        print "StrStreamFileName:%s" % ( self.StrStreamFileName )
        self.PropertyLoad = self.StrStreamFileName
    else:
      raise self.VideoImportHandlerLoaderWarning, self.StrStreamFileName
  
class VideoImportObject( object ):
    
  def __KargsFilter__( self, **Kargs ):
    if len( Kargs.keys() ) > 0 :
      for IterKeyName in Kargs.keys():
        print "Processing Key:[ %s ]" % ( IterKeyName )
        setattr( self.Main, IterKeyName, Kargs[IterKeyName] )

  def __init__( self, **Kargs ):
    self.Main=VideoImportHandler( )
    self.__KargsFilter__( **Kargs )
    self.Main.Load()
    print "Video Frame Handler[ %s ]" % ( self.Main.vs )
    print "Video Frame-Resized Handler[ %s ]" % ( self.Main.vsF )
    self.Main.PropertyVideoAlias = 'vs'
    print "Video Alias: %s" % ( self.Main.PropertyVideoAlias )

    self.Main.PropertyLoad
    """
      There is a lot of work behind Property-amalgam and C++, templating in effort to
      make common trait type and value for trait type... 
    """
    self.Main.PropertyShow= 'VideoHandler', 'fromstring', 'show'
    self.Main.PropertyFrame=36, 'vs', 'get_frame_sec'
    
    

if __name__.__eq__( '__main__' ):
  StrStreamFileNameTest='/media/COMST500GB/temp/349FED09d01_under_water.flv'
  testVideo=VideoImportObject( StrStreamFileName=StrStreamFileNameTest ,
                               VidImportFrameSize=( 640, 480 ),
                               FrameMode='RGB', VideoHandler=Image )
