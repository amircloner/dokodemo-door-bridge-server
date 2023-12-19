#!/usr/bin/python3

import json
from pathlib import Path

# LOAD CONFIG FILES

path = Path(__file__).parent

configPath = str(path.joinpath('config/config.json'))
configFile = open(configPath, 'r', encoding='utf-8')
config = json.load(configFile)

envPath = str(path.joinpath('.env.example'))
envFile = open(envPath, 'r', encoding='utf-8')
env = envFile.read()

# INPUT: SERVER IP

defaultServerIP = config['inbounds'][0]['settings']['address']
if defaultServerIP == '<SERVER-IP>':
    message = "Server Server Hostname:\n"
else:
    message = f"Server Server Hostname: (Leave empty to use `{defaultServerIP}`)\n"

serverIP = input(message)
if serverIP == '':
    serverIP = defaultServerIP

config['inbounds'][0]['settings']['address'] = serverIP

# INPUT: SERVER PORT

defaultServerPort = config['inbounds'][0]['settings']['port']
serverPort = input(f"Server Server Port: (Leave empty to use `{defaultServerPort}`)\n")
if serverPort == '':
    serverPort = defaultServerPort

config['inbounds'][0]['settings']['port'] = int(serverPort)

# SAVE CONFIG FILE

configContent = json.dumps(config, indent=2)
open(configPath, 'w', encoding='utf-8').write(configContent)

# SAVE ENV FILE
envContent = f"V2RAY_PORT={serverPort}\n"
envPath = str(path.joinpath('.env'))
open(envPath, 'w', encoding='utf-8').write(envContent)

# PRINT OUT RESULT

print('Done!')
