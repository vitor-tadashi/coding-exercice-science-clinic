import os

# main API endpoint
API_V1 = "/healthcare/v1"

# POSTGRES settings
POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", "localhost")
POSTGRES_USER = os.getenv("POSTGRES_USER", "developer")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "development")
POSTGRES_DB = os.getenv("POSTGRES_DB", "cms")