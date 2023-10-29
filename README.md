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

~~Use [IFTTT](https://ifttt.com).~~

IFTTT now requires payment.
Google Assistant also started interpreting the command as smart fans which were not configured, overriding the configured key phrases.

The integration does not work anymore, just use the Telegram bot.

## Network Architecture

To make the Flask application accessible over the Internet when the Raspberry Pi is on a home network, configuring port forwarding on the home router is one possible solution.

However, this is not ideal as the home ISP might not assign a fixed IP address. This will then need to be addressed with additional tools like Dynamic DNS to keep a domain name pointed to the correct IP address.

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


