import time
from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_manim_code(prompt, filename):
    print(f"Generating code for: {filename}...")
    response = client.models.generate_content(
        model='gemini-2.5-flash-lite',
        contents=f"Write a complete, runnable Manim Python script for: {prompt}. "
                 "Include all necessary imports (from manim import *). "
                 "Ensure the code is self-contained and ready to render."
                 "Write ONLY the Python code for: {prompt}. Do not include conversational text, markdown headers, or explanations."
    )
    
    # Clean the response to extract only the code block
    code = response.text.replace("```python", "").replace("```", "").strip()
    with open(filename, "w") as f: 
        f.write(code)
    print(f"Saved to {filename}")

# Tasks
pythagoras_prompt = "A visual proof of the Pythagorean theorem. Show a right triangle with squares on all three sides, labels for sides a, b, and c, and the identity 'a^2 + b^2 = c^2' displayed clearly."
fourier_prompt = "A visualization of a Fourier series decomposing a square wave. Sum at least the first 5 odd harmonic sine waves, each in a different color, and show the cumulative sum updating step-by-step.Write a Manim scene (Community Edition v0.20.1) that demonstrates this. Please use axes.get_graph for all function plots, avoid LineString or any imports not in the core manim library, and ensure that all variables are explicitly passed to lambda functions to avoid closure scope issues."

generate_manim_code(pythagoras_prompt, "pythagoras.py")
generate_manim_code(fourier_prompt, "fourier_series.py")