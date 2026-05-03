import os
from dotenv import load_dotenv

load_dotenv()

print("=== Configuration Check ===\n")

api_key = os.getenv("WATSONX_API_KEY")
project_id = os.getenv("WATSONX_PROJECT_ID")
use_api = os.getenv("USE_WATSONX_API", "false")

print(f"USE_WATSONX_API: {use_api}")
print(f"API Key present: {'Yes' if api_key else 'No'}")
if api_key:
    print(f"API Key (first 10 chars): {api_key[:10]}...")
print(f"Project ID present: {'Yes' if project_id else 'No'}")
if project_id:
    print(f"Project ID: {project_id}")

print("\n=== Status ===")
if use_api.lower() == "true":
    if api_key and project_id:
        print("✅ Configuration looks good - API mode enabled")
    else:
        print("❌ API mode enabled but credentials missing")
        print("   Please add WATSONX_API_KEY and WATSONX_PROJECT_ID to .env")
else:
    print("ℹ️  Running in MOCK mode (USE_WATSONX_API=false)")

# Made with Bob
