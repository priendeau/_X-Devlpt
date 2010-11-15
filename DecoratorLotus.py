import os, sys, re


"""

  Class : DecoratorLotus
  Desc  : A Decorator to integrate facilities like **Kargs, multi-variables parsing and some other implemented
  Action like Time registration and process control.

"""

class DecoratorLotus:

  InnerClassName=None 
  @classmethod
  def EntryFuncDisplay( cls,  FlagName ):
    
    """
    This Decorator Will:
    - 

    
    """
    def decorator(func):
        def inner(*args, **kwargs):
          print "entry in Func %s, from Inner class configured to %s " % ( func.__name__, cls.InnerClassName.__name__  )
          func( *args, **kwargs )
        return inner
    return decorator

  @classmethod
  def SurveyStatFlags( cls,  FlagName ):
    
    """
    This Decorator Will:
    - Report if Attr configured within definition function, will enter inside a definition simply bypass
    te function.

    
    """
    def decorator(func):
        def inner(*args, **kwargs):
          AttrStatement=None
          #print "entry in Func %s, from Inner class configured to %s " % ( func.__name__, cls.InnerClassName.__name__  )
          if hasattr( cls.InnerClassName, FlagName ):
            AttrStatement=getattr( cls.InnerClassName , FlagName )
            #print "Is Attr : %s, %s" %( FlagName, AttrStatement )
            if AttrStatement:
              func( *args, **kwargs )
            #else:
            #  print "Function %s is not executed for Attr decl. set to %s." % ( func.__name__ , AttrStatement ) 
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
          for ItemKeyName in kwargs.keys( ):
            print "Adding key, %s, value: %s" % ( ItemKeyName, kwargs[ItemKeyName] )
            if ShelveObject != None:
              setattr( getattr( ClassName, ShelveObject ), ItemKeyName, kwargs[ItemKeyName] )
            if ShelveObject == None:
              setattr( ClassName, ItemKeyName, kwargs[ItemKeyName] )
          func( *args, **kwargs )
        return inner
    return decorator

  def __init__( self, InnerName ):
    self.InnerClassName = InnerName.__name__
