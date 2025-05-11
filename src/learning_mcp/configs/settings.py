from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()


# Define the base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if __name__ == "__main__":
    # Print the base directory for verification
    print(f"Base Directory: {BASE_DIR}")