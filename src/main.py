import sys
from agent import ResearchAgent

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py '<research query>'")
        sys.exit(1)

    query = sys.argv[1]
    agent = ResearchAgent()
    result = agent.run(query)

    print("\n=== SYNTHESIS ===")
    print(result["synthesis"])
    print("\n=== SUMMARIES ===")
    for s in result["summaries"]:
        print(f"\n- {s['title']} ({s['year']})")
        print(f"  {s['summary']}")

if __name__ == "__main__":
    main()
