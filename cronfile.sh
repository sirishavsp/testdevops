#!/bin/bash

# Variables
SERVER1_FOLDER="/home/ubuntu/siri"
SERVER2_FOLDER="/home/ubuntu/siri/backups"
SERVER2_USER="Ubuntu"
SERVER2_IP="3.88.206.133"

# Use rsync to copy files
rsync -azP -e ssh $SERVER1_FOLDER $SERVER2_USER@$SERVER2_IP:$SERVER2_FOLDER

