# dockerized-cronied_github-traffic-stats
Based on https://github.com/nchah/github-traffic-stats , but now dockerized &amp; using cron for pulling data continuously from Github, since Github traffic data only preserved for 14 days.


1. Enter your Github ID and Password in gts_docker_cron.sh
2. Enter your Dropbox access token in config.ini
3. Build your docker image via /docker/dockerfile

4. Done. Run it using /docker/RUN COMMAND on your machine.
