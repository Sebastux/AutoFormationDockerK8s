FROM fedora:44
LABEL authors="Sebastux"
LABEL version="1.0"
LABEL commentaire="Conteneur de compilation de script python avec ou sans pyside 6."

ARG USER_ID=1001
ARG GROUP_ID=1001
ARG USER_NAME="compile"
ARG USER_GROUP="${USER_NAME}"
ENV HOME="/home/${USER_NAME}"


RUN dnf clean all && dnf update -y && dnf group install -y "c-development" && \
    dnf install -y python3 python3-devel python3-pip \
    mesa-libGL libX11 libXcomposite libXcursor libXdamage \
    libXext libXfixes libXi libXrandr libXrender libXtst \
    fontconfig nss libXrandr alsa-lib glib2-devel python3-devel patchelf ccache && \
    dnf clean all

RUN groupadd -g "${GROUP_ID}" "${USER_GROUP}" && useradd -l -u "${USER_ID}" "${USER_NAME}" -g "${USER_GROUP}" -m -s /bin/bash -c "Compte de compilation."
# RUN useradd -l -u "${USER_ID}" "${USER_NAME}" -g "${USER_GROUP}" -m -s /bin/bash -c "Compte de compilation."

RUN pip install --upgrade --no-cache-dir pip setuptools wheel && pip install --no-cache-dir nuitka PySide6

USER ${USER_NAME}
WORKDIR ${HOME}
RUN echo "alias ll='ls -lh'" >> ${HOME}/.bashrc