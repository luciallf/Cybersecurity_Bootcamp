FROM debian
# Instalar paquetes necesarios
RUN apt-get update -y && apt upgrade -y
RUN apt-get install nginx tor openssh-server sudo vim -y 
# Crear usuario ft_onion

COPY index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf
COPY torrc /etc/tor/torrc
COPY sshd_config /etc/ssh/sshd_config

COPY service_init.sh .
RUN chmod +x service_init.sh

RUN useradd -m lucia
RUN echo "lucia:123456" | chpasswd

RUN sudo mkdir -p /home/lucia/.ssh
RUN sudo chmod 700 /home/lucia/.ssh
#COPY rickroll-roll.gif /var/www/html/

RUN groupadd sshusers
RUN usermod -aG sshusers lucia
RUN usermod -aG sudo lucia

# Iniciar servicios
#CMD service ssh start && nginx -g 'daemon off;' && tor
CMD ["sh", "service_init.sh"]