import IPy
import datetime, time
import netfilter
from netfilter import table
from netfilter.table import Table
from netfilter.rule import Rule, Match, Target, Extension
import cPickle
from cPickle import Pickler
from cPickle import Unpickler


class DecoratorNetFilter:
  """
  This Decorator Will:
  - Create a variable funcName being assigned automatically to funcName the FunctionName

  The marshaller computes a key from function arguments
  """
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

class NetFilterBrotherhoodScriptFactory( object ):
  dictRule=None
  NetRoute=None
  
  __DictReference__= {
    'CreateNetRoute':False, 
    'CreateDictRule':False,
    'RuleCreation':False,
    'RuleAppendRoute':True,
    'RuleAppendGateway':True,
    'PicklerFileSave':False,
    'PicklerFileLoad':True }
  
  def PicklerFileLoad( self ):
    print "Pickler storage loader." 
    self.FhFirewallHandler=open( '/etc/firewall-netfilter-rules.pickle', 'r' )
    self.BPickler=Unpickler( FhFirewallHandler )
    self.PicklerVarLayer=BPickler.load( )
    for Itemkey in self.PicklerVarLayer.keys():
      setattr( __builtins__, Itemkey , PicklerVarLayer[Itemkey] )


  def CreateNetRoute( self ):
    print "Netroute Dict Storage creation" 
    NetRoute={
      'gateway':{
        'LOCALHOST':{ 'ip':IPy.IP('74.58.250.239'),
                      'rule':'clear'  },
        'LOCAL18-60':{ 'ip':IPy.IP( '74.58.192.0/18' ),
                       'rule':'block' } },
      'route':{
        'vl-mo-dn009-fae1.mo.videotron.ca':{
          'exchange-point':{
            'videotron.ca.':{
              'ip':IPy.IP('24.201.243.21'), 'rule':'clear' },
            'mx.videotron.ca.':{
              'ip':IPy.IP('24.201.245.37'), 'rule':'clear' },
            'vl-mo-dn009-fae1.mo.videotron.ca.':{
              'ip':IPy.IP('24.200.241.2'), 'rule':'clear' },
            'vl-mo-dn010-fae1.mo.videotron.ca.':{
              'ip':IPy.IP('24.200.241.6'), 'rule':'clear' },
            'vl-mo-dn011-fae1.mo.videotron.ca.':{
              'ip':IPy.IP('24.200.241.10'), 'rule':'clear' } } } ,
        'AS5769':{
          'exchange-point':{
            'TorIX':{ 'ip':IPy.IP('198.32.245.3'),
                      'rule':'block' },
            'Equinix New York':{ 'ip':IPy.IP('198.32.118.79'),
                                 'rule':'block' },
            'Equinix Chicago':{ 'ip':IPy.IP('206.223.119.6'),
                                'rule':'clear' },
            'Equinix Ashburn':{ 'ip':IPy.IP('206.223.115.76'),
                                'rule':'clear' } } },
        'AS36231':{
          'exchange-point':{
            'lordi(at)msdi.ca 20051129':{'ip':IPy.IP('64.15.71.0/24'),
                                         'rule':'block'},
            'lordi(at)msdi.ca 20051116':{'ip':IPy.IP('64.18.66.0/23'),
                                         'rule':'block'},
            'lordi(at)msdi.ca 20070712':{'ip':IPy.IP('208.79.112.0/22'),
                                         'rule':'block'} } },
        'AS34655':{
          'exchange-point':{
            'DE-CIX':{ 'ip':IPy.IP('80.81.192.142'),
                       'rule':'block' },
            'AMS-IX':{ 'ip':IPy.IP('195.69.144.150'),
                       'rule':'block' },
            'NL-IX':{ 'ip':IPy.IP('193.239.116.88'),
                      'rule':'block' },
            'BiX':{ 'ip':IPy.IP('193.188.137.134'),
                    'rule':'block' },
            'LINX Brocade LAN':{ 'ip':IPy.IP('195.66.224.210'),
                                 'rule':'block' },
            'CoreSite - Any2 California':{ 'ip':IPy.IP('206.223.143.13'),
                                           'rule':'block' },
            'LINX Extreme LAN':{ 'ip':IPy.IP('195.66.226.210'),
                                 'rule':'block' } } } } }

  def CreateDictRule( self ):
    print "dictRule Dict Storage creation" 
    self.dictRule={
      'table':{
        'filter':{
          'object':Table('filter'),
          'rule_gateway':{
            'clear':[],
            'block':[] },
          'rule_route':{
            'clear':[],
            'block':[]
            }
          }
        }
      }

  ### This section is excempt of Blocking, Clearing a path, because we generate rule not yet inserted in a table.
  ### 
  ### 

  def RuleCreation( self ):
    print "Rule Creation for gateway" 
    for ItemKeyGateway in self.NetRoute['gateway'].keys():
      for IpAddr in self.NetRoute['gateway'][ItemKeyGateway]['ip']:
        StrIpAddr=str(IpAddr)
        #for ItemExChKey in NetRoute['gateway'][ItemKeyGateway].keys():
        RuleKey=self.NetRoute['gateway'][ItemKeyGateway]['rule']
        if RuleKey == 'clear':
    ##      ClearRule=Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 1:1024')], source=str(IpAddr), jump='ACCEPT' )
          self.dictRule['table']['filter']['rule_gateway'][ RuleKey ].append( Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 1:1024')], source=StrIpAddr, jump='ACCEPT' ) )
          self.dictRule['table']['filter']['rule_gateway'][ RuleKey ].append( Rule( in_interface='eth0', protocol='udp', matches=[Match('udp', '--dport 1:1024')], source=StrIpAddr, jump='ACCEPT' ) )
        if RuleKey == 'block':
    ##      BlockRule=Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 80')], source=str(IpAddr), jump='DROP' )
          self.dictRule['table']['filter']['rule_gateway'][ RuleKey ].append( Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 1:1024')], source=StrIpAddr, jump='DROP' ) )
          self.dictRule['table']['filter']['rule_gateway'][ RuleKey ].append( Rule( in_interface='eth0', protocol='udp', matches=[Match('udp', '--dport 1:1024')], source=StrIpAddr, jump='DROP' ) )

  ### This section is excempt of Blocking, Clearing a path, because we generate rule not yet inserted in a table.
  ### 
  ###
  def RuleAppendRoute( self ):
    print "Rule Creation for route" 
    for ItemRouteKey in self.NetRoute['route'].keys():
      for ItemAsName in self.NetRoute['route'][ItemRouteKey].keys():
        for ItemExchPoint in self.NetRoute['route'][ItemRouteKey][ItemAsName].keys():
          for IpAddr in self.NetRoute['route'][ItemRouteKey][ItemAsName][ItemExchPoint]['ip']:
            StrIpAddr=str(IpAddr)
            self.RuleKey=self.NetRoute['route'][ItemRouteKey][ItemAsName][ItemExchPoint]['rule']
            if self.RuleKey == 'clear':
              self.dictRule['table']['filter']['rule_route'][ RuleKey ].append( Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 1:1024')], source=StrIpAddr, jump='ACCEPT' ) )
              self.dictRule['table']['filter']['rule_route'][ RuleKey ].append( Rule( in_interface='eth0', protocol='udp', matches=[Match('udp', '--dport 1:1024')], source=StrIpAddr, jump='ACCEPT' ) )
            if self.RuleKey == 'block':
              self.dictRule['table']['filter']['rule_route'][ RuleKey ].append( Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 1:1024')], source=StrIpAddr, jump='DROP' ) )
              self.dictRule['table']['filter']['rule_route'][ RuleKey ].append( Rule( in_interface='eth0', protocol='udp', matches=[Match('udp', '--dport 1:1024')], source=StrIpAddr, jump='DROP' ) )


  def RuleAppendGateway( self ):
    print "Appending Gateway rules" 
    for ItemGateway in [ 'rule_gateway', 'rule_route' ]:
      for ItemStatement in [ 'clear', 'block', ]:
        for ItemStreamPermeability in self.dictRule['table']['filter'][ItemGateway][ItemStatement]:
          #print "%s, %s Type( %s )" %( ItemGateway, ItemStatement , type(ItemStreamPermeability) )
          self.dictRule['table']['filter']['object'].append_rule('INPUT', ItemStreamPermeability )
   

  def PicklerFileSave( self ):
    print "Pickler storage saver." 
    self.FhFirewallHandler=open( '/etc/firewall-netfilter-rules.pickle', 'w' )
    self.APickler=Pickler( FhFirewallHandler, 2 )
    self.APickler.dump( { 'NetRoute':NetRoute , 'dictRule':dictRule } )
    self.FhFirewallHandler.close()

class NetFilterBrotherhoodMClass( object ):
  __metaclass__ = MClass
  
  Factory=NetFilterBrotherhoodScriptFactory()


class NetFilterBSI( object ):

  @DecoratorNetFilter.InstanceFuncMessage( "Creating Instance" )
  def InitCall( self ):
    for item in Factory.__DictReference__.keys():
      print "Statement of Keys %s : %s "% ( Factory.__DictReference__[item] )
    return True
  
  @DecoratorNetFilter.ParseTheKargs( NetFilterBrotherhoodMClass , None, None )
  def __init__( self, **Kargs ):
    self.InitCall( )

if __name__.__eq__( '__main__' ):
  NetFilterObj=NetFilterBSI() 
