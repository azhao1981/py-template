import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(),override=True)

def main():
  response = requests.get('https://ifconfig.me')
  print(response.text)

if __name__ == "__main__":
  main()