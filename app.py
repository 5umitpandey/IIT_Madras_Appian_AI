import asyncio
from paperqa import Docs
from paperqa.settings import Settings

settings = Settings(
    llm="ollama/mistral",
    embedding="ollama/nomic-embed-text",
    temperature=0.1,
    max_tokens=512,
)

docs = Docs(settings=settings)
_documents_loaded = False


async def load_documents():
    global _documents_loaded
    if not _documents_loaded:
        await docs.aadd(
            "data/sample_policies/Bajaj_Health_Insurance_Policy.pdf",
            citation="Bajaj Health Insurance Policy"
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
