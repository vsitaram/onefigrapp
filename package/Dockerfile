FROM python:3.6-buster

# update the packages
RUN apt update

# Create the run user and group
RUN addgroup --gid 1000 webservice && adduser -q --uid 1000 --gid 1000 --disabled-login webservice

# set the timezone appropriatly
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install the application requirements
COPY package/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Specify home 
ENV APP_HOME /onefigrapp
WORKDIR $APP_HOME

# install the application
ADD . $APP_HOME

# Update permissions
RUN chown -R webservice $APP_HOME /home/webservice && chgrp -R webservice $APP_HOME /home/webservice

# Define port and startup script
EXPOSE 8080
CMD scripts/entry.ksh

# Move in other assets
COPY package/container_bash_profile /home/webservice/.profile

# Ensure permissions are correct
RUN chown webservice:webservice /home/webservice/.profile $APP_HOME/scripts/entry.ksh && chmod 755 /home/webservice/.profile $APP_HOME/scripts/entry.ksh

# Add the build tag
ARG BUILD_TAG
RUN test -n "$BUILD_TAG" && touch $APP_HOME/buildtag.build-$BUILD_TAG || touch $APP_HOME/buildtag.build-0

# Specify the user
USER webservice
