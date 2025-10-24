from search_client import fetch_papers
from summarizer import summarize_papers, synthesize_summaries
from vector_store import VectorStore

class ResearchAgent:
    def __init__(self):
        self.store = VectorStore("data/store.pkl")

    def run(self, query: str):
        papers = fetch_papers(query, max_results=5)
        summaries = summarize_papers(papers)
        #self.store.add_many(summaries)
        synthesis = synthesize_summaries(summaries, query)
        return {"summaries": summaries, "synthesis": synthesis}
