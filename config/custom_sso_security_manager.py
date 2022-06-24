import logging
from superset.security import SupersetSecurityManager
from replace_vars import DOMAINS

ALLOW_DOMAINS = DOMAINS


class CustomSsoSecurityManager(SupersetSecurityManager):
    """
    Google UserInfo response sample
{ 
  'id': '1234456789', 
  'email': 'xxxxxx@hoge.jp', 
  'verified_email': True, 
  'name': 'John Smith', 
  'given_name': 'Jon', 
  'family_name': 'Smith', 
  'picture': 'https://lh3.googleusercontent.com/a/aaaaaaa', 
  'locale': 'ja', 
  'hd': 'xxxxx.jp'
}
"""

    def oauth_user_info(self, provider, response=None):
        logging.debug("Oauth2 provider: {0}.".format(provider))
        if provider == 'google':
            me = self.appbuilder.sm.oauth_remotes[provider].get('userinfo').json()
            logging.debug("user_data: {0}".format(me))
            if ALLOW_DOMAINS is not None:
                if me['hd'] not in ALLOW_DOMAINS:
                    logging.warn('Not allowed domain %s' % (me["hd"]))
                    logging.info("user_data: {0}".format(me))
                    raise Exception("Not allowed domain %s" % (me["hd"]))
            return { 
                'name' : me['name'], 
                'email' : me['email'], 
                'id' : me['id'], 
                'username' : me['email'], 
                'first_name':me['given_name'], 
                'last_name':me['family_name']
            }
    
