import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep, time
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

JD="""
Primary Responsibilities

Design and develop AI/ML and Generative AI-enabled applications addressing real business and engineering problems
Build solutions using LLMs, prompt engineering, RAG, embeddings, vector databases and agentic AI patterns
Develop and integrate AI agents with enterprise applications, APIs, databases and knowledge sources
Build reusable AI components, services and APIs that can be consumed across engineering teams
Develop Python-based backend services and REST APIs supporting AI/ML capabilities
Participate across the complete AI solution lifecycle: problem definition, prototyping, evaluation, development, testing, deployment and production support
Establish lightweight evaluation frameworks and metrics to measure solution quality, accuracy, reliability and business usefulness
Implement appropriate guardrails, observability and human-in-the-loop controls for enterprise AI solutions
Work with cloud and engineering teams to deploy AI capabilities into scalable production environments
Apply software-engineering practices including Git, code reviews, automated testing and CI/CD
Partner with product owners, architects, business teams and engineering teams to translate business problems into practical AI solutions
Continuously evaluate emerging AI capabilities and identify opportunities where AI can improve developer productivity, operational efficiency or customer/business outcomes
Comply with all applicable Company policies, procedures, and business directives, changes including those relating to work location, team assignments, work schedules, and flexible work arrangements

Required Qualifications

Bachelor's degree in Computer Science, Engineering, Data Science, AI/ML or a related technical field, or equivalent practical experience
Experience or solid practical understanding of:
Prompt engineering
RAG
Embeddings
Vector databases
LLM APIs
Agent/tool-calling concepts
Experience developing REST APIs / backend services
Solid programming fundamentals with hands-on experience in Python
Hands-on knowledge of Generative AI / Large Language Models
Understanding of core machine-learning concepts and model lifecycle
Understanding of cloud-native application development, preferably GCP, Azure or AWS
Familiarity with Git-based source control and modern CI/CD practices
Demonstrated solid analytical and problem-solving skills
Demonstrated ability to communicate effectively with both technical and non-technical stakeholders
Preferred Qualifications

Hands-on experience with frameworks such as LangChain, LangGraph, Semantic Kernel or comparable agent/orchestration frameworks
Experience with vector stores and semantic search
Experience with Docker, Kubernetes or containerized workloads
Experience integrating AI solutions with existing Java, .NET or Python enterprise applications
Healthcare technology experience 
Exposure to MLOps / LLMOps, model monitoring and evaluation
Exposure to enterprise security, privacy and Responsible AI principles

"""

Resume="""
ASHISH KUMAR
Delhi, India | 9142569558 | ashish232019@gmail.com | LinkedIn | GitHub
Professional Summary
I am a B.Tech CSIT graduate with hands-on experience in LLM evaluation, full-stack applications, backend APIs, databases, and general tools. Skilled in Python, C/C++, Java, SQL, React, Node.js, and machine learning, with experience in developing data-driven applications. With good adaptability and problem-solving skills, I am eager to contribute to software development,
AI-based development, and teams, while continuing to learn, grow, and contribute to the organisation.
Technical Skills
AI / Machine Learning: RAG, LLM Evaluation, Prompt Engineering, AI Agents, AI Output Validation, AI Data Annotation, Multimodal AI Evaluation, Machine Learning
Programming Languages: Python, C, C++, Java, SQL
Databases: MySQL, PostgreSQL, MongoDB, SQLite
Web Technologies: HTML, CSS, JavaScript, React.js, Node.js, Express.js, Django, FastAPI, REST APIs
Tools and Platforms: Git, GitHub, Jira, Google Cloud Platform, Render, Railway, Vercel, Excel, Ollama
Education
Acropolis Institute of Technology and Research 2022 - 2026
B.Tech. in Computer Science and Information Technology Indore, India | CGPA: 7.22/10
DAV 2021
Senior Secondary School Certificate (Class 10+2) Percentage: 77.67%
Sharon’s Public School 2019
High School Certificate (Class 10) Percentage: 88.4%
Experience
Ethara.AI Jan 2026 - May 2026
LLM Post-Training Intern India
•
Reviewed 1000+ AI-generated outputs across text, image, video, speech, and language model tasks according to project requirements.
•
Validated 500+ AI outputs for accuracy, consistency, compliance with instructions, user satisfaction, and overall quality.
•
Contributed to review process improvements associated with a 15% average reduction in review errors.
•
Guided 50+ team members through live video calls to resolve day-to-day issues and support project workflows.
Acropolis Institute of Technology and Research Aug 2025 - Sep 2025
MERN Full-Stack Training Indore, India
•
Developed full-stack web applications using MongoDB, MySQL, Express.js, React.js, and Node.js.
•
Worked with databases and multiple APIs while developing and validating application software.
•
Identified and resolved technical issues during development and deployment and documented solutions.
•
Used GitHub, Render, Vercel, and Railway during development and deployment.
Projects
PyVectorDB - Lightweight Vector Database & RAG Engine | Python, FastAPI, SQLite, React, Ollama 2026
•
Created a vector database and RAG model for document indexing, semantic search, and question answering in 3 document formats.
•
Built document chunking, vector embedding generation, vector database storage, and vector-retrieval based on metadata.
•
Implemented 3 vector search approaches:- Brute Force, KD-Tree, and HNSW for similarity retrieval.
•
Built API using FastAPI, React, and Ollama to retrieve source-cited answers from the documents.
Tirth Saathi - Smart Pilgrimage Companion | React.js, Node.js, Express.js, MongoDB, APIs Dec 2025 - May 2026
•
Constructed a pilgrimage platform integrating 10+ functionalities designed to improve pilgrim’s travel and spiritual experiences.
•
Worked on backend development, database management, and application integration.
Smart Shop - AI Recommendation System | Python, Django, PostgreSQL, JavaScript, APIs Aug 2024 - Dec 2024
•
Designed an e-commerce application with a personalized recommendation engine to suggest products based on user preferences.
•
Contributed to frontend development, database, and API and payment integration.
Certifications
•
NPTEL - Programming in Java Dec 2024
•
NPTEL - Database Management System Sep 2024
•
Google Cloud Certification Dec 2025
"""

def ask_LLM(system_prompt, user_prompt):
    sys_msg ={
        "role": "system",
        "content": system_prompt
    }
    user_msg ={
         "role": "user",
         "content": user_prompt
    }
    messages=[sys_msg, user_msg]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    answer = response.choices[0].message.content
    return answer


def step1_res_extract(Resume):
    print("1.")
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the candidate resume provided.
    ONLY return the skills no other information. Do not invent any skills by your self
    OUTPUT FORMAT:
    Skill1, Skill2, Skill3, Skill4, Skill5, Skill6, ........ and please do add any filler skills by your self.
    """
    
    user_prompt=f"""
    Extract the skills from this resume:
    {Resume}"""
    return ask_LLM(system_prompt, user_prompt)

def step2_JD_extract(JD):
    print("2.")
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the job description provided.
    ONLY return the skills no other information. Do not invent any skills by your self.
    OUTPUT FORMAT:
    Skill1, Skill2, Skill3, Skill4, Skill5, Skill6, ........ and please do add any filler skills by your self.
    """
    
    user_prompt=f"""
    Extract the skills from this job description:
    {JD}"""
    return ask_LLM(system_prompt, user_prompt)

def step3_match(Candidate, JD):
    print("3.")
    system_prompt="""
    You are a professional HR assistant. Compare the skills extracted from the candidate resume and the skills required in the job description.
    ONLY return the matching skills, no other information. Do not invent any skills by your self
    AND produce a final score between 0 to 100 based on the matching skills.
    Also produce a verdict whether the candidate is fit for the role.
    """
    
    user_prompt=f"""
    Compare and match skills from the candidate:
    {Candidate}
    with these skills required in the job description:
    {JD}"""
    return ask_LLM(system_prompt, user_prompt)

candidate_skills = step1_res_extract(Resume)
print(candidate_skills)
sleep(2)
jd_skills = step2_JD_extract(JD)
print(jd_skills)
sleep(2)
Score= step3_match(candidate_skills, jd_skills)
print(Score)