from dotenv import load_dotenv
import os

load_dotenv()

# Local vLLM
LOCAL_VLLM_URL = os.getenv("LOCAL_VLLM_URL")
LOCAL_VLLM_API_KEY = os.getenv("LOCAL_VLLM_API_KEY")
LOCAL_VLLM_MODEL = os.getenv("LOCAL_VLLM_MODEL")

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")
