import os, sys, re, logging


"""

  Basic Configuration

  Before using any other functions in the logging module, you should first perform
  some basic configuration of a special object known as the root logger.The root logger is
  responsible for managing the default behavior of log messages including the logging
  level, output destination, message format, and other basic details.The following function
  is used for configuration:

  basicConfig([**kwargs])
  TODO: resume following topic @20%
  
  
"""
class LoggerInfoLotusNotes( object ):

  Implements=None
  
  class ErrorPriorityNotSet( Warning ):
    attrname, attrvalue = None, None 
    MsgShow='No Priority Set with Attr %s, value: %s' 
    def __init__( self, value ):
      self.attrname, self.attrvalue = value
      print "Value inspected:<< %s;%s >>" % ( self.attrname, self.attrvalue )
      if self.attrvalue == None:
        Warning.__init__( self, self.MsgShow % ( self.attrname, self.attrvalue ) )
      pass

  class LoggerInfoLotusNotesFactory( object ):
    Log=None
    LogStatement=None
    Priority=None
    
    ListPriority=[ 'critical','error','warning','info','debug' ]

    def GetPriority( self ):
      return self.Priority

    def SetPriority( self, value ):
      print "Setting New Priority, value conf: << %s >>" % ( value )
      if value in self.ListPriority:
        self.Priority=value

    PropertyPriority=property( GetPriority, SetPriority )
    
    def GetLog( self ):
      return self.LogStatement

    def SetLog( self, value ):
      print "Storing New Log Messages, value conf: << %s >>" % ( value )
      self.LogStatement = value
      raise LoggerInfoLotusNotes.ErrorPriorityNotSet, [ 'Priority' , self.Priority ]
      getattr( self.Logger, self.Priority )( self.LogStatement ) 

    PropertyLog=property( GetLog, SetLog )

  class LoggerInfoLotusNotesImpl( object ):
    Logger=None
    Log=None
    Factory=None
    
    def __init__( self ):
      self.Logger=logging.getLogger( self.__class__.__name__ )
      self.Log=logging.basicConfig( filename = "%s.log" % self.__class__.__name__ ,
                                    format   = "%(levelname)-10s %(asctime)s %(message)s" )

      self.Factory=LoggerInfoLotusNotes.LoggerInfoLotusNotesFactory( )
      
  def __init__( self ):
    self.Implements=LoggerInfoLotusNotes.LoggerInfoLotusNotesImpl( ) 
