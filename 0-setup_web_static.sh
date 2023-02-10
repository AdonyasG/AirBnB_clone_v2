#!/usr/bin/bash
# configure web servers for deployment
sudo apt-get install nginx
sudo mkdir -p /data/web_static/{shared,releases/test}
echo "<html>
  <head>
  </head>
  <body>
    ALX School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
