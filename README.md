# StudyMate AI — Applied AI Project

## Overview
StudyMate AI is an AI-powered academic assistant. It uses a large language model (LLM), prompt engineering, structured inputs, and a defined workflow to generate personalized study plans and explain academic concepts.

## Main features
- Personalized study timetable generation
- Topic prioritization based on weak areas
- Revision and practice recommendations
- Follow-up academic Q&A

## Files
- `studymate_ai_agent_config.json`: agent instructions, model configuration, input/output schema, workflow, and deployment metadata.
- `sample_input_output.json`: illustrative request and response.

## How it works
1. Collect the student's subjects, exam date, available hours, and preparation level.
2. Validate the input.
3. Construct a prompt using the agent's system instructions.
4. Send the prompt to an LLM provider (for example, Google Gemini).
5. Format the response as a timetable and revision strategy.
6. Accept follow-up requests to refine the plan.

## Run/deployment status
The included files are project configuration and sample data, not a deployed application. To make it live, build a small Streamlit or web interface, connect an LLM API key through an environment secret named `GEMINI_API_KEY`, and deploy it using Streamlit Community Cloud, Render, or Hugging Face Spaces.

**Deployed URL:** Not deployed yet. Do not submit a made-up URL. If the form requires a URL, deploy the app first and paste the public hosting URL.

## Run locally
```bash
pip install -r requirements.txt
# Set GEMINI_API_KEY in your environment, then:
streamlit run app.py
```

For Streamlit Community Cloud, connect this folder's GitHub repository and add
`GEMINI_API_KEY` under App settings → Secrets. The app's public URL is assigned
by the hosting platform after deployment.
