
if ! command -v docker
then
    echo "Docker not installed"
    exit 1
fi

if ! command -v docker compose
then
    echo "Docker compose not installed"
    exit 1
fi

docker compose up --build -d
