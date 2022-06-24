Sample to run Apache SuperSet with Google SSO.


# Preparation

## Create OAuth 2.0 Client ID on GCP

Create your OAuth web service and get api keys on GCP Console.
You must set redirect url to `http://localhost:8080/oauth-authorized/google`.

## Set client_id and client_secret to superset_config.py

Then you set client_id and client_secret to config/superset_config.py

## Set allow domains

Modify config/custom_sso_security_manager.py ALLOW_DOMAINS constant to your Google workspace domain.


## Build and run 

```
docker-compose up
```

Then access to http://localhost:8080