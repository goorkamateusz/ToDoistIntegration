
docker compose exec database0 mongosh --port 40250 --eval '
var config = {
    "_id": "dbrs",
    "members": [
        { "_id": 1, "host": "database0:40250" },
        { "_id": 2, "host": "db1:40251" },
        { "_id": 3, "host": "db2:40252" }
    ]
};
rs.initiate(config, { force: true });
'

echo "Czekam..."
sleep 10

docker compose exec database0 mongosh --port 40250 --eval 'rs.status();'
