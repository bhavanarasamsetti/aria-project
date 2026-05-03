# IBM watsonx.ai Supported Models

Common models you can use (update WATSONX_MODEL_ID in .env):

## Foundation Models
- `ibm/granite-13b-instruct-v2` (Recommended for instructions)
- `ibm/granite-13b-chat-v2` (Chat optimized)
- `meta-llama/llama-2-70b-chat`
- `meta-llama/llama-2-13b-chat`
- `google/flan-ul2`
- `google/flan-t5-xxl`

## How to check available models:
1. Go to your watsonx.ai project
2. Navigate to "Foundation models"
3. Check which models are available in your region
4. Copy the exact model ID

## Update your .env:
```
WATSONX_MODEL_ID=ibm/granite-13b-instruct-v2
```

If you get a 404 error, the model may not be available in your region or project.
Try `ibm/granite-13b-instruct-v2` or `meta-llama/llama-2-13b-chat` instead.