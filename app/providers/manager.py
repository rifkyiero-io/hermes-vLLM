import traceback

from app.providers.local_vllm import LocalVLLMProvider
from app.providers.gemini import GeminiProvider
from app.providers.openrouter import OpenRouterProvider


class ProviderManager:

    def __init__(self):
        self.providers = [
            LocalVLLMProvider(),
            GeminiProvider(),
            OpenRouterProvider(),
        ]

    async def chat(self, messages):

        last_error = None

        for provider in self.providers:

            try:
                return await provider.chat(messages)

            except Exception as e:
                print(f"\n===== {provider.__class__.__name__} =====")
                traceback.print_exc()
                print("===============================\n")
                last_error = e

        raise RuntimeError(f"All providers failed: {last_error}")
