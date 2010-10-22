import sys, os, re, cStringIO
import time, datetime
import cPickle
import decimal
import thread
import zipfile
import zlib
import tempfile
from decimal import *

###
### FileName : Fibonnaci_exclusion_number.py
### 

getcontext().prec = 36

FhFilename=[ ['fibonacci_excl.pkl.zip', 'zip' ] ,
             ['fibonacci_excl.pkl'    , 'raw' ] ]

def TempFileWriteStreamInit( TempFileLoader, StreamIn ):
  TempFileLoader.file.write( StreamIn )
  TempFileLoader.file.seek( 0 ) 
  
def PicklerZipLoader( TempFileLoader, FileName ):
  print "Unpacking Compressed pickler"
  Dzip=zipfile.ZipFile( FileName, 'r' )
  TempFileWriteStreamInit( TempFileLoader, zlib.decompress( Dzip.read( 'fibonacci_excl.pkl' ) ) )
  Dzip.close()
  del Dzip

def PicklerRawLoader( TempFileLoader, FileName ):
  print "Unpacking Un-Compressed pickler"
  DRawHandler=open( FileName, 'r+' )
  TempFileWriteStreamInit( TempFileLoader, DRawHandler.read() )
  DRawHandler.close()
  del DRawHandler

def GetSizeStatFile( Filename ):
  FhStat=open( Filename, 'r+' )
  FosStats=os.fstat( FhStat.fileno() )
  IntSizePickleCpr=FosStats.st_size
  FhStat.close()
  del FosStats
  del FhStat
  return IntSizePickleCpr

def LoadPickler( AtempFile, DictDestName ):
  Dpickler=cPickle.Unpickler( AtempFile )
  AtempFile.file.seek(0)
  Dpickler=cPickle.Unpickler( AtempFile )
  #NewfibDict=Dpickler.load()
  #setattr( __builtins__, DictDestName, Dpickler.load() )
  DictDestName.update( Dpickler.load() )
  
def PicklerLoader( FileNameList, DictDestName ):
  DictUpdated=False
  atemp=tempfile.NamedTemporaryFile()
  Dzip=None
  DRawHandler=None
  Dpickler=None
  NewfibDict=None
  for IntFileHandler in range( 0 , len( FileNameList ) ):
    FileName, FileFormat = FileNameList[IntFileHandler]
    print "Testing File: %s " % ( FileName )
    IntSizePickleCpr=GetSizeStatFile( FileName )
    print "Report File Size : %s" % ( IntSizePickleCpr )
    if IntSizePickleCpr > 0:
      if not DictUpdated:
        if FileFormat == 'zip':
          PicklerZipLoader( atemp, FileName )
          DictUpdated=True
        if FileFormat == 'raw' :
          PicklerRawLoader( atemp, FileName )
          DictUpdated=True
        LoadPickler( atemp, DictDestName )
      

def Fibonacci2( n ):

  def Timer( ModuleDef={'Module':time , 'Attr':('time') } ):
    return getattr( ModuleDef['Module'], ModuleDef['Attr'] )()

  def SetStartTimer( DictName, AttrNode=None, AttrChild=None ):
    if AttrChild != None:
      DictName[AttrNode][AttrChild]=Timer()
    else:
      DictName[AttrNode]=Timer()

  def SetEndtTimer( DictName, AttrNode=None, AttrChild=None ):
    if AttrChild != None:
      DictName[AttrNode][AttrChild]=( Timer() - DictName[AttrNode][AttrChild] )
    else:
      DictName[AttrNode]=( Timer() - DictName[AttrNode] ) 
    
  def StubTransform( LongFib ):
    Alist=list()
    for item in str(LongFib):
      Alist.append( item )
    ReverseList=list(Alist)
    ReverseList.reverse()
    return ( Alist, ReverseList )

  def FilterNoFib( IntFibResult , List ):
    ReturnList=list()
    Range={'min':List[(len(List)-2)], 'max':IntFibResult }
    for ItemNum in range( Range['min'], Range['max'] ):
      if ItemNum not in List and ItemNum not in ReturnList:
        ReturnList.append( ItemNum )
    return ReturnList

  def CallFib( n ):
    u,v,k=int(),int(),int()
    u,v=1,0
    l=list()
    Time={ 'fibCreation':(),
           'StubTransform':(),
           'FilterNoFib':() }
    Time['fibCreation']=time.time()
    for k in range( 0, n ):
      u,v=v,u+v
      l.append(v)
      
    SetEndtTimer( Time, 'fibCreation' )
    SetStartTimer( Time, 'StubTransform' )
    tupleFibDecSep=StubTransform( v )
    SetEndtTimer( Time, 'StubTransform' )
    SetStartTimer( Time, 'FilterNoFib' )
    listReturn=FilterNoFib( v , l )
    SetEndtTimer( Time, 'FilterNoFib' )
    DictReturn={ 'fibonacci':(v),
                 'list':l,
                 'fibonacci_tuple':tupleFibDecSep[0],
                 'fibonacci_tupleR':tupleFibDecSep[1],
                 'notfib':listReturn,
                 'time':Time }
    return DictReturn
  return CallFib( n )

class WarnNoImplicitLock( Warning ):
  Msg='No Lock is installed inside the Dict, key:%s '
  def __init__(self, value):
    Warning.__init__( self, self.Msg % ( value ) )

class WarnOverLockingImplicitLock( Warning ):
  Msg='Locking already installed in Dict, key:%s '
  def __init__(self, value):
    Warning.__init__( self, self.Msg % ( value ) )

DictNameLock=None
DictNameLockState=None

def SetDictAddImplicitLock( value , LockKeyName='lock', StoreKey='value' ):
  if len( value ) == 1 :
    DictNameLock=value

  if not LockKeyName in getattr( eval(DictNameLock) , 'keys' )():
    DictFib[LockKeyName]=dict()
    DictFib[LockKeyName][StoreKey]=True
  else:
    raise WarnOverLockingImplicitLock, LockKeyName

def GetDictAddImplicitLock( LockKeyName='lock', StoreKey='value' ):
  if not LockKeyName in getattr( eval(DictNameLock) , 'keys' )():
    DictFib[LockKeyName]=dict()
    DictFib[LockKeyName][StoreKey]=True
  else:
    raise WarnOverLockingImplicitLock, LockKeyName

def SetDictDelImplicitLock( Dict, LockKeyName='lock', StoreKey='value' ):
  if LockKeyName in getattr( eval(DictNameLock) , 'keys' )():
    del DictFib[LockKeyName]
  else:
    raise WarnNoImplicitLock, LockKeyName

def GetDictDelImplicitLock( LockKeyName='lock', StoreKey='value' ):
  if LockKeyName in getattr( eval(DictNameLock) , 'keys' )():
    del DictFib[LockKeyName]
  else:
    raise WarnNoImplicitLock, LockKeyName

PropertyImplicitLockAdd=property( GetDictAddImplicitLock, SetDictAddImplicitLock )

PropertyImplicitLockDel=property( GetDictDelImplicitLock, SetDictDelImplicitLock )
    
def UnitTestFibonacci( DictFib, startRange, stopRange ):
  
  ListContentOut=list()
  TemplateDesc="Fibonacci:%d, %d \nElapsed Time:\n\t%s, %f\n\t%s, %f\n\t%s, %f\n\t"
  CountRange=startRange
  ProcessFib=True
  while CountRange <= stopRange:
    IntFibCreation=CountRange
    if not IntFibCreation in DictFib.keys():
      if ProcessFib:
        DictFib[IntFibCreation]=Fibonacci2( IntFibCreation )
        StrStream=TemplateDesc % ( IntFibCreation,DictFib[IntFibCreation]['fibonacci'] ,
                                     'fibCreation' , DictFib[IntFibCreation]['time']['fibCreation'],
                                     'StubTransform' ,DictFib[IntFibCreation]['time']['StubTransform'] ,
                                     'FilterNoFib' ,DictFib[IntFibCreation]['time']['FilterNoFib'] )
        ListContentOut.append( StrStream )
        TimeCalc=0L
        for itemKey in DictFib[IntFibCreation]['time'].keys():
          TimeCalc+=DictFib[IntFibCreation]['time'][itemKey]
        print "Fib:(%04d), Final Time : %s sec." % ( IntFibCreation, Decimal(str(TimeCalc)) )
    else:
      stopRange+=1
      print "Will Throw the limit to %d, Fibonacci Number(%d) already exist." % ( stopRange, IntFibCreation )
    CountRange+=1
  return DictFib

def ShowCreationTime( DictName ):
  for item in DictName.keys():
    if len(str(DictName[item]['notfib'])) > 100 :
      DictNotFibonacci="%s%s%s" % ( '[', str(DictName[item]['notfib'])[0:120] , ']... Shorted --->' )
    else:
      DictNotFibonacci=str(DictName[item]['notfib'])
    TupleDisplay=( item,
                   DictName[item]['fibonacci'] ,
                   DictName[item]['time']['fibCreation'] ,
                   DictName[item]['time']['FilterNoFib'],
                   DictNotFibonacci )
    print "Fibonacci: Fb(%d):%d Creation Time <Fibcreation, ExclusionList >%f ; %f sec\n\t%s" % ( TupleDisplay )

def PickleFibonacci( Dict , FhFilename='/home/ubuntu/fibonacci_excl.pkl.zip', ZipName='fibonacci_excl.pkl' ):
  Dzip=zipfile.ZipFile( FhFilename, 'w' )
  atemp=tempfile.NamedTemporaryFile()
  aPickler=cPickle.Pickler( atemp, -1 )
  aPickler.dump( Dict )
  del aPickler
  atemp.seek(0)
  Dzip.writestr( ZipName, zlib.compress( atemp.read() , 9 ) )
  Dzip.close()
  atemp.file.close()
  del atemp
  
if __name__ == '__main__' :
  if not 'NewfibDict' in vars():
    NewfibDict=dict()
    PicklerLoader(FhFilename,NewfibDict)
    
    thread.start_new_thread( UnitTestFibonacci, ( NewfibDict ,1 ,1, ) )
else:
 if not 'NewfibDict' in vars():
  NewfibDict=dict()
  PicklerLoader(FhFilename,NewfibDict)
  thread.start_new_thread( UnitTestFibonacci, ( NewfibDict ,1 ,1, ) )
  
  #ShowCreationTime( NewfibDict )
  
	
