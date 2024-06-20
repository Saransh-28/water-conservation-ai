import requests

url = ''

def trigger_door_alert(data):
  try:
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response
  except requests.exceptions.RequestException as e:
    print(f"Error sending data to {url}: {e}")
    return None