
if ! command -v docker
then
    echo "Docker not installed"
    return 1
fi

if ! command -v docker compose
then
    sudo apt install docker-compose-plugin
fi

docker compose build
docker compose up -d
