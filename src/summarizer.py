from llm_client import ollama_generate

SUMMARY_PROMPT = """Summarize this research paper abstract in 3 bullet points:
Title: {title}
Abstract: {abstract}
"""

SYNTHESIS_PROMPT = """Given these summaries on {query}, write a 3-paragraph synthesis describing:
1. Common methods
2. Key trends
3. Future research directions

Summaries:
{summaries}
"""

def summarize_papers(papers):
    results = []
    for p in papers:
        prompt = SUMMARY_PROMPT.format(title=p['title'], abstract=p['abstract'])
        summary = ollama_generate(prompt)
        results.append({
            "title": p["title"],
            "year": p["year"],
            "summary": summary
        })
    return results

def synthesize_summaries(summaries, query):
    combined = "\n\n".join(f"{s['title']} - {s['summary']}" for s in summaries)
    prompt = SYNTHESIS_PROMPT.format(summaries=combined, query=query)
    return ollama_generate(prompt)
