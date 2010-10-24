import os, sys, re

class VideoStreamPropertyFFVideo( object ):
  

  QueryAttrDict={
    'print_info_parser':{
      'DefaultDisplayKey':'display',
      'DefaultAttrKey':'attr',
      'DefaultTypeKey':'type' }
    }
  
  
  """
  ###### PROPERTY SUB-SET
  ######
  ###
  ###
                      """
  VideoAliasName=None
  VideoAliasID=None
  def GetVideoAlias( self ):
    return self.VideoAliasID

  def SetVideoAlias( self, value ):
    self.VideoAliasName=value
    self.VideoAliasID=getattr( self , self.VideoAliasName )
    print "\t[ Set VideoAlias, Name :%s , ID: %s ]" % ( self.VideoAliasName , self.VideoAliasID )

  PropertyVideoAlias=property( GetVideoAlias , SetVideoAlias )
  """                            ###
                                 ###
                              ######
             PROPERTY SUB-SET ######
  """

  
  """
  ###### PROPERTY SUB-SET
  ######
  ###
  ###
                      """
  def SetFIndexUniqueValue( self , value ):
    """
      Only attribuying only the time sequence by unit of ( get_frame_at_sec ) to Property.
    """
    (DefaultAttr, Value) = value 
    self.CurrentVideoAlias=self.PropertyVideoAlias
    self.FrameName, self.FrameGetterName, self.StatementCanQuery=Value, DefaultAttr, True

  def SetFIndexTwoValue( self , value ):
    """
      Only attribuying only the time sequence and VideoAlias
    """
    (DefaultAttr, Value) = value 
    self.FrameName, self.CurrentPropertyVideoAlias = Value
    self.PropertyVideoAlias = self.CurrentPropertyVideoAlias
    self.FrameGetterName, self.StatementCanQuery = DefaultAttr, True

  def SetFIndexThreeValue( self , value ):
      """
        Only attribuying only the time sequence, VideoAlias and the Attribute of Unit Query
      """
      (DefaultAttr, Value) = value 
      self.FrameName, self.CurrentPropertyVideoAlias, self.GetterNameQuery , = Value 
      self.PropertyVideoAlias, self.StatementCanQuery = self.CurrentPropertyVideoAlias , True
      self.StatementGetterResidute=1
    
  def SetFrameIndexCurrentTest( self, value, identityTest='len', DefaultAttr = 'get_frame_at_sec' ):
    self.CurrentTest=getattr( __builtins__, identityTest )( value )
    print "Set Frame provide %d argument." % ( self.CurrentTest )
    if self.CurrentTest == 1:
      self.SetFIndexUniqueValue( ( DefaultAttr, value ) )

    if self.SetFIndexTwoValue == 2:
      self.SetFIndexUniqueValue( ( DefaultAttr, value ) )

    if self.CurrentTest == 3:
      self.SetFIndexThreeValue( ( DefaultAttr, value ) )

  def SetFrameIndexValue( self, value ):
    self.CurrentPropertyVideoAlias=None
    self.SetFrameIndexCurrentTest( value )
    
  def SetFrameQueryAttr( self ):
    print "\t[ Set Frame Query Attribute ]"
    if self.StatementGetterResidute == 1:
      for ItemKey in self.GetterAssociatedName.keys():
        if ItemKey in self.DefaultGroupTest :
          if self.GetterNameQuery in self.GetterAssociatedName[ self.QueryAttrDict['KeyMain'] ][ ItemKey ][ self.QueryAttrDict['defaultItemKey'] ]:
            self.FrameGetterName=self.GetterAssociatedName[KeyMain][ItemKey][defaultAttrKey]
            self.StatementCanQuery=True

  def GetFrame( self ):
    return self.FrameId

  def SetFrame( self, value ):
    print "\t[ Set Frame ]"
    self.CurrentVideoAlias=None
    self.GetterNameQuery=None
    self.StatementGetterResidute=0
    self.StatementCanQuery=False
    """
      Future comment.
    """ 
    self.SetFrameIndexValue( value )
    self.SetFrameQueryAttr( )
    if not self.StatementCanQuery :
      raise self.VideoImportHandlerFrameQueryWarning, self.GetterNameQuery 
    else:
      self.CurrentVideoAlias = self.PropertyVideoAlias
      setattr( self, 'FrameId', getattr( self.CurrentVideoAlias, self.FrameGetterName )( self.FrameName ) )

  PropertyFrame=property( GetFrame, SetFrame )
  """                            ###
                                 ###
                              ######
             PROPERTY SUB-SET ######
  """


  """
  ###### PROPERTY SUB-SET
  ######
  ###
  ###
                      """
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
  """                            ###
                                 ###
                              ######
             PROPERTY SUB-SET ######
  """

  """
  ###### PROPERTY SUB-SET
  ######
  ###
  ###
  """
  
  def print_info_parser( self ):
    KeyNameQueryDict=self.print_info_parser.__name__
    QueryDict=self.QueryAttrDict[KeyNameQueryDict]
    
    self.CurrentVidAlias = self.PropertyVideoAlias
    for ItemTupleKey in self.DictDisplay.keys():
      PatternDisplay=self.DictDisplay[ItemTupleKey][ QueryDict[DefaultDisplayKey] ]
      AttrObj=self.DictDisplay[ ItemTupleKey ][ QueryDict[DefaultAttrKey] ]
      TypeAttr=self.DictDisplay[ ItemTupleKey ][ QueryDict[DefaultTypeKey] ]
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
  """                            ###
                                 ###
                              ######
             PROPERTY SUB-SET ######
  """
