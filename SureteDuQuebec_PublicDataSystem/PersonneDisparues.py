import pynav
from pynav import Pynav
from SureteDuQuebec_PublicDataSystem import decorator
from SureteDuQuebec_PublicDataSystem.decorator import DecoratorSQ

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



class DictPropertyFactory( object ):

  ASdQc={ 'Object':pynav.Pynav(),
          'url':'http://www.sq.gouv.qc.ca/personnes-disparues/personnes-disparues-surete-du-quebec.jsp#pageDemandee=1',
          'web':{
            'image':None,
            'link':None } }

  IntNodeLevel=0
  CurrentNodeLevel=None
  TreeNode=[ ] 

  RootNode=None
  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def GetRootNode( self ):
    return self.RootNode

  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def SetRootNode( self, value ):
    self.RootClassName, self.RootClassNode = value
    self.RootNode=getattr( self.RootClassName, self.RootClassNode )
  
  PropertyRootNode=property( GetRootNode, SetRootNode)
  
  ParentKey=None
  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def GetParentKey( self ):
    return self.ParentKey

  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def SetParentKey( self, value ):
    Value = value
    self.ParentKey=self.DictReferences[ Value ]

  PropertyParentKey=property( GetParentKey, SetParentKey)
  
  ChildKey=None
  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def GetChildKey( self ):
    return [self.ChildKey]

  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def SetChildKey( self, value ):
    Value = value
    self.ChildKey=self.DictReferences[ Value ]

  PropertyChildKey=property( GetChildKey, SetChildKey )
  
class PersonnesDisparues( object ):

  Factory=DictPropertyFactory()

  @DecoratorSQ.InstanceFuncMessage( "Creating Instance" )
  def InitCall( self ):
    return True
    
  @DecoratorSQ.ParseTheKargs( Factory , None, None )
  def __init__( self, **Kargs ):
    self.InitCall( )
