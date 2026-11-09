# Kouta

**KOUTA** stands for **K**eep **O**bserving, **U**nderstanding, **T**hinking, **A**cting.

Kouta is my from-scratch agent, built one chapter at a time while reading
*An Illustrated Guide to AI Agents*. It's my version of the book's **TinyAgent**. Like TinyAgent,
it avoids frameworks and keeps dependencies to a minimum so every line is understood.

## Current state (after Chapter 1)

A skeleton with no brain. Every component is `None` and every loop stage is a placeholder.

```python
from src.Kouta.agent import Kouta

agent = Kouta()
print(agent.run(task="what is 1+1 ?"))
```

## Anatomy

### Components

| Attribute     | Purpose                                  | Added in   |
|---------------|------------------------------------------|------------|
| `self.llm`    | The "brain": a (reasoning) LLM            | Ch. 2 & 3  |
| `self.memory` | Conversation history / long-term memory  | Ch. 4      |
| `self.tools`  | Actions the agent can take               | Ch. 5      |
| `self.plan`   | Task decomposition & reflection          | Ch. 6      |

### The loop

`run(task)` resets memory and calls `one_loop(task)`. `one_loop` runs one pass through the
stages in the name:

| Stage                    | Method              | Role                                               | Status          |
|--------------------------|---------------------|----------------------------------------------------|-----------------|
| **O**bserve              | `_observe`          | Turn the incoming task into a goal/observation     | placeholder     |
| **U**nderstand           | `_prompt_builder`   | Build the prompt / context for the LLM             | placeholder     |
| **T**hink                | `_llm_call`         | Ask the LLM to decide on an answer or action       | placeholder     |
| **A**ct                  | `_execute_action`   | Run the chosen action (tool call)                  | placeholder     |
| *(remember)*             | `self.memory.append`| Store what happened                                | stub (Ch. 4)    |

The planned format for an LLM action (see the comment in `one_loop`):

```python
{"action": "tool_call", "tool_call": {"tool_name": "...", "args": {...}}}
```

## How it differs from TinyAgent

- The book has one `_step()` method. Kouta splits it into explicit observe → prompt → LLM → act
  stages.
- `run()` re-initializes `memory` on every call, so for now each run starts fresh.
- Uses `plan` where the book uses `planner`.

## Roadmap

- [x] Ch. 1: Skeleton class and loop stages
- [ ] Ch. 2: Real LLM in `_llm_call`
- [ ] Ch. 3: Reasoning before acting
- [ ] Ch. 4: Memory and context engineering
- [ ] Ch. 5: Tools, parsing actions, MCP
- [ ] Ch. 6: Planning & reflection, a real multi-step loop
- [ ] Ch. 7: Evaluation
