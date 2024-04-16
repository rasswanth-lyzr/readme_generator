import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.tasks.task_literals import InputType, OutputType

from dotenv import load_dotenv
import os

load_dotenv()

# Load OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Function to generate readme file
def generate_readme_file(file_contents, output_headers):
    # Initialize OpenAI Text Model
    open_ai_model_text = OpenAIModel(
    api_key=OPENAI_API_KEY,
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 4000,
        },
    )

    # Create a markdown generator Agent
    readme_agent = Agent(
        prompt_persona="You are an intelligent agent that can write in markdown format, but do not include ```markdown in the output.",
        role="Readme Generator"
    )

    # Create a markdown generator Task
    readme_creator_task = Task(
        name="Generate Readme Task",
        agent=readme_agent,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=open_ai_model_text,
        instructions="Write a README file for the provided code. Return only the output. Headers to be included are: " + output_headers,
        log_output=True,
        enhance_prompt=False,
        default_input=file_contents,
    ).execute()

    with open("generated_file.md", "w") as my_file:
        my_file.write(readme_creator_task)

    return readme_creator_task
    
# File uploader input
code_file = st.file_uploader("Upload your .py file")

# Headers input
output_headers = st.text_area("Headers to include", '''1. Title
2. Overview
3. Dependencies
4. Flow of the code in a bulleted format with 1-2 sentences each point.
5. How to run
''')

# Submit button
submit_file = st.button("Submit")

if submit_file:
    file_contents = code_file.read() # Read file
    readme_content = generate_readme_file(file_contents, output_headers) # Generate Readme file
    st.write(readme_content) # Print output
    st.download_button('Download readme', readme_content, file_name="generated_readme.md", mime="text/markdown") # Download output