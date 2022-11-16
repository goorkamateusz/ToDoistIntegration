#!/bin/bash

mongosh --port 40250 <<EOF
var config = {
    "_id": "dbrs",
    "version": 1,
    "members": [
        {
            "_id": 1,
            "host": "database0:40250",
            "priority": 3
        },
        {
            "_id": 2,
            "host": "db1:40251",
            "priority": 2
        },
        {
            "_id": 3,
            "host": "db2:40252",
            "priority": 1
        }
    ]
};
rs.initiate(config, { force: true });
rs.status();
EOF
