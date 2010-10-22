import sys, os, re, uno, iterpipes, thread, time
import iterpipes
from iterpipes import cmd, bincmd, linecmd, run, call, check_call, cmdformat, compose

"""
  - Under development.
  - not final
  - is prototype
  - thoose can correct it shall not ask to get it work before I decide to remove the Item No.2
  - Have a nice day.
"""

"""
  Explanation :
  What is a UnoOOBridge ?

  Belong to Sun, OpenOffice division, Developpers from OpenOffice have provided extra functionality
  for developper like scipting and programmatic-macro to let creation and automation of Users-experience
  being seemless to human normal development, in mass production of content.

  The UnoBridge is a module and this module can access to an Open Instance of worlking Office
  Suite tools like OOWriter, OOCalc, OOPresentation... And can talk to the engine, being able to
  act like user and add content...

  It own exact functionality except this one can be automated for mass development...

  Quite Simple ;)


  Other Transistive option : Learning aids and Tutorial on specific context...

  Known, Office tools is a 4th generation of tools, being able to do everything,
  people learning how it's working gain more than just supplemental qualification
  but can reduce considerably effort, scheme and dignostic by providing plan,
  answer and event over what is asked.. But Unfortunately there is no information
  on specific methodology for specific context needs. There is several Exemple and
  human are cowardly invited to uses theirs brain to seek for similarity. This
  UnoBridge, can design the All-Experience in a sequence which can teach more easily
  in professionnal context specific alternate tools can safe time rather having no
  hands at all helping for a task, there is couple of solution.

  Learning Aids is a domains keys in ADD, ADHD, stimulus in todays over uses of
  stimulant, contribued to ruins dopamine-attention-based situation involving
  similirarity visualisation, sematic approximation and task alternative
  distribution...

  Note: Merely synthesised from DSM-IV, ADD and ADHD deficit in child schoolar performance
  and lack of creativity and motivation skills.

  
  

"""


"""
  Will be usefull on launching-date, will search if a package for openoofice is installed...
  And maybe all the rest...
  don't forget,
  
  for Item in [ 'uno', 'apt' ] :
    for ItemLine in run( linecmd( 'pip install {}', ( Item ) ) ) :
      print ItemLine
  Can install everything automatically...

  having a repository holding iterpipes, using autoinstall a must...
  
"""
from apt import cache

"""
Openning the OpenOffice Writer with socket Handler
"""

class OpenOfficeWriterBrigeImpl( object ):
  
  class OpenOfficeWriterBrigeFactory( object ):
    IntPortBridge=2002
    StrHostBridge='localhost'
    StrAcceptBridgeType='socket'
    localContext=None
    resolver=None
    ctx=None
    URIConnection=None
    WriterReady=False
    InterfaceWaitingTotal=None
    DefaultSleepSlice=5
    TriggerList={ 'interruption':False }
    TriggerKey=None
    TriggerValue=None
    EngineList=['oocalc', 'oodraw', 'ooffice', 'oomath', 'ooimpress', 'ooweb', 'oowriter']
    OfficeEngine=None


    class EngineListNotImplemented( Warning ):
      Msg='FactoryFinish raised for Interruption of %s'
      def __init__(self, value ):
        Warning.__init__( self, self.Msg % ( value ) )

    class FactoryFinish( Exception ):
      Msg='FactoryFinish raised for Interruption of %s'
      def __init__(self, value ):
        Exception.__init__( self, self.Msg % ( value ) )

    class PropertyGetterURIException( Exception ):
      Msg='PropertyURIException raised from Function %s.'
      def __init__(self, value ):
        Exception.__init__( self, self.Msg % ( value ) )

    class PropertySetterURIException( Exception ):
      Msg='PropertySetterURIException raised from Function %s.'
      def __init__(self, value ):
        Exception.__init__( self, self.Msg % ( value ) )

    class PropertySetterURINoAttrAssingException( Exception ):
      Msg='PropertySetterURINoAttrAssingException raised from Function %s.'
      def __init__(self, value ):
        Exception.__init__( self, self.Msg % ( value ) )

    class PropertySetterURIMissingFieldException( Exception ):
      Msg='PropertySetterURIMissingFieldException raised from Function %s.'
      def __init__(self, value ):
        Exception.__init__( self, self.Msg % ( value ) )

    class PropertySetterUpdateURIBridgeArgListException( Exception ):
      Msg='PropertySetterUpdateURIBridgeArgListException raised from Function %s. Missing the only one key <<True>>'
    
    class ListURIConnectionNotInstanciated( Warning ):
      Msg='ListURIConnectionNotInstanciated raised from Function %s in favor of empty self.URIConnection not instantiated or incorrectly parsed.'
      def __init__(self, value ):
        Warning.__init__( self, self.Msg % ( value ) )

    def GetTriggerState( self ):
      if self.TriggerList[self.TriggerKey] == True:
        raise self.FactoryFinish, self.TriggerKey

    """
      Only True are allowed, most of the time they are final interruption and will not imply an unlocking...
      There is less-sever Trigger-state comming...
    """
    def SetTriggerState( self, value ):
      self.TriggerKey=value 
      self.TriggerValue=True
      self.TriggerList[self.TriggerKey]=self.TriggerValue

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

    def GetOpenOffice( self, value ):
      self.OpenOfficeEngine = 'value'
      
    def SetOpenOffice( self, value ):
      if value not in self.EngineListNotImplemented:
        raise self.EngineListNotImplemented
      return self.OpenOfficeEngine

    PropertyTriggerInterrupt=property( GetTriggerState, SetTriggerState )

    PropertyUpdateURIBridge=property( GetUpdateURIBridgeArgList, SetUpdateURIBridgeArgList )

    PropertyUriConnection=property( GetUriConnection, SetUriConnection )
    
    def CmdOpenWriter( self ):
      try:
        self.AlineCmd=linecmd( 'oowriter {}', "\"-accept=%s,host=%s,port=%s;urp;\"" %  self.PropertyUriConnection )
      except self.PropertyURIException:
        raise (self.PropertyGetterURIException,self.ListURIConnectionNotInstanciated), (self.CmdOpenWriter.__name__,self.CmdOpenWriter.__name__)
      for self.ItemLine in run( self.AlineCmd ):
        sys.stdout.write( '%s' % ( self.ItemLine )  )
      self.WriterReady=True

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
      self.ctx = resolver.resolve( "uno:%s,host=%s,port=%s;urp;StarOffice.ComponentContext" % self.PropertyUriConnection  )


    def StartThread( self ):
      thread.start_new_thread( self.CmdOpenWriter, (,) )
      while not self.WriterReady :
        time.sleep( self.DefaultSleepSlice )
        self.InterfaceWaitingTotal+=self.DefaultSleepSlice


