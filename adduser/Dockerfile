# Set image
FROM camsae/jupyter-hub:latest
WORKDIR /srv/jupyterhub/

# Copy jupyter-hub config
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# Set user (do not forget to add the users to the jupyterhub_config.py to allow acces)
RUN useradd user1 --home /home/user1 --create-home --shell /bin/bash
RUN useradd user2 --home /home/user2 --create-home --shell /bin/bash
RUN useradd user3 --home /home/user3 --create-home --shell /bin/bash



