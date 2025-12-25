import asyncio
from paperqa import Docs
from paperqa.settings import Settings


async def main():
    """
    Entry point for the Just-in-Time Knowledge Retrieval demo.
    Runs fully locally using Ollama + Mistral.
    """

    # -------------------------------
    # 1. Configure local models
    # -------------------------------
    settings = Settings(
        llm="ollama/mistral",
        embedding="ollama/nomic-embed-text",
        temperature=0.1,
        max_tokens=512,
    )

    # -------------------------------
    # 2. Initialize document system
    # -------------------------------
    docs = Docs(settings=settings)

    # -------------------------------
    # 3. Load policy documents
    # -------------------------------
    print("📄 Loading policy documents...\n")

    await docs.aadd(
        "data/sample_policies/Bajaj_Health_Insurance_Policy.pdf",
        citation="Bajaj Health Insurance Policy",
    )

    # Add more PDFs here if needed
    # await docs.aadd("data/sample_policies/Another_Policy.pdf")

    print("✅ Documents loaded successfully\n")

    # -------------------------------
    # 4. Simulated Appian case context
    # -------------------------------
    case_context = {
        "claim_type": "Flood",
        "location": "Florida",
        "case_category": "Insurance Claim",
    }

    # Convert structured case data into a query
    query = f"""
    A case is being processed with the following details:
    - Claim Type: {case_context['claim_type']}
    - Location: {case_context['location']}
    - Case Category: {case_context['case_category']}

    Based on the policy documents:
    1. Is flood damage covered?
    2. What conditions or exclusions apply?
    3. What steps should the agent follow?
    """

    # -------------------------------
    # 5. Run knowledge retrieval
    # -------------------------------
    print("🤖 Retrieving context-aware knowledge...\n")

    answer = await docs.aquery(query)

    # -------------------------------
    # 6. Display results
    # -------------------------------
    print("🧠 ANSWER\n")
    print(answer.answer)

    print("\n📎 SOURCES\n")
    for ctx in answer.contexts:
        print(f"- {ctx}")

    print("\n✅ Demo completed successfully")


if __name__ == "__main__":
    asyncio.run(main())
