from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from typing import List
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
    @agent
    def user_interaction(self) -> Agent:
        return Agent(
            config=self.agents_config['user_interaction'], # type: ignore[index]
            verbose=True
        )

    @agent
    def travel_searcher(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_searcher'], # type: ignore[index]
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

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def gather_requirements_task(self) -> Task:
        return Task(
            config=self.tasks_config['gather_requirements_task'], # type: ignore[index]
        )

    @task
    def identify_interests_task(self) -> Task:
        return Task(
            config=self.tasks_config['identify_interests_task'], # type: ignore[index]
            output_file='report.md'
        )

    @task
    def handle_clarification_task(self) -> Task:
        return Task(
            config=self.tasks_config['handle_clarification_task'], # type: ignore[index]
            expected_output="clarification.md"
        )

    @task
    def confirm_details_task(self) -> Task:
        return Task(
            config=self.tasks_config['confirm_details_task'], # type: ignore[index]
            expected_output="confirmation.md"
        )
    
    @task
    def flight_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['flight_search_task'], # type: ignore[index]
            expected_output="flight_search.md"
        )

    @task
    def accommodation_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['accommodation_search_task'], # type: ignore[index]
            expected_output="accommodation_search.md"
        )

    @task
    def destination_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['destination_search_task'], # type: ignore[index]
            expected_output="destination_search.md"
        )

    @task
    def attraction_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['attraction_search_task'], # type: ignore[index]
            expected_output="attraction_search.md"
        )

    @task
    def dinner_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['dinner_search_task'], # type: ignore[index]
            expected_output="dinner_search.md"
        )

    @task
    def structure_itinerary_task(self) -> Task:
        return Task(
            config=self.tasks_config['structure_itinerary_task'], # type: ignore[index]
            expected_output="itinerary.md"
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
            expected_output="integrated_preferences.md"
        )
    
    @task
    def consider_budget_task(self) -> Task:
        return Task(
            config=self.tasks_config['consider_budget_task'], # type: ignore[index]
            expected_output="budget_consideration.md"
        )
    
    @task
    def recommend_experiences_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommend_experiences_task'], # type: ignore[index]
            expected_output="recommended_experiences.md"
        )
    
    @task
    def offer_alternative_options_task(self) -> Task:
        return Task(
            config=self.tasks_config['offer_alternative_options_task'], # type: ignore[index]
            expected_output="alternative_options.md"
        )
    
    @task
    def post_planning_advice_task(self) -> Task:
        return Task(
            config=self.tasks_config['post_planning_advice_task'], # type: ignore[index]
            expected_output="post_planning_advice.md"
        )
    
    @task
    def evaluate_match_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_match_task'], # type: ignore[index]
            expected_output="evaluation.md"
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
            verbose=True,
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
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
