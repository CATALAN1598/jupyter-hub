# Set image
FROM quay.io/jupyterhub/jupyterhub:latest
WORKDIR /srv/jupyterhub/

# Install dependencies
COPY requirements.txt /srv/jupyterhub/requirements.txt
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

RUN /srv/venv/bin/pip install --no-cache-dir -r requirements.txt
RUN /srv/venv/bin/python3 -m bash_kernel.install

# Set user  
RUN useradd jupyter --home /home/jupyter --create-home --shell /bin/bash
RUN useradd adminhub --home /home/adminhub --create-home --shell /bin/bash



