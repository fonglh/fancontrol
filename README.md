# RF Fan Control with a Raspberry PI

Documentation is a work in progress. Here are links to most of the resources used.

## Resources
https://hackernoon.com/diy-home-automation-fan-control-with-raspberry-pi-3-rf-transmitter-and-homebridge-59ad24845770

http://stevenhickson.blogspot.com/2015/02/control-anything-electrical-with.html

https://pinout.xyz/

**Most useful tutorial**

https://www.instructables.com/id/Super-Simple-Raspberry-Pi-433MHz-Home-Automation/

#### Flask Server

https://docs.dataplicity.com/docs/control-gpios-using-rest-api

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04

#### Google Assistant to Webhook

Use [IFTTT](https://ifttt.com).

## Installed on Pi

```
sudo apt install python3-pip
sudo pip3 install Flask
sudo pip3 install Flask-API
sudo pip3 install python-dotenv
sudo pip3 install uwsgi
sudo pip3 install python-telegram-bot
```

## Installed on Public facing web server

```
sudo apt install nginx
```

Install [certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx.html).


