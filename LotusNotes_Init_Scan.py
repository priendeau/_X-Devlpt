import os, sys, re
import LoggerInfoLotusNotes
from LoggerInfoLotusNotes import LoggerInfoLotusNotes 
import DecoratorLotus
from DecoratorLotus import DecoratorLotus

"""
    Sample of Lotus Scanner.
    Description: Scan Lotus Notes, notes.ini and scan Notes.ini to find duplicates Keys while notes.ini in
    transition may have irrigularities and hold more than one sample. Also This sample will in second-time,
    valites information from excessive field value from differents version of notes and yield invalid transitions
    states.

"""

class LotusScan( object ):
  Implements=None
  Factory=None

  class LotusScanFactory( object ):
    #filename='c:/notes/notes.ini'
    filename=None
    ListBuffer=None
    DictReference={ 'notes.ini':{ } ,
                    'duplicate':[ ] }  
    Fh=None
    DisplayColLen=False
    StepSplit=True
    TestDuplicate=False
    AddDictNote=False
    LoopItemScan=True
    IsReadFile=True
    DisplayKeyName=True
    #ThisDecorator.InnerClassName=self.__class__.__name__
    
    def __AddDictNote__( self ):
      if self.DisplayKeyName:
        print "Key Name : %s" % ( self.SplitItem[0] )
      if self.AddDictNote:
        self.DictReference['notes.ini'][ self.SplitItem[0] ]=self.SplitItem[1]

    def __DisplayColLen__( self ):
      if self.DisplayColLen:
        print "Number of item per col : %d" % ( len(SplitItem) )

    @DecoratorLotus.SurveyStatFlags( 'TestDuplicate' )
    def __TestDuplicate__( self ):
      if self.SplitItem[0] in self.DictReference:
        self.DictReference['duplicate'].append( self.SplitItem )
      else:
        self.__AddDictNote__()

    @DecoratorLotus.SurveyStatFlags( 'StepSplit' )
    def __StepSplit__( self ):
      self.__TestDuplicate__()


    @DecoratorLotus.SurveyStatFlags( 'LoopItemScan' )
    def __LoopItemScan__( self ):
      for self.ItemLines in self.ListBuffer:
        self.SplitItem=self.ItemLines.split( '=' )
        self.__DisplayColLen__( )
        if len( self.SplitItem ) == 2:
          self.__StepSplit__( )

    @DecoratorLotus.SurveyStatFlags( 'IsReadFile' )
    def read( self ):
      #if self.IsReadFile:
      self.Fh=open( self.filename , 'r' )
      self.Fh.seek(0)
      self.ListBuffer=self.Fh.readlines( )
      self.__LoopItemScan__( )
      
  class LotusScanImpl( object ):

    def __init__( self ) :
      Factory=LotusScan.LotusScanFactory( )
      self.LogInformation=LoggerInfoLotusNotes()
      self.LogInformation.PropertyPriority = 'info'
      self.LogInformation.PropertyLog = 'Starting Logging information for LotusNote notes.ini Error and report.'
      Factory.read()

  @DecoratorLotus.ParseTheKargs( LotusScanFactory, None , None  )    
  def __init__( self, **Kargs ):
    self.Implements=LotusScan.LotusScanImpl( )

if __name__.__eq__( '__main__' ):
##  LoggerInfo=LoggerInfoLotusNotes()
##  LoggerInfo.PropertyPriority = 'info'
##  LoggerInfo.PropertyLog = 'Starting Logging information for LotusNote notes.ini Error and report.'
  DecoratorLotus.InnerClassName=LotusScan.LotusScanFactory
  Ascan=LotusScan( filename='c:/notes/notes.ini' ,IsReadFile=True, DisplayKeyName=False )
  #Ascan=LotusScan( IsReadFile=True, DisplayKeyName=False, AddDictNote=True )
