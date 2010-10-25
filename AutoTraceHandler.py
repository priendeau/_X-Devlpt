import sys, os, re, cStringIO, cPickle, iterpipes, thread ,PIL, datetime, time
from iterpipes import cmd, bincmd, linecmd, run, call, check_call, cmdformat, compose
from socket import *


"""
    This Prototype Implementation will use simple iterpipes-access, future release will add sucessfully
    The Normal Link Librayry with Swig wrapper and next to it, a Pyrex... 
"""


  
@classmethod
def ImageInput( cls ):
  print ImageInput.__name__
  cls.ImageInputHandler( cls )
  
@classmethod
def ImageOutput( cls ):
  print ImageOutput.__name__
  cls.ImageOutputHandler( cls )

@classmethod
def HexNumber( cls ):
  print HexNumber.__name__
  cls.HexNumberHandler( cls )

@classmethod
def AngleNumber( cls ):
  print AngleNumber.__name__
  cls.AngleNumberHandler( cls )

@classmethod
def ImageInputString( cls ):
  print ImageInputString.__name__
  cls.ImageInputStringHandler( cls )

class DecoratorAutotrace:

  DictReference={
    'Error':{
      'Handler':False, 'Name':[ None ] } }
  
  @staticmethod
  def TimerImplement( ClassName,  AttrNameProcHwnd ):
    
    """
    This Decorator Will:
    - Create a variable funcName being assigned automatically to funcName the FunctionName

    The marshaller computes a key from function arguments
    """
    def decorator(func):
        def inner(*args, **kwargs):
          if not func.__name__ in getattr( ClassName , AttrNameProcHwnd ).keys():
            getattr( ClassName, AttrNameProcHwnd )[func.__name__]=list()
          else:
            getattr( ClassName, AttrNameProcHwnd )[func.__name__].append( time.time() )
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
  
class AutoTraceFactory( object ):
  DictReference={ 'name':'dict',
                  'value':[ 'PropertyReference' ],
                  'dict':{ 'name':'type',
                           'value':[ 'hexadecimal','bool', 'unsigned', 'angle-in-degrees', 'real', 'string-filename',
                                     'image-input-format', 'image-output-format'],
                           'hexadecimal':{ 'name':'HexNumber',
                                           'type':type(int()) ,
                                           'range':[0,65535],
                                           'value':[ 'background-color' ] },
                             'bool':{ 'name':'bool',
                                      'type':type(bool()),
                                      'range':[True,False],
                                      'value':[ 'centerline', 'log','preserve-width','remove-adjacent-corners','report-progress','debug-arch','debug-bitmap' ] },
                             'unsigned':{'name':'int',
                                         'type':type(int()) ,
                                         'value':[ 'color-count','corner-surround','despeckle-level','dpi','filter-iterations' ] },
                             'angle-in-degrees':{ 'name':'AngleNumber',
                                                  'type':type(int()) ,
                                                  'value':[ 'corner-always-threshold', 'corner-threshold' ] },
                             'real':{ 'name':'float',
                                      'type':type(float()) ,
                                      'value':[ 'despeckle-tightness','error-threshold','line-reversion-threshold','line-threshold','width-weight-factor' ] },
                             'string-filename':{ 'name':'str',
                                                 'type':type(str()) ,
                                                 'value':[ 'input-name','output-file' ] },
                             'image-input-format':{ 'name':'ImageInputString',
                                                    'type':'ImageInput' ,
                                                    'value':[ 'png', 'tga', 'pbm', 'pnm', 'pgm', 'ppm' , 'bmp' ] },
                             'image-output-format':{ 'name':'str',
                                                     'type':'ImageOutout' ,
                                                     'value':[ 'eps', 'ai', 'p2e', 'sk', 'svg', 'fig', 'emf', 'mif', 'er', 'dxf', 'epd', 'pdf', 'cgm','magick', 'idraw', 'obj', 'tgif', 'gnuplot', 'svm', 'tk', 'gschem', 'pcbfill', 'pcb', 'pcb', 'pcbi', 'hpgl', 'pic','xml', 'noixml', 'tex', 'latex2e', 'm', 'mma', 'asy', 'mp', 'mpost', 'txt', 'text','kil', 'java2', 'java', 'java1', 'rpl', 'rib', 'lwo', 'meta', 'gmfa', 'meta', 'gmfb', 'plot', 'pnm', 'plot-pnm', 'pcl', 'plot-pcl', 'hpgl', 'plot-hpgl', 'tek', 'plot-tek' ,'dr2d' ] }
                             } }
                             
  ProcAccessTime={ }          
  PropertyReference={ 'input-name':None,
                      'background-color':None,
                      'centerline':None,
                      'color-count':None,
                      'corner-always-threshold':None,
                      'corner-surround':None,
                      'corner-threshold':None,
                      'despeckle-level':None,
                      'despeckle-tightness':None,
                      'dpi':None,
                      'error-threshold':None,
                      'filter-iterations':None,
                      'input-format':None,
                      'line-reversion-threshold':None,
                      'line-threshold':None,
                      'list-output-formats':None,
                      'list-input-formats':None,
                      'log':None,
                      'output-file':None,
                      'output-format':None,
                      'preserve-width':None,
                      'remove-adjacent-corners':None,
                      'tangent-surround':None,
                      'report-progress':None,
                      'debug-arch':None,
                      'debug-bitmap':None,
                      'version':None,
                      'width-weight-factor':None }


class AutoTraceProperty( object ):
  
  @DecoratorAutotrace.TimerImplement( AutoTraceFactory , 'ProcAccessTime' )
  def ImageInputHandler( self ):
    print "Entry..."

  @DecoratorAutotrace.TimerImplement( AutoTraceFactory , 'ProcAccessTime' )
  def ImageOutputHandler( self ):
    print "Entry..."

  @DecoratorAutotrace.TimerImplement( AutoTraceFactory , 'ProcAccessTime' )
  def HexNumberHandler( self  ):
    print "Entry..."

  @DecoratorAutotrace.TimerImplement( AutoTraceFactory , 'ProcAccessTime' )
  def AngleNumberHandler( self ):
    print "Entry..."

  @DecoratorAutotrace.TimerImplement( AutoTraceFactory , 'ProcAccessTime' )
  def ImageInputStringHandler( self ):
    print "Entry..."

class AutotraceHandler():

  @DecoratorAutotrace.ParseTheKargs( AutoTraceFactory , None, None  )
  def __init__( self ):
    print "Creating Instance %s" % ( self.__class__.__name__ )


if __name__.__eq__( '__main__' ):
  AAutotraceObj=AutoTraceProperty()
  
""" 'bool', 'unsigned', 'angle-in-degrees', 'real', 'string-filename',  ,'image-input-format':['png', 'tga', 'pbm', 'pnm', 'pgm', 'ppm' , 'bmp']
'image-output-format':['eps', 'ai', 'p2e', 'sk', 'svg', 'fig', 'emf', 'mif', 'er', 'dxf', 'epd', 'pdf', 'cgm','magick', 'idraw', 'obj', 'tgif', 'gnuplot', 'svm', 'tk', 'gschem', 'pcbfill', 'pcb', 'pcb', 'pcbi', 'hpgl', 'pic','xml', 'noixml', 'tex', 'latex2e', 'm', 'mma', 'asy', 'mp', 'mpost', 'txt', 'text','kil', 'java2', 'java', 'java1', 'rpl', 'rib', 'lwo', 'meta', 'gmfa', 'meta', 'gmfb', 'plot', 'pnm', 'plot-pnm', 'pcl', 'plot-pcl', 'hpgl', 'plot-hpgl', 'tek', 'plot-tek' ,'dr2d']
,,,,
Options:<input_name> should be a supported image.
  You can use `--' or `-' to start an option.
  You can use any unambiguous abbreviation for an option name.
  You can separate option names and values with `=' or ` '.

background-color <hexadezimal>: the color of the background that
  should be ignored, for example FFFFFF;
  default is no background color.

centerline: trace a character's centerline, rather than its outline.

color-count <unsigned>: number of colors a color bitmap is reduced to,
  it does not work on grayscale, allowed are 1..256;
  default is 0, that means not color reduction is done.

corner-always-threshold <angle-in-degrees>: if the angle at a pixel is
  less than this, it is considered a corner, even if it is within
  `corner-surround' pixels of another corner; default is 60.

corner-surround <unsigned>: number of pixels on either side of a
  point to consider when determining if that point is a corner;
  default is 4.

corner-threshold <angle-in-degrees>: if a pixel, its predecessor(s),
  and its successor(s) meet at an angle smaller than this, it's a
  corner; default is 100.

despeckle-level <unsigned>: 0..20; default is no despeckling.

despeckle-tightness <real>: 0.0..8.0; default is 2.0.

dpi <unsigned>: The dots per inch value in the input image, affects scaling
  of mif output image

error-threshold <real>: subdivide fitted curves that are off by
  more pixels than this; default is 2.0.

filter-iterations <unsigned>: smooth the curve this many times
  before fitting; default is 4.

input-format:  PNG, TGA, PBM, PNM, PGM, PPM or BMP. 

help: print this message.

line-reversion-threshold <real>: if a spline is closer to a straight
  line than this, weighted by the square of the curve length, keep it a
  straight line even if it is a list with curves; default is .01.

line-threshold <real>: if the spline is not more than this far away
  from the straight line defined by its endpoints,
  then output a straight line; default is 1.

list-output-formats: print a list of support output formats to stderr.

list-input-formats:  print a list of support input formats to stderr.

log: write detailed progress reports to <input_name>.log.

output-file <filename>: write to <filename>

output-format <format>: use format <format> for the output file
  eps, ai, p2e, sk, svg, fig, emf, mif, er, dxf, epd, pdf, cgm, ..., magick, idraw, obj, tgif, gnuplot, svm, tk, gschem, pcbfill, pcb, pcb, pcbi, hpgl, pic, xml, noixml, tex, latex2e, m, mma, asy, mp, mpost, txt, text, kil, java2, java, java1, rpl, rib, lwo, meta, gmfa, meta, gmfb, plot, pnm, plot-pnm, pcl, plot-pcl, hpgl, plot-hpgl, tek, plot-tek or dr2d can be used.

preserve-width: whether to preserve line width prior to thinning.

remove-adjacent-corners: remove corners that are adjacent.

tangent-surround <unsigned>: number of points on either side of a
  point to consider when computing the tangent at that point; default is 3.

report-progress: report tracing status in real time.

debug-arch: print the type of cpu.

debug-bitmap: dump loaded bitmap to <input_name>.bitmap.

version: print the version number of this program.

width-weight-factor <real>: weight factor for fitting the linewidth.

"""
