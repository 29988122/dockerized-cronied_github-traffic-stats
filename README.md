# dockerized-cronied_github-traffic-stats
Based on https://github.com/nchah/github-traffic-stats , but now dockerized &amp; using cron for pulling data continuously from Github, and upload them to your Dropbox.

Since Github traffic data only preserved for 14 days, this is a necessary cron job.


1. Enter your Github ID and Password in gts_docker_cron.sh
2. Enter your Dropbox access token in config.ini
3. Build your docker image via /docker/dockerfile
4. Done. Run it using /docker/RUN COMMAND on your machine

Docker image can also be found here:
https://hub.docker.com/r/a29988122/dockerized-cronied_github-traffic-stats
