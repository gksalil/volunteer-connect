
"""
 Covid Volunteers Aggregator Bot Pluggin class

   Copyright (C) 2007-2017 Free Software Foundation, Inc.
   Contributed by : Salil G K <gksalil@gmail.com>
   Contributed by :

   This file is part of Covid Volunteers Aggregator Bot
"""

class SiteConfig(object):

    site_config={}
    
    sites = ['blr', 'chen', 'hyd']
    servs = ['ambulance', 'blood', 'oxygen']
    
    def add_siteconfig(self, site, service, action):
        if site not in self.sites or service not in self.servs:
            # Log here
            return False
    
        if site in self.site_config.keys():
            self.site_config[site][service] = action
        else:
            self.site_config[site] = {}
            self.site_config[site][service] = action
        return True
       
    def get_siteconfig(self, site, service):
        if site in self.site_config.keys() and service in self.site_config[site].keys() :
            return self.site_config[site][service] 
    
"""    

B='blr'
C='chen'
H='hyd'

S1='ambulance'
S2='blood'

a1='TRUE'
a2='FALSE'
a3='TRUE'

sitecfg = SiteConfig()

print sitecfg.get_siteconfig(B,S1)
print 1

# reading google sheet and populate the dictionary
sitecfg.add_siteconfig(B,S1,a1)

print sitecfg.get_siteconfig(B,S1)
print 2
sitecfg.add_siteconfig(C,S1,a3)
print sitecfg.get_siteconfig(C,S1)
print 3
if sitecfg.get_siteconfig(C, S1): 
  print "YES " + sitecfg.get_siteconfig(C,S1)
else:
  print "NO"
if sitecfg.get_siteconfig(C, S2):
  print "YES"
else:
  print "NO"

"""    
