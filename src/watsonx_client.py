import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_access_token():
    api_key = os.getenv("WATSONX_API_KEY")
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={api_key}"
    
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

def generate_text(prompt):
    try:
        token = get_access_token()
        project_id = os.getenv("WATSONX_PROJECT_ID")
        url = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29")
        
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        
        body = {
            "input": prompt,
            "parameters": {
                "decoding_method": "greedy",
                "max_new_tokens": 1500,
                "temperature": 0.7,
                "stop_sequences": []
            },
            "model_id": "ibm/granite-13b-chat-v2",
            "project_id": project_id
        }
        
        response = requests.post(url, headers=headers, json=body)
        return response.json()["results"][0]["generated_text"]
    
    except Exception as e:
        print(f"API Error: {e}")
        return None

# Made with Bob
