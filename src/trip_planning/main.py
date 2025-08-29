#!/usr/bin/env python
import sys
import warnings
from dotenv import load_dotenv
from datetime import datetime
from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool
from trip_planning.crew import TripPlanning
from pydantic import BaseModel

# Load environment variables
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

app = FastAPI()

class TripRequest(BaseModel):
    origin: str
    destination: str
    start_date: str
    end_date: str
    budget: str
    travelers: int
    trip_type: str
    accomodation: str
    flights: str
    user_preferences: str
    email: str

@app.post("/plan-trip")
async def plan_trip(trip_request: TripRequest):
    """
    API endpoint to start trip planning crew
    """
    try:
        inputs = trip_request.model_dump()
        # Run the blocking crew.kickoff in a thread pool
        result = await run_in_threadpool(TripPlanning().crew().kickoff, inputs=inputs)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def main():
    """
    Defines the main entry point for the application.
    This is used to run the FastAPI server.
    """
    import uvicorn
    print("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
def run():
    """
    Run the crew (for backward compatibility).
    """
    inputs = {
        "origin": "Bogota, Colombia",
        "destination": "Panama City, Panama",
        "start_date": "11/01/2025",
        "end_date": "11/15/2025",
        "budget": "5K USD per person",
        "travelers": 5,
        "trip_type": "Vacations",
        "accomodation": "Hotel",
        "flights": "economic",
        "user_preferences": "I want to go to a place where I can relax and enjoy the nature"
    }

    result = TripPlanning().crew().kickoff(inputs=inputs)
    # Access the raw response
    print(result.raw)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        TripPlanning().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TripPlanning().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        TripPlanning().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

# For running the FastAPI server directly with `python src/trip_planning/main.py`
if __name__ == "__main__":
    main()
