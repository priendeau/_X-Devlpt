import pynav
from pynav import Pynav

class DecoratorSQ:

  DictReference={
    'Error':{
      'Handler':False, 'Name':[ None ] } }

  ReferenceTransfert={ }

  @classmethod
  def InnerVariableFromFuncModule( ModuleImport, defaultNodeImpl=__builtins__ ):
    for item in dir( ModuleImport ):
      TypeItem=type(getattr( iterpipes, item))
      if TypeItem == type(nameTestType):
        setattr( defaultNodeImpl, item, getattr( iterpipes, item) )

  @classmethod
  def InnerModuleImport( ModuleImportName, DefaultListFunc=[], defaultNodeImpl=__builtins__, defaultImporter='__import__' ):
    if not ModuleImportName in vars():
      print "Module Name %s not in memory, importing-it" % ( ItemModuleName )
      getattr( defaultNodeImpl, defaultImporter )( ItemModuleName , {}, {}, DefaultListFunc , -1 )

  @classmethod
  def InnerCreateKeyName( ListName ):
    for itemKey in ListName:
      if itemKey in vars():
        DecoratorSQ.ReferenceTransfert[itemKey]=getattr( __builtins__, 'eval')( itemKey )
      setattr( __builtins__,  itemKey, itemKey )

  @classmethod
  def InnerCreateKeyName( ListName ):
    for itemKey in ListName:
      setattr( __builtins__,  itemKey, itemKey )


  @staticmethod
  def ImplementError( ErrorName ):
    self.DictReferencep[ 'Error' ][ 'Handler' ]= True
    self.DictReferencep[ 'Name' ][ 'Handler' ]=ErrorName

  @staticmethod
  def TimerImplement( ClassName,  AttrNameProcHwnd ):
    
    """
    This Decorator Will:
    - Create a variable funcName being assigned automatically to funcName the FunctionName

    The marshaller computes a key from function arguments
    """
    def decorator(func):
        def inner(*args, **kwargs):
          if self.DictReference[ 'Error' ][ 'Handler' ] == True:
            raise getattr( ClassName, self.DictReferencep[ 'Name' ][ 'Handler' ] )
          
          if not func.__name__ in getattr( ClassName , AttrNameProcHwnd ).keys():
            getattr( ClassName, AttrNameProcHwnd )[func.__name__]=list()
          else:
            getattr( ClassName, AttrNameProcHwnd )[func.__name__].append( time.time() )
          func( *args, **kwargs )
        return inner
    return decorator

  @staticmethod
  def VariableFromFuncModule( ModuleImport, defaultNodeImpl=__builtins__ ):
    """
    This Decorator Will:
    - Create a variable funcName being assigned automatically to funcName the FunctionName

    The marshaller computes a key from function arguments
    """
    def decorator(func):
        def inner(*args, **kwargs):
          DecoratorSQ.VariableFromFuncModule( ModuleImport, defaultNodeImpl ) 
          func( *args, **kwargs )
        return inner
    return decorator

  @staticmethod
  def ModuleImport( ModuleImportName, DefaultListFunc=[], defaultNodeImpl=__builtins__, defaultImporter='__import__' ):
    """
    This Decorator Will:
    - Create a variable funcName being assigned automatically to funcName the FunctionName

    The marshaller computes a key from function arguments
    """
    def decorator(func):
        def inner(*args, **kwargs):
          DecoratorSQ.InnerModuleImport( ModuleImportName, DefaultListFunc, defaultNodeImpl, defaultImporter )
          if len( defaultNodeImpl ) > 0 :
            DecoratorSQ.VariableFromFuncModule( getattr( __builtins__,ModuleImportName), DefaultListFunc )
          func( *args, **kwargs )
        return inner
    return decorator
  
  @staticmethod
  def ParseTheKargs( ClassName,  ShelveObject, TypeObj ):
    
    """
    This Decorator Will:
    - Create a variable funcName being assigned automatically to funcName the FunctionName

    The marshaller computes a key from function arguments
    """
    def decorator(func):
        def inner(*args, **kwargs):
          for ItemKeyName in kwargs.keys():
            if ShelveObject == None:
              if not hasattr( ClassName, ItemKeyName ):
                setattr( ClassName, ItemKeyName, kwargs[ItemKeyName] )
            else:
              if TypeObj == None:
                if not hasattr( getattr( ClassName,ShelveObject ), ItemKeyName ):
                  setattr( getattr( ClassName,ShelveObject ), ItemKeyName, kwargs[ItemKeyName] )
                else:
                  setattr( getattr( ClassName,ShelveObject ), ItemKeyName, kwargs[ItemKeyName] )
              else:
                if type(TypeObj) == type(dict()):
                  if not ItemKeyName in getattr( ClassName,ShelveObject ).keys():
                    setattr( ClassName,ShelveObject,  { ItemKeyName:kwargs[ItemKeyName] } )
                  else:
                    setattr( ClassName,ShelveObject, { ItemKeyName:kwargs[ItemKeyName] } )
          func( *args, **kwargs )
        return inner
    return decorator

  @staticmethod
  def InstanceFuncMessage( MessageName ):
    
    """
    """
    def decorator(func):
        def inner(*args, **kwargs):
          print "From Def:%s\n\t%s." % ( func.__name__ , MessageName )
          func( *args, **kwargs )
        return inner
    return decorator

  @staticmethod
  def GlobalKeyNameAssertion( ListKey ):
    
    """
    """
    def decorator(func):
        def inner(*args, **kwargs):
          DecoratorSQ.InnerCreateKeyName( ListKey )
          func( *args, **kwargs )
          DecoratorSQ.InnerDeleteKeyName( ListKey )
        return inner
    return decorator


"""

  This structure is intended for the Public Access of Visual Information, to provide tools to
  accelerate search or enhance content into harmonic-identification of << dudits recherchés >>...

  This is provided by third non-private party's and is out of any remuneration form or contribution form
  to provide the information under false-reason, abussive form or gangsterism-form listed in Canada.

  This Tools is provided as-is and beleive in evolution of tools to provide accurate information to
  help our security systems being wiser...


  By the way, This tools will implement fast path drawing with conversion of image into wavelet path-definition,
  and being meshed with meshPy to provide structural rotation form and valid images deformation re-rendering in
  3d world....

  
"""

__KeyDictAttribute__=[ 'Object','url','web','image', 'link' ]



CreateKeyName( __KeyDictAttribute__ )


class DictProperty( object ):

  def GetParentKey( self ):
    return self.RootKey

  def SetParentKey( self, value ):
    Value = value
    self.RootKey=self.DictReferences[ Value ]

  def GetChildKey( self ):
    return self.RootKey

  def SetChildKey( self, value ):
    Value = value
    self.RootKey=self.DictReferences[ Value ]
    
class PersonnesDisparues( object ):

  ASdQc={ Object:pynav.Pynav(),
          url:'http://www.sq.gouv.qc.ca/personnes-disparues/personnes-disparues-surete-du-quebec.jsp#pageDemandee=1',
          web:{
            'image':None,
            link:None } }

  @DecoratorSQ.InstanceFuncMessage( "Creating Instance" )
  def InitCall( self ):
    return True
    
  @DecoratorSQ.ParseTheKargs( DictProperty , None, None )
  def __init__( self, **Kargs ):
    self.InitCall( )
