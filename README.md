# Website Template

This Website for { Company Name } and is being developed by MCduBois Web Services, LLC.

## Table of Contents

1. [Installation](#Installation)
2. [Configuration](#Configuration)
3. [Service Control](#Service-Control)

## Installation

- Clone the repository
  - > git clone https://github.com/MichaelCduBois/Website-Template

## Configuration

- Update domain names in Nginx config files
  - [https.conf](Nginx/https.conf)
  - [http.conf](Nginx/http.conf)

- Install Certbot
  - > apt install certbot

- Allow firewall connections on port 80
  - > ufw allow 80

- Create certificate for each domain
  - > certbot certonly --standalone -d {domain}

- Edit crontab configuring for daily expiration checs
  - > crontab -e
  - > @daily certbot renew --pre-hook "docker-compose -f {path/to/docker-compose.yml} down" -- post-hook "docker-compose -f {path/to/docker-compose.yml} up -d"

## Service Control

### Development

> docker-compose -f docker-compose.dev.yml build
> docker-compose -f docker-compsoe.dev.yml up -d

### Production

> docker-compose build
> docker-compose up -d

### Shutdown all containers

> docker-compose down

### Start specific container

> docker-compose start {CONTAINER NAME}

### Stop specific container

> docker-compose stop {CONTAINER NAME}
