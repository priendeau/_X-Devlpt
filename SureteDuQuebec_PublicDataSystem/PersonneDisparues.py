import pynav
from pynav import Pynav

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

def CreateKeyName( ListName ):
  for itemKey in __KeyDictAttribute__:
    setattr( __builtins__,  itemKey, itemKey )

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


  def __init__( self, **Kargs ):
    
    
