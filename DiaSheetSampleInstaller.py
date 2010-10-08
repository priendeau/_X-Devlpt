import os, sys, re, zlib, zipfile, base64, time, datetime, thread, iterpipes, guidata
from iterpipes import cmd, bincmd, linecmd, run, call, check_call, cmdformat, compose
import pynav
from pynav import Pynav
import apt
from apt import cache



guidata.qapplication()

import guidata.dataset.datatypes as dt
import guidata.dataset.dataitems as di
from guidata.dataset.datatypes import *
from guidata.dataset.dataitems import *

class DiaSheetUpdate( object ):

  DiaPackageScan=r'(?ui)dia'
  PackageReport=dict()

  class SubDataset( dt.dataset ):
    dirPath = DirectoryItem( "Directory", os.path.dirname('/home/ubuntu') )
    
##  class GuiInterfaceSelect(dt.DataSet):
##    TableUpdate = di.


  class AptHandler( object ):

    class DirectiveReady( Warning ):
      def __init__(self, msg):
        Warning.__init__( self, msg )
        pass
      
    class WarnDirective( Warning ):
      def __init__(self, msg):
        Warning.__init__( self, msg )
        pass

    class WarnDirectiveUselessAction( Warning ):
      def __init__(self, msg):
        Warning.__init__( self, msg )
        pass

    class WarnDirectiveOutOfScope( Warning ):
      def __init__(self, msg):
        Warning.__init__( self, msg )
        pass

    class WarnDirectiveSessionNotClosed( Warning ):
      def __init__(self, msg):
        Warning.__init__( self, msg )
        pass

    class WarnDirectiveSessionNotLocked( Warning ):
      def __init__(self, msg):
        Warning.__init__( self, msg )
        pass

    class WarnDirectiveSessionNotCommitted( Warning ):
      def __init__(self, msg):
        Warning.__init__( self, msg )
        pass

    class WarnDirectiveSessionCommittedUnlock( Warning ):
      def __init__(self, msg):
        Warning.__init__( self, msg )
        pass

    class WarnDirectiveSessionUnlocked( Warning ):
      def __init__(self, msg):
        Warning.__init__( self, msg )
        pass

    class WarnDirectiveSessionNotUnlocked( Warning ):
      def __init__(self, msg):
        Warning.__init__( self, msg )
        pass

    class ExceptDirectiveGateLatchingProblems( Exception ):
      def __init__(self, msg):
        Exception.__init__( self, msg )
        pass

    class ExceptDirectiveOpFailure( Exception ):
      def __init__(self, msg):
        Exception.__init__( self, msg )
        pass
    
    DirectiveList={ 'storeDict':{ 'open':False, 'close':True ,'lock':False, 'commit':False },
                     'bindCode':{ 'open':False, 'close':True ,'lock':False, 'commit':False } }

    """
      This was introduced inside a Community work at Cegep of Rosemont under a Java project involving
      a creation of graduated-Administrative technician information belong to manage qualification and
      several information... At this time I only own few times and despite the story of a complete class
      loosing theirs time by assisting on Informatic course of 1999-420.0a Informatic Techniques, most of
      student of this grade was caught downloading spayware, malware, music, porn... and all the rest was
      caught getting things like my T.P.... Even M.Gaillou[xs] was presenting the altered version of the
      final T.P., a version of mine... Quite surprising And truth...

      Well, at the time I was askied to generate a Database with Java, Jdbc technologies was not a big problems
      since the Java 1.1 introduced a equivalent of Interlogic Jdbc-Access... I would not want to
      try VB6 or so being know to generate a lot of oditties and ancestrality know to be ugly, I was in charge
      to keep compatibility of MS-Access, where I was ables to craft something fast until I fall on a uncertains
      pit where I should manage unknown condition... Developping something written after inside beautiful code,
      The expected counting (recensing) information by developping comb-filter, where a matrix of information
      is holding information on counting, mine just hold information on open access, commiting information and
      if there is lock... The work was generously gived to VDL2/ ex-VDL2, Pheromone under Ledevoir project(2002)
      holding a crypted Access DB, Where the inspection tools workings like SQL syntax prompt developped
      under this time was used to port the Access into postgreSql withing days, saving lots of effort...

      And those know M.Bourget, this one always calling the Access-driven Jdbc-Pilot, an Excel Server...
      M.Asseling can report lots of wasting time feeding information inside this project without really owning
      right to argues or request comment on future developmnent where I hope it can be precious in OPLA
      project handling... Which I was surprize by M.bourget to not letting me having talk... Was-it a task,
      homework, duty or simple punition for him ... Only God can know about... 
    """
    SessionExceptionList=[
      [ { 'open':True,  'close':True,  'lock':True,  'commit':True  }, [ 'ExceptDirectiveGateLatchingProblems'] ],
      [ { 'open':True,  'close':True,  'lock':True,  'commit':False }, [ 'ExceptDirectiveGateLatchingProblems','WarnDirectiveSessionNotCommitted' ] ],
      [ { 'open':True,  'close':True,  'lock':False, 'commit':True  }, [ 'ExceptDirectiveGateLatchingProblems','WarnDirectiveSessionNotLocked' ] ],
      [ { 'open':True,  'close':True,  'lock':False, 'commit':False }, [ 'ExceptDirectiveGateLatchingProblems','WarnDirectiveSessionNotLocked','WarnDirectiveSessionNotCommitted' ] ],
      [ { 'open':True,  'close':False, 'lock':True,  'commit':True  }, [ None ] ] ,
      [ { 'open':True,  'close':False, 'lock':True,  'commit':False }, [ None ] ] ,
      [ { 'open':True,  'close':False, 'lock':False, 'commit':True  }, [ 'WarnDirectiveSessionCommittedUnlock' ] ] ,
      [ { 'open':True,  'close':False, 'lock':False, 'commit':False }, [ 'WarnDirectiveSessionUnlocked' ] ] ,
      [ { 'open':False, 'close':True,  'lock':True,  'commit':True  }, [ 'WarnDirectiveSessionNotUnlocked','WarnDirectiveSessionNotCommitted' ] ] ,
      [ { 'open':False, 'close':True,  'lock':True,  'commit':False }, [ 'WarnDirectiveSessionNotUnlocked' ] ] ,
      [ { 'open':False, 'close':True,  'lock':False, 'commit':True  }, [ 'WarnDirectiveSessionNotCommitted'] ] ,
      [ { 'open':False, 'close':True,  'lock':False, 'commit':False }, [ None ] ] ,
      [ { 'open':False, 'close':False, 'lock':True,  'commit':True  }, [ 'WarnDirectiveSessionNotUnlocked','WarnDirectiveSessionNotCommitted'] ] ,
      [ { 'open':False, 'close':False, 'lock':True,  'commit':False }, [ 'WarnDirectiveSessionNotUnlocked' ] ] ,
      [ { 'open':False, 'close':False, 'lock':False, 'commit':True  }, [ 'WarnDirectiveSessionCommittedUnlock','WarnDirectiveSessionNotCommitted'] ] ,
      [ { 'open':False, 'close':False, 'lock':False, 'commit':False }, [ 'DirectiveReady' ] ] ]

    """
      Valid Case :
      [ { 'open':True,  'close':False, 'lock':True,  'commit':True  }, [ None ] ]
      - A Directive between storeDict and bindCode is in use, being locked against crossing the
      directive, a commit was asked, to feed the information inside the stream.

      Valid Case :
      [ { 'open':True,  'close':False, 'lock':True,  'commit':False }, [ None ] ] ,
      - A Directive between storeDict and bindCode is in use, being locked against crossing the
      directive is at least instanciated, affected or simply in build.

      Valid Case :
      [ { 'open':False, 'close':True,  'lock':False, 'commit':False }, [ None ] ] ,
      - A Directive between storeDict and bindCode is asked to close, commit may be done or useless if
      it's an bufferless directive or quantumic-operation.

      Valid Case :
      [ { 'open':False, 'close':False, 'lock':False, 'commit':False }, [ None ] ] ]
      None of The Directive is Instanciated and shall be ready to start.

    """
    
    DictPackageInfo=dict()
    DirectiveHandler=None
    DirectiveLastOp=None

    """

        The Directive theory with implementation of Yield in PropertyPackage :
        The uses of yield in a Property directive is to allow the content to
        to be oriented in a specific OSI Level... This way will provide method
        to allow content being stored inside a dict() and using counter method
        or mixture of second-listed directive type will throw error over
        unexplicit uses of FileSystemStoring and Code Binding method...
        We are supposing Debian can test package inside a virtual env. and can
        explicitly test all recurrent lib binding... This engine is a single
        explanation of creation of logical gateway and restrict method being
        used in another fashion.

        resume@40%:
        The uses of yield in a Property directive is to allow the content to
        be oriented in a specific OSI Level... This way will provide method to
        allow content being stored inside a dict() and using counter method or
        mixture of second-listed directive type will throw error over unexplicit
        uses of FileSystemStoring and Code Binding method...

    """

    def SetErrorHandler( self , Value ):
      self.NextThrowDirective=None
      try:
        try:
          for CondFollowPattern, CondFollowErrorList in self.SessionExceptionList:
            if self.DirectiveList[ self.DirectiveHandler ] == CondFollowPattern:
              for ErrorThrowable in CondFollowErrorList:
                self.NextThrowDirective=getattr( self, ErrorThrowable )
                yield self.NextThrowDirective
          
        except self.WarnDirective:
          raise self.NextThrowDirective, "Throw WarnDirective"

      except self.DirectiveReady:
        raise self.DirectiveReady, "Process Can Start."
        pass

    def GetErrorHandler( self ):
      raise self.NextThrowDirective.next()

    PropertyErrorHandler=property( GetErrorHandler, SetErrorHandler )
    
    def SetDirective( self, value ):
      self.DirectiveHandler, self.DirectiveHandler = Value
      
    def GetDirective( self ):
      return self.DirectiveHandler
    

    PropertyDirective=property( GetDirective, SetDirective )
    
    def SetPackageChunk( self, value ):
      self.PropertyDirective = value
      for self.ItemPackege in AptCache:
        yield self.ItemPackege

    def GetPackageChunk( self ):
      return self.PackageList.next() 

    PropertyPackageChunk=property( GetPackageChunk, SetPackageChunk )
    
    def PackageVerification( self ):
      print "Function: %s" % ( self.PackageVerification.__name__ )
      
    def __init__( self, ReMatch ):
      self.PropertyDirective = 'storeDict'
      self.AptCache=apt.cache.Cache()
      self.MatchPackage = re.compile( ReMatch )
      
   
##	if DiaPackage.match( ItemPackege.name ):
##		PackageReport[ItemPackege.name]=dict()
##		PackageReport[ItemPackege.name]['object']=ItemPackege
##		PackageReport[ItemPackege.name]['file']=ItemPackege.installedFiles()
  def __init__( self ):
    AptCache=apt.cache.Cache()
    for ItemPackage in AptCache:
      print "%s" % ( ItemPackage.name )
##    param = Processing()
##    param.edit()

      
if __name__.__eq__( '__main__' ):
  AUpdate=DiaSheetUpdate()
