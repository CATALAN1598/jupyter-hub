c = get_config()
c.Authenticator.allowed_users = {'root'}

c.Authenticator.admin_users = {'adminhub'}

c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'

