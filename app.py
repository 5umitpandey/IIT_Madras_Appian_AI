import asyncio
import os
from paperqa import Docs

# -------------------------------------------------
# FORCE LOCAL-ONLY EXECUTION (CRITICAL)
# -------------------------------------------------
os.environ["LLM"] = "ollama/mistral"
os.environ["EMBEDDING"] = "ollama/nomic-embed-text"

# Disable OpenAI & external services completely
os.environ["OPENAI_API_KEY"] = ""
os.environ["CROSSREF_API_KEY"] = ""
os.environ["SEMANTIC_SCHOLAR_API_KEY"] = ""

# Disable enrichment features that trigger OpenAI
os.environ["PAPERQA_DISABLE_ENRICHMENT"] = "1"
os.environ["PAPERQA_DISABLE_METADATA"] = "1"
os.environ["PAPERQA_DISABLE_MEDIA_ENRICHMENT"] = "1"

# -------------------------------------------------
# Initialize Docs (NO arguments)
# -------------------------------------------------
docs = Docs()
_documents_loaded = False


async def load_documents():
    global _documents_loaded
    if not _documents_loaded:
        await docs.aadd(
            "data/Bajaj_Health_Insurance_Policy.pdf",
            citation="Bajaj Health Insurance Policy",
        )
        _documents_loaded = True


async def query_knowledge(case_context: dict):
    await load_documents()

    query = f"""
    A case is being processed with the following details:
    - Claim Type: {case_context['claim_type']}
    - Location: {case_context['location']}
    - Case Category: {case_context['case_category']}

    Based on the policy documents:
    1. Is this covered?
    2. What conditions or exclusions apply?
    3. What steps should the agent follow?
    """

    answer = await docs.aquery(query)
    return answer.answer, answer.contexts
