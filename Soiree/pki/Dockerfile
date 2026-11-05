FROM ubuntu:24.04
LABEL authors="Sebastux"
LABEL version="1.0"
LABEL commentaire="Conteneur de compilation de script python avec ou sans pyside 6."

ARG USER_ID=1001
ARG GROUP_ID=1001
ARG USER_NAME="compile"
ARG USER_GROUP="${USER_NAME}"
ENV HOME="/home/${USER_NAME}"


RUN apt-get update && apt-get upgrade -y; apt-get install -y build-essential python3 python3-dev python3-pip libgl1 \
    libx11-6 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxtst6 \
    fontconfig libnss3 libasound2t64 libglib2.0-dev python3-venv patchelf ccache && rm -rf /var/lib/apt/lists/*

RUN groupadd -g "${GROUP_ID}" "${USER_GROUP}" && useradd -l -u "${USER_ID}" "${USER_NAME}" -g "${USER_GROUP}" -m -s /bin/ \
    bash -c "Compte de compilation."

# RUN pip install --upgrade --no-cache-dir pip setuptools wheel && pip install --no-cache-dir nuitka PySide6

USER ${USER_NAME}
WORKDIR ${HOME}

RUN python3 -m venv venv && ./venv/bin/pip install --upgrade --no-cache-dir pip setuptools wheel && ./venv/bin/pip install --no-cache-dir nuitka PySide6
RUN mkdir "${HOME}/projet" && echo "source ${HOME}/venv/bin/activate" >> ${HOME}/.bashrc && echo "alias ll='ls -lh'" >> ${HOME}/.bashrc
