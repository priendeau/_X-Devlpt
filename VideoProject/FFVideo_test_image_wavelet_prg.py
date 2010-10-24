import ffvideo
import os, sys, re
from ffvideo import VideoStream
import pynav
from pynav import Pynav 
from PIL import Image
import tempfile

"""

  Une promesse pour M.Couture( alias, <X> in near future ) de faire un wavelet sur un ensemble d'image pour
  extraire :
  1 - les contours les plus fins pour l'auto-découpage et un traceur de forme finie pour serializer en .SVG
  2 - Extraires les les palettes les plus génerique avec les wavelet les plus grossier, permettant
  3 - le <<Blendage, coloriage, traitement et superposition>> d'image par une conversion local au lieu
  de unie dans la gestion de superposition et montages d'images...

  Cet essais à pour but la détection des formes et des éclats de soleil... Peu-être utiliser pour la
  détection des formes humaines debout ( hints: les humains possède un gyroscope qui re-équilibre
  l'humain selon sa position sur terre... un plug-ins dans vlc dans le mode video en montre la présence
  dans le déplacement de vecteur et montre que la plupart des video pornos disponibles sous les réseaux
  Videotron et Bell, démontre quels sont presques toutes filmé sur notres latitudes (45 et 55deg) )

  
"""

"""
  Don't forget the Property Order... It's getting conflict only when a superseding property is used
  when another property is being used or will be involved in next operations.
"""
class VideoImportObject( object ):
  Main=None
  ReferenceDescriptor=None
  
  """
    YYY : Object Descriptor.
  """

  class VideoImportHandler( object ):

    StrStreamFileName=None
    VidImportFrameSize=None
    FrameMode=None
    FrameName=None
    FrameId=None
    FrameGetterName=None
    LoadFileName=None
    vs=None
    vsF=None
    DisplayBufferList=list()
    DisplayBufferLineLength=None
    ShowModule=None
    ShowModuleAttr=None
    ShowModuleAttrDisplay=None
    VideoHandler=None
    DefaultGroupTest=['no','pts','sec']
    QueryAttrDict={
      'KeyMain':'VideoStream',
      'defaultItemKey':'pattern',
      'defaultAttrKey':'attr' }
    
    class VideoImportHandlerError( Exception ):
      MsgShow='Error Occur:\n'
      def __init__(self, value):
        Exception.__init__( self, self.MsgShow % ( value ) )
      
    class VideoImportHandlerFrameQueryWarning( Warning ):
      MsgShow='Can not understand what is this type of FrameQuery : %s'
      def __init__(self, value):
        Warning.__init__( self, self.MsgShow % ( value ) )

    class VideoImportHandlerLoaderWarning( Warning ):
      MsgShow='Can not open incorrect FileName : %s'
      def __init__(self, value):
        Warning.__init__( self, self.MsgShow % ( value ) )
    


    def Load( self ):
      if not self.StrStreamFileName == None:
        if not self.VidImportFrameSize == None:
          if not self.FrameMode == None:
            print "StrStreamFileName:%s, VidImportFrameSize:%s, FrameMode:%s" % ( self.StrStreamFileName, self.VidImportFrameSize, self.FrameMode )
            self.PropertyLoad = self.StrStreamFileName, self.VidImportFrameSize, self.FrameMode
          else:
            print "StrStreamFileName:%s, VidImportFrameSize:%s" % ( self.StrStreamFileName, self.VidImportFrameSize )
            self.PropertyLoad = self.StrStreamFileName, self.VidImportFrameSize
        else:
          print "StrStreamFileName:%s" % ( self.StrStreamFileName )
          self.PropertyLoad = self.StrStreamFileName
      else:
        raise self.VideoImportHandlerLoaderWarning, self.StrStreamFileName
  
    
  def __KargsFilter__( self, **Kargs ):
    if len( Kargs.keys() ) > 0 :
      for IterKeyName in Kargs.keys():
        print "Processing Key:[ %s ]" % ( IterKeyName )
        setattr( self.Main, IterKeyName, Kargs[IterKeyName] )

  def __init__( self, **Kargs ):
    self.Main=VideoImportHandler( )
    self.__KargsFilter__( **Kargs )
    self.Main.Load()
    print "Video Frame Handler[ %s ]" % ( self.Main.vs )
    print "Video Frame-Resized Handler[ %s ]" % ( self.Main.vsF )
    self.Main.PropertyVideoAlias = 'vs'
    print "Video Alias: %s" % ( self.Main.PropertyVideoAlias )

    self.Main.PropertyLoad
    """
      There is a lot of work behind Property-amalgam and C++, templating in effort to
      make common trait type and value for trait type... 
    """
    self.Main.PropertyShow='VideoHandler', 'fromstring', 'show'
    self.Main.PropertyFrame=36, 'vs', 'get_frame_sec'
    
    

if __name__.__eq__( '__main__' ):
  StrStreamFileNameTest='/media/COMST500GB/temp/349FED09d01_under_water.flv'
  testVideo=VideoImportObject( StrStreamFileName=StrStreamFileNameTest ,
                               VidImportFrameSize=( 640, 480 ),
                               FrameMode='RGB', VideoHandler=Image )
