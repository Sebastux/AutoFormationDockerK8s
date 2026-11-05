FROM fedora:45
LABEL authors="Sebastux"
LABEL version="1.0.0"
LABEL commentaire="Conteneur webmin."

RUN dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm && \
    dnf clean all && dnf update -y

 RUN dnf install -y wget2 bind9-next bind9-next-dnssec-utils bind9-next-libs bind9-next-libs && \
     dnf install -y https://sourceforge.net/projects/webadmin/files/webmin/2.670/webmin-2.670-1.noarch.rpm


RUN echo "alias ll='ls -lh'" >> /root/.bashrc

EXPOSE 10000

CMD ["/usr/libexec/webmin/miniserv.pl", "/etc/webmin/miniserv.conf"]
