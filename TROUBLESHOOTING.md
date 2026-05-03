# Troubleshooting IBM watsonx.ai Integration

## Issue: Model Not Found (404 Error)

**Error Message:**
```
Model 'ibm/granite-13b-instruct-v2' was not found
```

### Solution Steps:

#### 1. Check Available Models in Your Project
1. Go to https://cloud.ibm.com
2. Navigate to your watsonx.ai project
3. Click on "Prompt Lab" or "Foundation models"
4. See which models are actually available

#### 2. Common Working Models (Try These):
```
meta-llama/llama-2-70b-chat
meta-llama/llama-2-13b-chat
google/flan-ul2
google/flan-t5-xxl
ibm/granite-13b-chat-v2
```

#### 3. Update Your .env File
Edit `.env` and change the model:
```bash
WATSONX_MODEL_ID=meta-llama/llama-2-13b-chat
```

#### 4. Test Again
```bash
python src/analyzer.py
```

### Alternative: Use Mock Mode
If you can't get the API working for your demo, use mock mode:

Edit `.env`:
```
USE_WATSONX_API=false
```

This will use simulated responses that look realistic for your demo.

## Other Common Issues

### Issue: Authentication Error (401)
- Check your API key is correct
- Verify the API key hasn't expired
- Ensure the API key has proper permissions

### Issue: Project Not Found
- Verify WATSONX_PROJECT_ID is correct
- Check you have access to the project
- Ensure the project is in the same region as your API endpoint

### Issue: Timeout
- Increase timeout in watsonx_client.py
- Check your internet connection
- Try a smaller/faster model

## Quick Test Command
```bash
python test_config.py
```

This will verify your configuration without making API calls.