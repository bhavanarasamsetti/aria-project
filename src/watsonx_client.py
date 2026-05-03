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
    response.raise_for_status()
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
            "model_id": os.getenv("WATSONX_MODEL_ID", "ibm/granite-13b-instruct-v2"),
            "project_id": project_id
        }
        
        response = requests.post(url, headers=headers, json=body, timeout=120)
        response.raise_for_status()
        
        result = response.json()
        print(f"DEBUG: API Response keys: {result.keys()}")
        
        # Handle different response formats
        if "results" in result:
            return result["results"][0]["generated_text"]
        elif "generated_text" in result:
            return result["generated_text"]
        elif "predictions" in result:
            return result["predictions"][0]["generated_text"]
        else:
            print(f"DEBUG: Full response: {result}")
            raise Exception(f"Unexpected response format: {list(result.keys())}")
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Response: {e.response.text if hasattr(e, 'response') else 'No response'}")
        return None
    except Exception as e:
        print(f"API Error: {e}")
        return None

# Made with Bob
