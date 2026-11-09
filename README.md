# Illustrated Guide To AI Agents — My Implementation

My notes and code while working through
**_An Illustrated Guide to AI Agents: Concepts and Code for Building Agents with LLMs, Tools, and Memory_**
by Maarten Grootendorst and Jay Alammar (O'Reilly, 2026).

The book builds an agent called **TinyAgent** one component at a time. I'm building my own version
alongside it, called **[Kouta](src/Kouta/)**: **K**eep **O**bserving, **U**nderstanding, **T**hinking, **A**cting.

> The official companion code is at
> [HandsOnLLM/An-Illustrated-Guide-To-AI-Agents](https://github.com/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents).
> This repo is a personal learning project, not a copy of that one.

## Repository layout

```
Illustrated-Guide-To-AI-Agents/
├── Book/                      # One folder per chapter: notes + notebook
│   └── chapter01/
│       ├── README.md          # Chapter 1 notes
│       └── introduction.ipynb # Runs the Kouta skeleton
└── src/
    └── Kouta/                 # The agent, grown chapter by chapter
        ├── README.md
        └── agent.py
```

## Progress

| Chapter | Topic                                   | Status  | What changed in Kouta                      |
|---------|-----------------------------------------|---------|--------------------------------------------|
| 1       | What is an AI agent?                    | ✅ Done | Skeleton class with placeholder loop steps |
| 2       | Large language models                   | ⬜      | Plug in an LLM (`self.llm`)                |
| 3       | Reasoning LLMs                          | ⬜      | Reasoning before acting                    |
| 4       | Memory                                  | ⬜      | `self.memory`, context engineering         |
| 5       | Tools & Model Context Protocol (MCP)    | ⬜      | `self.tools`, real `_execute_action`       |
| 6       | Planning & reflection                   | ⬜      | `self.plan`, multi-step loop               |
| 7       | Evaluation                              | ⬜      | Outcome and trajectory evals               |
| 8       | Multi-agent systems                     | ⬜      |                                            |
| 9       | Multi-modal agents                      | ⬜      |                                            |
| 10      | Coding agents                           | ⬜      |                                            |

## Getting started

Requires Python 3.12 (what the venv uses). Kouta has no third-party dependencies yet; Jupyter is
only needed for the notebooks.

```bash
git clone <this-repo-url>
cd Illustrated-Guide-To-AI-Agents

python3 -m venv venv
source venv/bin/activate
pip install jupyter
```

Notebooks import the agent as `from src.Kouta.agent import Kouta`, so **run them with the repo root
as the working directory**. In VS Code, `.vscode/settings.json` already sets
`jupyter.notebookFileRoot` to the workspace folder. From the command line:

```bash
jupyter notebook   # launch from the repo root, then open Book/chapter01/introduction.ipynb
```

Quick check without Jupyter:

```bash
python -c "from src.Kouta.agent import Kouta; print(Kouta().run('what is 1+1 ?'))"
```
