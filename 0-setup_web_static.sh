#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static. It must:
#     -Install Nginx if it not already installed
#     -Create the folder `/data/` if it doesn’t already exist
#     -Create the folder `/data/web_static/` if it doesn’t already exist
#     -Create the folder `/data/web_static/releases/` if it doesn’t already exist
#     -Create the folder `/data/web_static/shared/` if it doesn’t already exist
#     -Create the folder `/data/web_static/releases/test/` if it doesn’t already exist
#     -Create a fake HTML file `/data/web_static/releases/test/index.html` (with simple
#      content, to test your Nginx configuration)
#     -Create a symbolic link `/data/web_static/current` linked to
#      the `/data/web_static/releases/test/` folder. If the symbolic link already exists, it
#      should be deleted and recreated every time the script is ran.
#     -Give ownership of the `/data/` folder to the `ubuntu` user AND group (you can assume this user
#      and group exist). This should be recursive; everything inside should 
#      be created/owned by this user/group.
#      -Update the Nginx configuration to serve the content of `/data/web_static/current/` to `hbnb_static`
#      (ex: `https://mydomainname.tech/hbnb_static`). Don’t forget to restart Nginx after updating the configuration:
#          Use alias inside your Nginx configuration
#          [Tip](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)

# script to install and setup nginx
CONFIG_FILE="/etc/nginx/sites-available/default"
HOST_NAME=$(hostname)
MY_ID=496
STATIC=/data/web_static

# check if hostname is correct
if [[ $(hostname) =~ ^$MY_ID-web-[0-9]+ ]]; then
    echo 'hostname properly configured'
else
    (>&2 echo 'hostname not configured properly...')
    (>&2 echo 'please set hostname to pattern: 496-web-<server_id>...')
    (>&2 echo 'Example: sudo hostnamectl set-hostname 496-web-<insert_server_id_here>')
fi

# install nginx
apt-get -y update
apt-get -y install nginx

# update 404 error page
echo "Ceci n'est pas une page" > /usr/share/nginx/html/404.html

# create static directories and links
mkdir -p $STATIC/releases/test
mkdir -p $STATIC/shared
echo 'Holberton School Is Running!' > $STATIC/releases/test/index.html
ln -sfn $STATIC/releases/test $STATIC/current
sudo chown -f -R ubuntu:ubuntu /data/

# update config file to redirect
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   $STATIC/current;
    index  index.html index.htm 8-index.html;

    add_header X-Served-By $HOST_NAME;

    location / {
        alias $STATIC/current/;
    }

    location /redirect_me {
        return 301 http://google.com/;
    }

    location /hbnb_static {
        alias $STATIC/current/;
    }

    error_page 404 /404.html;
    location /404 {
      root /usr/share/nginx/html;
      internal;
    }
}" > $CONFIG_FILE

# start nginx after reloading config
service nginx start
# if nginx was already running restart it
service nginx restart
