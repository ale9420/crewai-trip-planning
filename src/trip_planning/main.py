#!/usr/bin/env python
import sys
import warnings
import gradio as gr
import os
from dotenv import load_dotenv

from datetime import datetime

from trip_planning.crew import TripPlanning

# Load environment variables
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def respond(message, history):
    """
    Handle chat messages and return crew response.
    """
    if not message.strip():
        return "", history
    
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        error_msg = "❌ **Error**: OpenAI API key not found. Please set your OPENAI_API_KEY in the .env file."
        history = history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": error_msg}
        ]
        return "", history
    
    # Convert Gradio history format to the format expected by crewAI
    # Gradio history is a list of tuples (user_msg, assistant_msg)
    # We need to convert it to a list of dicts with role and content
    crew_history = []
    for user_msg, assistant_msg in history:
        if user_msg:
            crew_history.append({"role": "user", "content": user_msg})
        if assistant_msg:
            crew_history.append({"role": "assistant", "content": assistant_msg})
    
    # Add current message
    crew_history.append({"role": "user", "content": message})
    
    # Pass the converted history to the backend
    inputs = {
        'human_feedback': message
        #'content': message,
        #'role': 'user',
        #'history': crew_history
    }

    print("[LOG] respond() method called with message:", message)
    print("[LOG] History length:", len(crew_history))
    
    try:
        result = TripPlanning().crew().kickoff(inputs=inputs)
        print("[LOG] Crew result:", result)
        
        # Return the result and let Gradio handle the history
        return result.raw, history
    except Exception as e:
        print("[LOG] Error - respond():", e)
        error_msg = f"❌ **Error**: An error occurred while running the crew: {str(e)}"
        return error_msg, history



def run():
    """
    Run the crew (for backward compatibility).
    """
    inputs = {
        "origin": "Bogota, Colombia",
        "destination": "Medellin, Colombia",
        "start_date": "11/01/2025",
        "end_date": "11/15/2025",
        "budget": "5K USD per person",
        "travelers": 5,
        "trip_type": "Vacations",
        "accomodation": "Hotel",
        "flights": "economic",
        "user_preferences": "I want to go to a place where I can relax and enjoy the nature"
    }

    TripPlanning().crew().kickoff(inputs=inputs)

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
