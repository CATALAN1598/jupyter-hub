c = get_config()
c.Authenticator.allowed_users = {'user1', 'user2', 'user3'}

c.Authenticator.admin_users = {'admin_user'}

c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'

