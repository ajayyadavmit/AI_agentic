# Project Overview

This repository contains multiple small AI-related agents, example scripts, and Docker setups. Each top-level folder is a separate component or demo. Below is a concise guide to the structure and how to run the main entrypoints.

## Structure

- image/
  - main.py — image processing/demo entrypoint

- langchain_ai/
  - main.py, chat.py, chat_2.py, chat_checkpoint.py — LangChain-based chat/demo services
  - docker-compose.yml — Docker compose for this service
  - requirem.txt — Python dependencies for LangChain components

- mem_agent/
  - mem.py — memory agent demo
  - docker-compose.yml — Docker compose for mem agent

- Prompt/
  - agent_tool.py, prompt.py, cot*.py, google_ai.py, few_prompt.py — collection of prompts and tools for prompting workflows

- rag/
  - chat.py, index.py — retrieval-augmented generation demo
  - docker-compose.yml

- rag_queue/
  - server.py, main.py — queue-backed RAG demo with docker-compose

- sdk_agent/
  - agent_tools.py, main.py — SDK-based agent utilities and entrypoints

- voice_agent/
  - main.py, voice.py, cursor.py — voice / audio agent examples

- weather/
  - main.py, agent.py, ktm.py — weather agent demo scripts

- queue/ and client/ — small rq worker and client helpers

## Dependencies

The most complete dependency list is in `langchain_ai/requirem.txt`. Install into a virtual environment before running components:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r langchain_ai/requirem.txt
```

If you prefer Docker, several folders include a `docker-compose.yml` you can use to run that component in containers, e.g.:

```bash
cd langchain_ai
docker-compose up --build
```

## Running common entrypoints

- LangChain chat demo:
  - `python langchain_ai/main.py`
  - or use the `langchain_ai/docker-compose.yml` target

- Image demo:
  - `python image/main.py`

- RAG demo:
  - `python rag/index.py` or `python rag/chat.py`
  - `docker-compose` available in `rag/`

- Memory agent:
  - `python mem_agent/mem.py`
  - `docker-compose` available in `mem_agent/`

- Voice agent demo:
  - `python voice_agent/main.py`

- Queue worker / client:
  - Start worker: `python queue/worker.py`
  - Use client: `python client/rq_client.py`

## Notes & Next steps

- The `langchain_ai/requirem.txt` file is large and includes many optional components; consider creating a minimal `requirements.txt` if you want a smaller environment.
- Inspect individual `main.py` files for component-specific environment variables (API keys, ports). Many demos expect OpenAI/Google credentials or local services (Redis, MongoDB, Qdrant).

If you want, I can:
- Extract environment variables used by each `main.py` into a `.env.example` file.
- Create smaller per-component `requirements.txt` files.
- Add quick-run scripts or Makefile targets.

---
Generated automatically by an assistant scanning the repository.