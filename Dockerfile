# This Dockerfile will be used to run a test environment for install-2BG.
FROM ubuntu:24.04

# As root: install packages and create the test user.
# sudo: the playbook uses become. pipx also pulls in python3-venv.
RUN apt-get update \
 && apt-get install -y sudo pipx git curl ca-certificates
RUN useradd -m -s /bin/bash testuser \
 && echo 'testuser:testuser' | chpasswd \
 && usermod -aG sudo testuser

# From here on, everything runs as testuser. Password is "testuser"
USER testuser
ENV PATH="/home/testuser/.local/bin:${PATH}"
RUN pipx install ansible-core

# WORKDIR creates a missing folder as root, so create it as testuser first.
# install.sh writes .venv in this folder.
RUN mkdir /home/testuser/app
WORKDIR /home/testuser/app
COPY --chown=testuser:testuser ansible ./ansible
COPY --chown=testuser:testuser scripts ./scripts
COPY --chown=testuser:testuser install.sh .

CMD ["./install.sh"]