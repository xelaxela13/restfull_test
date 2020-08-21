FROM node
RUN mkdir -p /home
ENV PROJECT_ROOT /home/restfull
ENV PATH $PATH:$PROJECT_ROOT
RUN mkdir $PROJECT_ROOT
WORKDIR $PROJECT_ROOT
RUN CI=true
#COPY package.json $PROJECT_ROOT
COPY . $PROJECT_ROOT

RUN npm install

EXPOSE 3000
CMD ["npm", "start"]