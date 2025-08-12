from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from typing import List
from pydantic import BaseModel, Field
from crewai_tools import SerperDevTool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

class DestinationInvestigation(BaseModel):
    """
    Comprehensive destination intelligence report containing essential travel information.
    
    This model captures all critical information needed for trip planning including
    weather conditions, entry requirements, safety considerations, cultural insights,
    and practical travel tips. All information should be tailored to the specific
    travel dates and user preferences provided in the task context.
    """
    overview: str = Field(
        description="A comprehensive overview of the destination including key highlights, "
                   "general atmosphere, and what makes it unique. Should include major "
                   "attractions, cultural significance, and overall travel appeal."
    )
    weather: list[str] = Field(
        description="Detailed weather information for the specific travel dates including "
                   "temperature ranges, precipitation patterns, humidity levels, and seasonal "
                   "considerations. Include packing recommendations and weather-related travel tips."
    )
    events: list[str] = Field(
        description="Major events, festivals, holidays, or special occasions during the travel period. "
                   "Include impact on crowds, prices, availability, and whether these events "
                   "enhance or complicate the travel experience."
    )
    entry_requirements: list[str] = Field(
        description="Complete entry and visa requirements including passport validity, visa types, "
                   "application processes, fees, and processing times. Include health requirements, "
                   "COVID-19 protocols, and travel insurance mandates."
    )
    safety_tips: list[str] = Field(
        description="Comprehensive safety information including crime rates, common scams, "
                   "areas to avoid, emergency contacts, and health/medical care availability. "
                   "Include political stability and any current travel advisories."
    )
    cultural_norms: list[str] = Field(
        description="Essential cultural etiquette, customs, dress codes, and social norms. "
                   "Include tipping practices, language basics, local dos and don'ts, "
                   "and cultural sensitivities to respect."
    )
    best_times_to_visit: list[str] = Field(
        description="Optimal timing for visiting major attractions including opening hours, "
                   "peak vs. off-peak times, crowd management tips, and recommendations "
                   "for maximizing the visitor experience."
    )
    local_transportation: list[str] = Field(
        description="Complete transportation overview including public transit systems, "
                   "ride-sharing options, taxi services, walking safety, and accessibility "
                   "features for travelers with special needs."
    )
    money_and_connectivity: list[str] = Field(
        description="Financial and communication information including local currency, "
                   "payment methods, ATM availability, internet access, SIM card options, "
                   "mobile coverage, and connectivity costs."
    )
    insider_tips: list[str] = Field(
        description="Local secrets, hidden gems, off-the-beaten-path suggestions, and "
                   "common tourist mistakes to avoid. Include authentic local experiences "
                   "and insider knowledge for a more genuine travel experience."
    )
    recent_developments: list[str] = Field(
        description="Recent news, travel advisories, infrastructure changes, or disruptions "
                   "relevant to the travel period. Include any updates that could impact "
                   "the travel experience or require special planning."
    )

class FlightOption(BaseModel):
    """
    Detailed information for a single flight option including all pricing, timing, and service details.
    
    This model captures comprehensive flight information to help travelers make informed decisions
    based on their specific needs, budget, and preferences.
    """
    airline: str = Field(
        description="The airline name and any codeshare partners. Include major carrier, "
                   "budget airline, or regional carrier designation."
    )
    flight_numbers: list[str] = Field(
        description="All flight numbers for the journey including connecting flights. "
                   "Format as airline code + number (e.g., 'AA123', 'BA456')."
    )
    departure_time: str = Field(
        description="Departure time in local timezone with date. Include timezone information "
                   "if different from origin timezone."
    )
    arrival_time: str = Field(
        description="Arrival time in local timezone with date. Include timezone information "
                   "if different from destination timezone."
    )
    total_travel_time: str = Field(
        description="Total journey time including layovers. Format as hours and minutes "
                   "(e.g., '8h 30m' or '2h 15m' for direct flights)."
    )
    stops: int = Field(
        description="Number of stops (0 for direct flights, 1 for one connection, etc.). "
                   "Include layover duration and airport codes."
    )
    layover_details: list[str] = Field(
        description="Detailed layover information including airport codes, duration, "
                   "and any terminal changes. Include visa requirements for layover countries."
    )
    aircraft_type: str = Field(
        description="Aircraft model and configuration. Include seat layout and capacity "
                   "information if available."
    )
    total_price_per_person: float = Field(
        description="Total price per person including all taxes and fees. "
                   "Specify currency and whether price is for one-way or round-trip."
    )
    price_breakdown: dict[str, float] = Field(
        description="Detailed price breakdown including base fare, taxes, fuel surcharges, "
                   "and any additional fees. Include currency for each component."
    )
    baggage_allowance: str = Field(
        description="Checked and carry-on baggage allowance. Include weight limits, "
                   "dimension restrictions, and any additional baggage fees."
    )
    seat_selection_cost: float = Field(
        description="Cost for seat selection including any advance seat reservation fees. "
                   "Specify if seat selection is included in base fare."
    )
    cancellation_fees: str = Field(
        description="Cancellation and change fees including refund policies. "
                   "Include time restrictions and any non-refundable components."
    )
    cabin_class: str = Field(
        description="Cabin class (Economy, Premium Economy, Business, First). "
                   "Include seat configuration and legroom information."
    )
    in_flight_amenities: list[str] = Field(
        description="Available in-flight amenities including WiFi, entertainment systems, "
                   "meal service, power outlets, and lounge access."
    )
    on_time_performance: float = Field(
        description="Airline's on-time performance percentage for this route. "
                   "Include historical data if available."
    )
    customer_rating: float = Field(
        description="Customer satisfaction rating out of 5 stars. "
                   "Include number of reviews and recent feedback trends."
    )
    airport_transfer_info: str = Field(
        description="Information about airport transfers including transfer times, "
                   "costs, and transportation options between terminals."
    )
    visa_requirements: list[str] = Field(
        description="Visa requirements for any layover countries. "
                   "Include transit visa needs and application processes."
    )
    covid_requirements: list[str] = Field(
        description="COVID-19 related requirements including testing, vaccination, "
                   "and quarantine rules for all countries in the journey."
    )
    booking_class: str = Field(
        description="Fare class and booking code. Include fare rules and restrictions "
                   "for changes, cancellations, and upgrades."
    )
    loyalty_program: str = Field(
        description="Loyalty program earning potential including miles/points per dollar "
                   "and any elite status benefits that apply."
    )
    recommended_booking_channel: str = Field(
        description="Best booking channel recommendation (direct airline, OTA, travel agent). "
                   "Include reasoning and any exclusive deals available."
    )
    booking_timing: str = Field(
        description="Optimal booking timing recommendations. Include advance booking "
                   "requirements and last-minute deal possibilities."
    )

class FlightSearchResults(BaseModel):
    """
    Comprehensive flight search results containing summary statistics and detailed flight options.
    
    This model provides a complete overview of available flight options with pricing analysis,
    recommendations, and important considerations for travelers. All information should be
    tailored to the specific travel requirements and preferences provided in the task context.
    """
    search_summary: dict[str, str] = Field(
        description="Summary statistics including total options found, price range, "
                   "and best value highlights. Include currency and search criteria used."
    )
    flight_options: list[FlightOption] = Field(
        description="Detailed flight options (maximum 10) ranked by relevance and value. "
                   "Include a mix of direct flights, connections, and different price points."
    )
    recommendations: dict[str, str] = Field(
        description="Specific recommendations including top 3 value-for-money options, "
                   "best options for families, business travelers, and budget-conscious travelers. "
                   "Include reasoning for each recommendation."
    )
    alternative_airports: list[str] = Field(
        description="Nearby airports that could offer better pricing or convenience. "
                   "Include distance from primary airports and transportation options."
    )
    flexible_date_recommendations: list[str] = Field(
        description="Recommendations for flexible date travel including potential savings "
                   "and optimal travel dates within the user's flexibility range."
    )
    seasonal_considerations: list[str] = Field(
        description="Seasonal price variations, peak travel periods, and weather impacts "
                   "on flight availability and pricing."
    )
    promotions_and_deals: list[str] = Field(
        description="Current promotions, fare sales, and special deals that could "
                   "provide additional savings or benefits."
    )
    travel_advisories: list[str] = Field(
        description="Any travel advisories, restrictions, or warnings relevant to "
                   "the flight routes or destinations."
    )
    booking_tips: list[str] = Field(
        description="Best practices for booking including timing, payment methods, "
                   "and strategies for securing the best deals."
    )
    insurance_recommendations: list[str] = Field(
        description="Travel insurance recommendations including coverage options, "
                   "costs, and specific policies that would benefit this trip."
    )

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
    def budget_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['budget_manager'], # type: ignore[index]
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

    @agent
    def quality_assurance(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_assurance'], # type: ignore[index]
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
            expected_output="accommodation_options.md"
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

    # Budget Management Phase
    @task
    def budget_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['budget_analysis_task'], # type: ignore[index]
            expected_output="budget_analysis.md"
        )

    @task
    def cost_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config['cost_optimization_task'], # type: ignore[index]
            expected_output="cost_optimization.md"
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
