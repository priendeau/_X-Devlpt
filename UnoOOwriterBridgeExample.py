import sys, os, re, uno, iterpipes, thread
from iterpipes import cmd, bincmd, linecmd, run, call, check_call, cmdformat, compose


"""
Openning the OpenOffice Writer with socket Handler
"""

class OpenOfficeWriterBrigeFactory( object ):
  IntPortBridge=2002
  StrHostBridge='localhost'
  StrAcceptBridgeType='socket'
  localContext=None
  resolver=None
  ctx=None
  URIConnection=None

  class PropertyGetterURIException( Exception ):
    Msg='PropertyURIException raised from Function %s.'
    def __init__(self, value ):
      Warning.__init__( self, self.Msg % ( value ) )

  class PropertySetterURIException( Exception ):
    Msg='PropertySetterURIException raised from Function %s.'
    def __init__(self, value ):
      Warning.__init__( self, self.Msg % ( value ) )

  class PropertySetterURINoAttrAssingException( Exception ):
    Msg='PropertySetterURINoAttrAssingException raised from Function %s.'
    def __init__(self, value ):
      Warning.__init__( self, self.Msg % ( value ) )

  class PropertySetterURIMissingFieldException( Exception ):
    Msg='PropertySetterURIMissingFieldException raised from Function %s.'
    def __init__(self, value ):
      Warning.__init__( self, self.Msg % ( value ) )

  class PropertySetterUpdateURIBridgeArgListException( Exception ):
    Msg='PropertySetterUpdateURIBridgeArgListException raised from Function %s. Missing the only one key <<True>>'
  
  class ListURIConnectionNotInstanciated( Warning ):
    Msg='ListURIConnectionNotInstanciated raised from Function %s in favor of empty self.URIConnection not instantiated or incorrectly parsed.'
    def __init__(self, value ):
      Warning.__init__( self, self.Msg % ( value ) )

  def GetUriConnection( self ):
    if not self.URIConnection  == None:
      return self.URIConnection
    else:
      raise self.PropertyURIException , self.GetUriConnection.__name__

  def SetUriConnection( self, value ):
    FuncName=self.SetUriConnection.__name__
    ValueListOrder=[ 'StrAcceptBridgeType','StrHostBridge','IntPortBridge' ]
    if len( value ) != len( ValueListOrder ):
      raise self.PropertySetterURIMissingFieldException, FuncName
    for IntPosN in range( 0 , len(ValueListOrder) ) :
      StreamInfoValue=value[IntPosN]
      StreamInfoKey=ValueListOrder[IntPosN]
      if StreamInfoValue == '':
        raise self.PropertySetterURIException, FuncName
      if not hasattr( self, StreamInfoKey ):
        raise self.PropertySetterURINoAttrAssingException, FuncName
      getattr( self, StreamInfoKey, StreamInfoValue )
      self.URIConnection.append( StreamInfoValue )

  def SetUpdateURIBridgeArgList( self, value  ):
    FuncName=self.SetUpdateURIBridgeArgList.__name__
    if value == True :
      self.URIConnection=[ self.StrAcceptBridgeType , self.StrHostBridge, self.IntPortBridge ]
    else:
      raise self.PropertySetterUpdateURIBridgeArgListException, FuncName

  def GetUpdateURIBridgeArgList( self ):
    return self.URIConnection

  PropertyUpdateURIBridge=property( GetUpdateURIBridgeArgList, SetUpdateURIBridgeArgList )

  PropertyUriConnection=property( GetUriConnection, SetUriConnection )
  
  def CmdOpenWriter( self ):
    try:
      self.AlineCmd=linecmd( 'oowriter {}', "\"-accept=%s,host=%s,port=%s;urp;\"" %  ListArgParse )
    except self.PropertyURIException:
      raise (self.PropertyGetterURIException,self.ListURIConnectionNotInstanciated), (self.CmdOpenWriter.__name__,self.CmdOpenWriter.__name__)
    for self.ItemLine in run( self.AlineCmd ):
      sys.stdout.write( '%s' % ( self.ItemLine )  )

  def StartThread( self ):
    

  def OpenBridge( self ):
    """
       Creating Context
    """
    self.localContext = uno.getComponentContext()
    """
      Creating Resolver
    """
    self.resolver = localContext.ServiceManager.createInstanceWithContext( "com.sun.star.bridge.UnoUrlResolver", localContext )
    """
      Connecting the Bridge
    """
    self.ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )




