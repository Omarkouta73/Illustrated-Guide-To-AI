# Chapter 1 — What Is an AI Agent?

Chapter 1 sets up the rest of the book. It defines what an agent is, lays out the
"anatomy of an agent" figure that every later chapter fills in, and starts the agent skeleton.

📓 Notebook: [`introduction.ipynb`](introduction.ipynb)

## Key ideas

### Definition

> An agent is anything that can be viewed as perceiving its environment through sensors and
> acting upon that environment through actuators.
> — Russell & Norvig, *Artificial Intelligence: A Modern Approach*

| Classic term      | Meaning                                      | In an LLM agent                              |
|-------------------|----------------------------------------------|----------------------------------------------|
| **Environment**   | The world the agent interacts with           | Files, web, APIs… and the **user**           |
| **Sensors**       | How the agent observes the environment       | Text input, plus images/audio for multi-modal LLMs |
| **Actuators**     | How the agent acts on the environment        | **Tools**                                    |
| **Agent program** | The "brain" that maps observations to actions | A **reasoning LLM**                          |

### Building blocks (and where the book covers them)

1. **LLM (Ch. 2).** Splits text into **tokens** and predicts the next one. It generates
   **autoregressively**: each predicted token is appended to the input before predicting the next.
2. **Reasoning LLM (Ch. 3).** Making models bigger (**train-time scaling**) stopped paying off.
   Models like OpenAI o1 and DeepSeek-R1 instead spend extra compute at inference time, writing out
   "thoughts" before the final answer. That helps with multi-step problems, at the cost of speed and money.
3. **Memory (Ch. 4).** LLMs are **stateless** and forget earlier turns. The simplest fix is putting
   the conversation history back in the prompt. Too much context causes **information overload**,
   so you have to choose what goes in. That is **context engineering**.
4. **Tools (Ch. 5).** LLMs are text-in/text-out, so they can only *state an intent* such as
   `multiply(5.1, 7.3)`. Our own code has to parse that output (for example as JSON) and run the real action.
   Memory plus tools gives Anthropic's **"augmented LLM"**.
5. **Planning & reflection (Ch. 6).** **Task decomposition** splits a big task into steps. After each
   step the agent reasons about what to do next, and **reflection** lets it revise the plan when it
   learns something new.

**AI agent = reasoning LLM + memory + tools + planning/reflection.**

### The agentic system

- **Autonomy is a spectrum.** It runs from a single LLM call, to a fixed pipeline, to fully
  autonomous agents. The book counts something as an agent once it shows goal-directed behavior
  and makes its own decisions.
- **Good use cases** are open-ended problems where the goal is clear but the path isn't: coding,
  deep research, automation.
- **Responsible use:** humans in the loop, **guardrails** against destructive actions, and
  awareness of **hallucinations**.
- **Evaluation (Ch. 7)** looks at the **outcome** (did the task get done?) and the **trajectory**
  (were the steps sensible and efficient?). It also checks **reliability**, since outputs are
  stochastic, and **safety**. You are evaluating a whole system, not just a model.

### Specializations (Part II)

- **Multi-agent (Ch. 8):** specialized agents working together, often under a supervisor agent.
- **Multi-modal (Ch. 9):** an encoder plus a connector lets the LLM *understand* other modalities,
  and a generator lets it *produce* them.
- **Coding agents (Ch. 10):** read, write, run, and test code in a real environment.

### Agent harnesses

The **harness** is the code around the LLM that makes it act like an agent. Types:
terminal-based (Claude Code, Codex CLI), code-based (LangGraph, Smolagents), personal assistant
(OpenClaw, Hermes Agent), hosted (Replit, Manus), and UI-based (Cursor, Copilot). They all use the
same scaffolding (LLM, memory, tools…) and differ mostly in packaging.

## What I built

The book's `TinyAgent` skeleton has a single `_step()` placeholder. In **Kouta** I split that one
step into the stages of the agent loop, so later chapters have obvious places to plug in:

```
task ──► _observe ──► _prompt_builder ──► _llm_call ──► _execute_action ──► result
```

Every stage is still a placeholder that only formats strings. There's no LLM yet, so the agent
just passes the task through:

```python
from src.Kouta.agent import Kouta

agent = Kouta()
agent.run(task="what is 1+1 ?")
# 'Executing Processing the prompt...             Prompt for Recieved task: what is 1+1 ?'
```

(The extra spaces come from the line continuation inside the f-string in `_llm_call`.)

```
src/Kouta/
└── agent.py   ← New (Kouta skeleton)
```

## Next

Chapter 2: replace the `_llm_call` placeholder with a real LLM.
