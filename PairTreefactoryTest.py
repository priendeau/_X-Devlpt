# -*- coding: utf-8 -*-
import os, sys, re
from pairtree import *


class PairTreeFactory( object ):

  class PairTreeDomainUpdateFactory( object ):

    class SyntaxIncursionIndexer( object ):
      DictReference={ 'class':{ 'parent':(False) , 'child':(False) },
                          'def':{ 'parent':(False) , 'child':(False) } }
      KeySyntaxClass=None
      KeyParentLevel=None

      def GetSyntaxLevelInspection( self ):
        return self.DictReference[ self.KeySyntaxClass ][ self.KeyParentLevel ]

      def SetSyntaxLevelInspection( self, value ):
        self.KeySyntaxClass, self.KeyParentLevel, NewStateSLI=value
        self.DictReference[ self.KeySyntaxClass ][ self.KeyParentLevel ]=NewStateSLI

      PropertySLI=property( GetSyntaxLevelInspection, SetSyntaxLevelInspection )

    class ConfigHandler( object ):
      DictReference={
        'conf':{
          'path':{
            'search':[ '/usr/local/lib/python2.6/dist-packages' ] },
          'key':{ 'scan_class':(r'(?ui)[\t\ ]?class[\t\ ]?\[a-zA-Z0-9_\-]+[\t\ ]?\([a-zA-Z0-9_\t\ \,\-=]+\)'),
                'scan_def':(r'(?ui)[\t\ ]?def[\t\ ]?[a-zA-Z0-9_\-]+[\t\ ]?\([a-zA-Z0-9_\t\ \,\-=]+\)'),
                'class':(r'(?ui)[\t\ ]?class[\t\ ]?)'),
                'def':(r'(?ui)[\t\ ]?def[\t\ ]?)'),
                'arg':(r'\([a-zA-Z0-9_\t\ \,\-=]+\)') } } }

      RootNodeKey=None
      RootNodeKeyTypeNode=None
      RootNodeKeyTypeNodeName=None
      RootNodeKeyTypeNodeKey=None
      RootNodeValue=None

      def GetKeyNodeType( self ):
        return self.RootNodeValue

      def SetKeyNodeType( self, value ):
        self.RootNodeKeyTypeNodeName=value
        self.RootNodeValue=self.DictReference[ self.RootNodeKey ]

      PropertyKeyNodeType=property( GetKeyNodeRoot, SetKeyNodeRoot )      

      def GetKeyNodeRoot( self ):
        return self.RootNodeValue

      def SetKeyNodeRoot( self, value ):
        self.RootNodeKey=value
        self.RootNodeValue=self.DictReference[ self.RootNodeKey ]

      PropertyKeyNode=property( GetKeyNodeRoot, SetKeyNodeRoot )      

      
    DictReference={ 'class':{ 'type':['scan_class'], 'item':[ 'class', 'arg' ] },
                    'function':{ 'type':['scan_def'], 'item':[ 'def', 'arg' ] },
                    'PairtreeStorageClient':{
                      'filename':[ 'pairtree/pairtree_client.py' ] ,
                      'key':[ 'class', 'function'] } }

    DefaultDictTemplate={ }

    def ReadConf( self ):
      """
        Configuration-reader action.
      """
      
    def StartScanClass( self ):
      """
        Class discovery action.
      """

    def StartScanFunction( self ):
      """
        Function discovery action.
      """

      
    
  Domain={  }
  class PairTreeImpl( object ):
    ActiveGetter=''
    StoreDirInfo="/home/ubuntu/data"
    UriBaseInfo="http://theysaysomethinginterrestingapparentl.blogspot.com/"
    aFactoryPairTree = None
    aFactoryPairTreeStorage=None
    DictReference={ 'dir':{ 'data':( None ) }   }
    

  def __Kargs__( self, **Kargs ):
    for ItemKey in Kargs.keys():
        setattr( self, ItemKey, Kargs[ItemKey] )
        
  def __init__( self , **Kargs ):
    self.__Kargs__( Kargs )


  #aFactoryPairTree.get_store(store_dir=StoreDirInfo, uri_base=UriBaseInfo)
