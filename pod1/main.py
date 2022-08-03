import os
import requests
import time
import subprocess

service_url = os.environ["URL"]
# client_url = "http://pod2-service:3000"
client_url = f"http://{service_url}:3000"
print(client_url)

# client_url = "http://0.0.0.0:3005"

wait_time = int(os.environ["WAIT_TIME"])

while True:
    time.sleep(wait_time)
    response = requests.get(client_url, params={"msg":"hello world"})
    print(response.content.decode())
