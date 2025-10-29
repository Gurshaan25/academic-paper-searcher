# Research Agent

A Python-based research assistant that fetches academic papers from arXiv, generates summaries using a local LLM, and synthesizes findings into a comprehensive overview.

## Overview

This tool automates the research literature review process by:
1. Searching arXiv for papers matching your query
2. Summarizing each paper's abstract into bullet points
3. Synthesizing all summaries into a coherent analysis covering common methods, key trends, and future research directions

## Features

- **Automated Paper Retrieval**: Fetches papers from arXiv API based on search queries
- **LLM-Powered Summaries**: Uses Ollama (llama3 by default) to generate concise paper summaries
- **Synthesis Generation**: Creates a unified overview from multiple paper summaries
- **Vector Store Support**: Includes infrastructure for semantic search over summaries (currently disabled)

## Prerequisites

- Python 3.7+
- [Ollama](https://ollama.ai/) installed and running locally
- Required Python packages:
  ```bash
  pip install requests sentence-transformers numpy
  ```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install requests sentence-transformers numpy
   ```
3. Ensure Ollama is installed and the llama3 model is available:
   ```bash
   ollama pull llama3
   ```

## Usage

Run the research agent from the command line:

```bash
python main.py "your research query"
```

**Example:**
```bash
python main.py "transformer architectures in natural language processing"
```

## Output

The tool provides two sections of output:

1. **SYNTHESIS**: A 3-paragraph overview covering:
   - Common methods across papers
   - Key trends in the field
   - Future research directions

2. **SUMMARIES**: Individual paper summaries with:
   - Paper title and publication year
   - 3 bullet-point summary of the abstract

## Project Structure

- `main.py` - Entry point and CLI interface
- `agent.py` - Main orchestration logic
- `search_client.py` - arXiv API integration
- `summarizer.py` - LLM prompt templates and summary generation
- `llm_client.py` - Ollama integration via subprocess
- `vector_store.py` - Vector embedding storage for semantic search (optional feature)

## Configuration

### Changing the LLM Model

Edit `llm_client.py` to use a different Ollama model:
```python
def ollama_generate(prompt: str, model: str = "your-model-name"):
```

### Adjusting Number of Papers

Modify the `max_results` parameter in `agent.py`:
```python
papers = fetch_papers(query, max_results=10)  # Default is 5
```

## Future Enhancements

The vector store functionality is currently commented out in `agent.py`. To enable semantic search over your research summaries:

1. Uncomment the line in `agent.py`:
   ```python
   self.store.add_many(summaries)
   ```
2. Use `self.store.search(query)` to retrieve relevant past summaries

## Limitations

- Requires local Ollama installation
- Summary quality depends on the LLM model used
- arXiv API rate limits may apply for large queries
- No caching mechanism for repeated queries

## License

[Add your license information here]