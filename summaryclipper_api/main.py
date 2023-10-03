from service.app import application
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=os.getenv("PORT"))
