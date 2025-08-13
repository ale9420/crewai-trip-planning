from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from typing import List
from crewai_tools import SerperDevTool
from .models import DestinationInvestigation, FlightOption, FlightSearchResults, AccommodationSearchResults

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TripPlanning():
    """TripPlanning crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @agent
    def travel_searcher(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_searcher'], # type: ignore[index]
            tools=[SerperDevTool()],
            verbose=True
        )
    
    @agent
    def itinerary_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_planner'], # type: ignore[index]
            verbose=True
        )

    @agent
    def recommendation_engine(self) -> Agent:
        return Agent(
            config=self.agents_config['recommendation_engine'], # type: ignore[index]
            verbose=True
        )
    
    # Research Phase
    @task
    def destination_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['destination_search_task'], # type: ignore[index]
            output_pydantic=DestinationInvestigation
        )

    @task
    def flight_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['flight_search_task'], # type: ignore[index]
            output_pydantic=FlightSearchResults
        )

    @task
    def accommodation_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['accommodation_search_task'], # type: ignore[index]
            output_pydantic=AccommodationSearchResults
        )

    @task
    def transportation_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['transportation_search_task'], # type: ignore[index]
            expected_output="transportation_options.md"
        )

    @task
    def attraction_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['attraction_search_task'], # type: ignore[index]
            expected_output="attraction_options.md"
        )

    @task
    def dining_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['dining_search_task'], # type: ignore[index]
            expected_output="dining_options.md"
        )

    # Planning Phase
    @task
    def structure_itinerary_task(self) -> Task:
        return Task(
            config=self.tasks_config['structure_itinerary_task'], # type: ignore[index]
            expected_output="structured_itinerary.md"
        )

    @task
    def optimize_routes_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_routes_task'], # type: ignore[index]
            expected_output="optimized_routes.md"
        )
    
    @task
    def integrate_preferences_task(self) -> Task:
        return Task(
            config=self.tasks_config['integrate_preferences_task'], # type: ignore[index]
            expected_output="personalized_itinerary.md"
        )

    @task
    def create_contingency_plans_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_contingency_plans_task'], # type: ignore[index]
            expected_output="contingency_plans.md"
        )
    
    # Quality Assurance Phase
    @task
    def validate_itinerary_task(self) -> Task:
        return Task(
            config=self.tasks_config['validate_itinerary_task'], # type: ignore[index]
            expected_output="validation_report.md"
        )

    @task
    def test_logistics_task(self) -> Task:
        return Task(
            config=self.tasks_config['test_logistics_task'], # type: ignore[index]
            expected_output="logistics_verification.md"
        )

    @task
    def budget_final_check_task(self) -> Task:
        return Task(
            config=self.tasks_config['budget_final_check_task'], # type: ignore[index]
            expected_output="final_budget_summary.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TripPlanning crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=False,
            memory=True,
            # Long-term memory for persistent storage across sessions
            long_term_memory = LongTermMemory(
                storage=LTMSQLiteStorage(
                    db_path="./memory/long_term_memory_storage.db"
                )
            ),
            # Short-term memory for current context using RAG
            short_term_memory = ShortTermMemory(
                storage = RAGStorage(
                        embedder_config={
                            "provider": "openai",
                            "config": {
                                "model": 'text-embedding-3-small'
                            }
                        },
                        type="short_term",
                        path="./memory/"
                    )
                ),            # Entity memory for tracking key information about entities
            entity_memory = EntityMemory(
                storage=RAGStorage(
                    embedder_config={
                        "provider": "openai",
                        "config": {
                            "model": 'text-embedding-3-small'
                        }
                    },
                    type="short_term",
                    path="./memory/"
                )
            ),
        )
