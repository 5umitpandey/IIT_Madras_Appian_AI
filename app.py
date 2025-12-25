import asyncio
import os
from paperqa import Docs

# -------------------------------------------------
# Configure paper-qa via environment variables
# -------------------------------------------------
os.environ["LLM"] = "ollama/mistral"
os.environ["EMBEDDING"] = "ollama/nomic-embed-text"
os.environ["TEMPERATURE"] = "0.1"
os.environ["MAX_TOKENS"] = "512"

# -------------------------------------------------
# Initialize Docs (NO arguments allowed)
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


# -------------------------------------------------
# Optional backend test
# -------------------------------------------------
if __name__ == "__main__":
    async def test():
        ctx = {
            "claim_type": "Flood",
            "location": "Florida",
            "case_category": "Insurance Claim",
        }
        ans, srcs = await query_knowledge(ctx)
        print(ans)
        print("\nSources:")
        for s in srcs:
            print("-", s)

    asyncio.run(test())
