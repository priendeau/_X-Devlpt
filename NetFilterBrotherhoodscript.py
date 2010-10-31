import IPy
import datetime, time
import netfilter
from netfilter import table
from netfilter.table import Table
from netfilter.rule import Rule, Match, Target, Extension
import cPickle
from cPickle import Pickler
from cPickle import Unpickler

CreateNetRoute=False
CreateDictRule=False
RuleCreation=False
RuleAppendRoute=False
RuleAppendGateway=False
PicklerFileSave=True
PicklerFileLoad=True

if PicklerFileLoad:
  FhFirewallHandler=open( '/etc/firewall-netfilter-rules.pickle', 'r' )
  BPickler=Unpickler( FhFirewallHandler )
  AobjLoad=BPickler.load( )
  FhFirewallHandler.close()
  NetRoute=AobjLoad['NetRoute']
  dictRule=AobjLoad['dictRule']

if CreateNetRoute:
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

if CreateDictRule:
  dictRule={
    'table':{
      'filter':{
        'object':Table('filter'),
        'rule_gateway':{ 'clear':[],'block':[] },
        'rule_route':{ 'clear':[],'block':[] } } } }

### This section is excempt of Blocking, Clearing a path, because we generate rule not yet inserted in a table.
### 
### 

if RuleCreation:
  for ItemKeyGateway in NetRoute['gateway'].keys():
    for IpAddr in NetRoute['gateway'][ItemKeyGateway]['ip']:
      StrIpAddr=str(IpAddr)
      #for ItemExChKey in NetRoute['gateway'][ItemKeyGateway].keys():
      RuleKey=NetRoute['gateway'][ItemKeyGateway]['rule']
      if RuleKey == 'clear':
  ##      ClearRule=Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 1:1024')], source=str(IpAddr), jump='ACCEPT' )
        dictRule['table']['filter']['rule_gateway'][ RuleKey ].append( Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 1:1024')], source=StrIpAddr, jump='ACCEPT' ) )
        dictRule['table']['filter']['rule_gateway'][ RuleKey ].append( Rule( in_interface='eth0', protocol='udp', matches=[Match('udp', '--dport 1:1024')], source=StrIpAddr, jump='ACCEPT' ) )
      if RuleKey == 'block':
  ##      BlockRule=Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 80')], source=str(IpAddr), jump='DROP' )
        dictRule['table']['filter']['rule_gateway'][ RuleKey ].append( Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 1:1024')], source=StrIpAddr, jump='DROP' ) )
        dictRule['table']['filter']['rule_gateway'][ RuleKey ].append( Rule( in_interface='eth0', protocol='udp', matches=[Match('udp', '--dport 1:1024')], source=StrIpAddr, jump='DROP' ) )

### This section is excempt of Blocking, Clearing a path, because we generate rule not yet inserted in a table.
### 
###
if RuleAppendRoute:
  for ItemRouteKey in NetRoute['route'].keys():
    for ItemAsName in NetRoute['route'][ItemRouteKey].keys():
      for ItemExchPoint in NetRoute['route'][ItemRouteKey][ItemAsName].keys():
        for IpAddr in NetRoute['route'][ItemRouteKey][ItemAsName][ItemExchPoint]['ip']:
          StrIpAddr=str(IpAddr)
          RuleKey=NetRoute['route'][ItemRouteKey][ItemAsName][ItemExchPoint]['rule']
          if RuleKey == 'clear':
            dictRule['table']['filter']['rule_route'][ RuleKey ].append( Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 1:1024')], source=StrIpAddr, jump='ACCEPT' ) )
            dictRule['table']['filter']['rule_route'][ RuleKey ].append( Rule( in_interface='eth0', protocol='udp', matches=[Match('udp', '--dport 1:1024')], source=StrIpAddr, jump='ACCEPT' ) )
          if RuleKey == 'block':
            dictRule['table']['filter']['rule_route'][ RuleKey ].append( Rule( in_interface='eth0', protocol='tcp', matches=[Match('tcp', '--dport 1:1024')], source=StrIpAddr, jump='DROP' ) )
            dictRule['table']['filter']['rule_route'][ RuleKey ].append( Rule( in_interface='eth0', protocol='udp', matches=[Match('udp', '--dport 1:1024')], source=StrIpAddr, jump='DROP' ) )


if RuleAppendGateway:
  for ItemGateway in [ 'rule_gateway', 'rule_route' ]:
    for ItemStatement in [ 'clear', 'block', ]:
      for ItemStreamPermeability in dictRule['table']['filter'][ItemGateway][ItemStatement]:
        #print "%s, %s Type( %s )" %( ItemGateway, ItemStatement , type(ItemStreamPermeability) )
        dictRule['table']['filter']['object'].append_rule('INPUT', ItemStreamPermeability )
   

if PicklerFileSave:
  FhFirewallHandler=open( '/etc/firewall-netfilter-rules.pickle', 'w' )
  APickler=Pickler( FhFirewallHandler, 2 )
  APickler.dump( { 'NetRoute':NetRoute , 'dictRule':dictRule } )
  FhFirewallHandler.close()




