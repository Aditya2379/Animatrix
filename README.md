# Animatrix: AI-Powered Educational Animation Generator

## Overview

Animatrix is an end-to-end AI-powered system that automatically converts natural language educational prompts into fully rendered animations.

The goal is to make educational content creation accessible to everyone. Instead of manually writing animation logic, users simply describe what they want to visualize in plain English, and the system automatically generates, renders, and displays the animation.

Think of it as **"ChatGPT for educational animations."**

---

## Problem Statement

Creating educational animations traditionally requires:

* Expertise in animation frameworks such as Manim
* Knowledge of Python programming
* Manual scene design and coordinate management
* Significant development and rendering time

These requirements create a high barrier for educators, students, and content creators.

Animatrix removes this barrier by using Large Language Models (LLMs) to automatically generate animation code from natural language descriptions.

---

## Traditional vs AI-Powered Workflow

| Traditional Approach                      | Animatrix                             |
| ----------------------------------------- | ------------------------------------- |
| Developer manually writes animation logic | User enters a natural language prompt |
| Hard-coded coordinates and transitions    | AI generates complete animation code  |
| Requires programming expertise            | Accessible to non-programmers         |
| Time-consuming development process        | Automated end-to-end pipeline         |
| Manual rendering and debugging            | One-click generation and rendering    |

---

## System Architecture

```text
User Prompt
     │
     ▼
LLM (GPT / Claude / Gemini)
     │
     ▼
Generated Manim Code
     │
     ▼
Python Backend
     │
     ▼
Manim Renderer
     │
     ▼
Video Processing
     │
     ▼
Frontend Interface
```


---

## How It Works

### Step 1: User Prompt

The user provides a natural language instruction such as:

* "Explain the Pythagorean theorem"
* "Animate projectile motion"
* "Visualize binary search"
* "Show how Fourier series approximates a square wave"

No programming knowledge is required.

---

### Step 2: Prompt Understanding

The backend sends the prompt to an LLM.

The model determines:

* The educational concept
* Relevant visual objects
* Animation sequence
* Mathematical relationships
* Appropriate presentation strategy

---

### Step 3: Manim Code Generation

The LLM generates executable Python code using the Manim animation framework.

The generated code defines:

* Scenes
* Shapes
* Mathematical objects
* Labels
* Animations
* Transitions

---

### Step 4: Code Extraction

The backend processes the AI response and extracts only valid Python code.

This stage removes:

* Markdown formatting
* Explanatory text
* Non-code responses

The cleaned output is saved as:

```python
generated_scene.py
```

---

### Step 5: Automatic Rendering

The backend executes Manim programmatically.

```bash
manim generated_scene.py GeneratedScene
```

Manim automatically renders the animation into an MP4 file.

---

### Step 6: Video Processing

Optional post-processing is performed using:

* FFmpeg
* MoviePy

Possible operations include:

* Scene stitching
* Clip concatenation
* Transition effects
* Audio synchronization

---

### Step 7: Frontend Delivery

The generated animation is delivered through a web interface featuring:

* Prompt input field
* Generate button
* Loading status
* Embedded video player

---

## Technology Stack

| Technology                 | Purpose                         |
| -------------------------- | ------------------------------- |
| Python                     | Core backend language           |
| GPT / Claude / Gemini APIs | Code generation                 |
| Manim                      | Educational animation rendering |
| FastAPI                    | Backend API service             |
| FFmpeg                     | Video processing                |
| MoviePy                    | Video editing and composition   |
| React                      | Frontend interface              |
| HTML/CSS/JavaScript        | User interface                  |
| Docker                     | Containerization and deployment |

---

## Project Structure

```text
animatrix/
│
├── backend/
│   ├── app.py
│   ├── llm_handler.py
│   ├── code_extractor.py
│   ├── renderer.py
│   └── video_processor.py
│
├── frontend/
│   ├── src/
│   └── public/
│
├── generated/
│   ├── generated_scene.py
│   └── output.mp4
│
├── prompts/
│
├── tests/
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Week 1 Focus

The first phase of development focuses on LLM integration.

### Objectives

* Establish communication with AI APIs
* Send prompts programmatically
* Receive generated responses
* Extract valid Python code
* Build a reliable code-generation workflow

### Topics Covered

* REST APIs
* JSON responses
* Authentication using API keys
* Prompt engineering
* Response parsing
* Environment management using `.env`
* Basic Manim scene structure

---

## Core Engineering Challenges

Generating educational animations automatically is not simply a frontend problem.

The primary challenge is ensuring that AI-generated code is valid, executable, and visually correct.

Common issues include:

* Hallucinated Manim classes
* Syntax errors
* Runtime exceptions
* Deprecated API usage
* Invalid animation logic
* Visually incorrect outputs

As a result, prompt engineering, validation, and error handling are critical components of the system.

---

## Why This Project Matters

Animatrix combines multiple engineering disciplines into a single product:

### Artificial Intelligence

* Prompt engineering
* LLM integration
* Output validation

### Backend Engineering

* FastAPI
* File handling
* Process orchestration

### Automation

* Rendering pipelines
* Workflow management

### Graphics & Rendering

* Manim
* Video generation
* Scene composition

### Frontend Development

* React
* User experience design
* Video delivery

### DevOps

* Docker
* Deployment
* Environment management

This breadth makes Animatrix a strong demonstration of full-stack engineering, AI integration, and automation skills.

---

## Future Enhancements

* Multi-scene animation generation
* Interactive educational content
* Voice-over generation
* AI-generated narration
* Custom animation templates
* Cloud-based rendering infrastructure
* User authentication and project storage
* Real-time animation previews

---

## License

This project is intended for educational and research purposes.

---

## Author

Aditya Panwar
B.Tech, Mechanical Engineering
Indian Institute of Technology, Kanpur
