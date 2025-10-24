import requests
import xml.etree.ElementTree as ET

def fetch_papers(query: str, max_results: int = 5):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
    r = requests.get(url)
    root = ET.fromstring(r.text)
    papers = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text.strip()
        abstract = entry.find("{http://www.w3.org/2005/Atom}summary").text.strip()
        year = entry.find("{http://www.w3.org/2005/Atom}published").text[:4]
        papers.append({"title": title, "abstract": abstract, "year": year})
    return papers
