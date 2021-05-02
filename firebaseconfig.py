import os

config = {
  "apiKey": os.getenv('API_KEY'),
  "authDomain": os.getenv('AUTH_DOMAIN'),
  "databaseURL": os.getenv('DATABASE_URL'),
  "projectId": os.getenv('PROJECT_ID'),
  "storageBucket": os.getenv('STORAGE_BUCKET'),
  "messagingSenderId": os.getenv('MESSAGING_SENDER_ID'),
  "measurementId": os.getenv('MEASUREMENT_ID')
}
