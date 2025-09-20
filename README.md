# TripPlanning Crew

[![CI](https://github.com/ale9420/crewai-trip-planning/actions/workflows/ci.yml/badge.svg)](https://github.com/ale9420/crewai-trip-planning/actions/workflows/ci.yml)
[![Build and Deploy](https://github.com/ale9420/crewai-trip-planning/actions/workflows/cd.yml/badge.svg)](https://github.com/ale9420/crewai-trip-planning/actions/workflows/cd.yml)

Welcome to the TripPlanning Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
uv sync
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/trip_planning/config/agents.yaml` to define your agents
- Modify `src/trip_planning/config/tasks.yaml` to define your tasks
- Modify `src/trip_planning/crew.py` to add your own logic, tools and specific args
- Modify `src/trip_planning/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

## Understanding Your Crew

The trip-planning Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the TripPlanning Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
