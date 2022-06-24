
from custom_sso_security_manager import CustomSsoSecurityManager
from flask_appbuilder.security.manager import AUTH_OAUTH
from replace_vars import CLIENT_ID, CLIENT_SECRET

CUSTOM_SECURITY_MANAGER = CustomSsoSecurityManager

AUTH_TYPE = AUTH_OAUTH
OAUTH_PROVIDERS = [
    {   'name':'google',
        'token_key':'access_token', # Name of the token in the response of access_token_url
        'icon':'fa-address-card',   # Icon for the provider
        'remote_app': {
            'client_id': CLIENT_ID,  # Client Id (Identify Superset application)
            'client_secret': CLIENT_SECRET, # Secret for this Client Id (Identify Superset application)
            'client_kwargs':{
                'scope': 'email profile'               # Scope for the Authorization
            },
            'access_token_method':'POST',    # HTTP Method to call access_token_url
            'access_token_params':{        # Additional parameters for calls to access_token_url
            },
            'access_token_headers':{    # Additional headers for calls to access_token_url
                'Authorization': 'Basic Base64EncodedClientIdAndSecret'
            },
            'api_base_url':'https://www.googleapis.com/oauth2/v2/',
            'access_token_url':'https://oauth2.googleapis.com/token',
            'authorize_url':'https://accounts.google.com/o/oauth2/auth'
        }
    }
]

# Will allow user self registration, allowing to create Flask users from Authorized User
AUTH_USER_REGISTRATION = True

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Admin"
# After create first user, highly recommend to change to "Public"
# AUTH_USER_REGISTRATION_ROLE = "Public"

CACHE_TYPE = "RedisCache"
# correspond to redis's service name in docker-compose.yaml
CACHE_REDIS_HOST = "redis"

DATA_CACHE_CONFIG = {
    "CACHE_TYPE": "SupersetMetastoreCache",
    "CACHE_KEY_PREFIX": "superset_results",  # make sure this string is unique to avoid collisions
    "CACHE_DEFAULT_TIMEOUT": 86400,  # 60 seconds * 60 minutes * 24 hours
}
