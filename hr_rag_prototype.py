import os
from google import genai

# Failsafe: Ensure the API key is set in the environment, NOT hardcoded.
if "GEMINI_API_KEY" not in os.environ:
    raise ValueError("GEMINI_API_KEY environment variable not set. Do not hardcode keys!")

client = genai.Client()

# Mocked retrieval database representing a subset of the 12 HR PDFs
MOCK_HR_KNOWLEDGE_BASE = {
    "leave_policy": "Employees accrue 1.5 days of Paid Time Off (PTO) per month. Maximum rollover into the next calendar year is 5 days.",
    "remote_work": "Remote work is allowed up to 2 days per week for standard employees. Core hours are 10 AM to 3 PM EST."
}

def retrieve_context(query: str) -> str:
    """Mock retrieval step to simulate pulling text from a vector database."""
    query_lower = query.lower()
    if "leave" in query_lower or "pto" in query_lower:
        return MOCK_HR_KNOWLEDGE_BASE["leave_policy"]
    elif "remote" in query_lower or "home" in query_lower:
        return MOCK_HR_KNOWLEDGE_BASE["remote_work"]
    return ""

def ask_hr_assistant(query: str) -> str:
    """Combines retrieved context with the LLM to generate a grounded answer."""
    context = retrieve_context(query)
    
    # Enforce strict grounding: if no context is found, refuse to answer.
    if not context:
        return "I cannot answer this based on the provided HR policies."
    
    prompt = f"""
    You are a strict HR Policy Assistant. Answer the employee's question using ONLY the provided context. 
    If the context does not completely answer the question, state that clearly. Do not make up information.
    
    Context: {context}
    Question: {query}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text

if __name__ == "__main__":
    # Example Inputs required by the task instructions
    queries = [
        "How many PTO days do I get per month?",
        "Can I work from home 4 days a week?",
        "What is the company policy on traveling first class?" # Out of scope test
    ]
    
    for q in queries:
        print(f"Input: {q}")
        print(f"Output: {ask_hr_assistant(q)}\n")
        print("-" * 40)