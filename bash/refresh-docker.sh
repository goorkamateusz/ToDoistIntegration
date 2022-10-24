docker build -t todoist-integration:latest .;

containerId=`docker ps -qaf name=todoist-integration`;

[ -z $containerId ] || docker stop $containerId;
[ -z $containerId ] || docker rm $containerId;

docker run -d -p 5100:5100 --name todoist-integration --restart always todoist-integration;
