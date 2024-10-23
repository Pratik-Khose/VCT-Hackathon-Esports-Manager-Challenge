# Project Submission for Hackathon: LLM-Powered Digital Assistant for VALORANT Esports Team Scouting

## Team Name: Team Alpha

### **Overview:**

We have developed ValorScout, an AI-powered digital assistant designed to assist VALORANT esports team managers in scouting, recruiting, and assembling optimal team compositions. This assistant leverages Amazon Bedrock's capabilities, particularly its support for large language models (LLMs), to analyze player data and provide actionable insights that help in decision-making. The project focuses on streamlining the process of building effective VALORANT teams by using advanced AI techniques for analyzing and interpreting esports data.

Our solution includes a conversational chatbot interface built with Streamlit, allowing easy and interactive queries, providing real-time answers, and suggesting team configurations based on various factors like player strengths, roles, and synergy between players. We also integrated LLM fine-tuning techniques to make the assistant highly specific and efficient for the VALORANT esports domain.

### **Problem Statement:**
In esports, assembling a balanced and effective team is critical for success. The process of scouting players, evaluating their roles, and predicting team synergy can be highly time-consuming and subjective. Our goal was to build a digital assistant that would automate and optimize this process for a VALORANT team’s general manager or recruiter by delivering data-driven insights and recommendations.

### **Solution Summary:**
ValorScout was designed to solve this challenge by providing a LLM-powered chatbot that allows users to interact with esports data efficiently. The assistant is capable of answering various questions about players and teams, helping in role assignment, evaluating team compositions, and offering justifications for specific configurations. By using Amazon Bedrock’s fine-tuned models, the assistant understands the VALORANT esports domain and delivers precise, contextually relevant responses.

## **Technology Stack & Detailed Workflow:**

1. **Amazon Bedrock for LLMs:** 

- We used Amazon Bedrock, a fully managed service from AWS that provides access to pre-trained large language models (LLMs) from various providers. The models were specifically fine-tuned on VALORANT esports data.

- **Fine-tuning process:** We fine-tuned the LLM models to understand VALORANT-specific terms, player roles, statistics, and strategies. This was done by feeding the model extensive data on player stats, role assignments, tournament results, and team compositions from various data sources. The fine-tuning helped the model become domain-specific, making it much more effective at answering queries related to team-building decisions.
- The models were trained to evaluate player performance metrics like average combat score (ACS), kills/deaths ratio (K/D), damage per round (DPR), and others.

2. **Data Ingestion & Storage:**

- **Data Sources:** We gathered and formatted data from multiple sources, including official VALORANT API endpoints, community-built datasets, and esports player stats. This data includes detailed player information such as their preferred agents, play styles, roles (Duelist, Controller, Initiator, Sentinel), and their match history.
- We used AWS S3 to store the data, ensuring scalability and quick access. The data is loaded into the LLM-powered system to enable real-time queries.

3. **Streamlit Frontend for Chatbot Interface:**

- We built the user interface with Streamlit, a powerful tool for creating data-driven web applications with minimal effort. The interface offers a conversational chatbot where the user (team manager, recruiter, etc.) can ask questions.

- The chatbot retrieves the relevant information using Amazon Bedrock's fine-tuned LLM and displays the response in an easy-to-read format, often accompanied by data visualizations.

4. **LLM Fine-Tuning & Deployment on AWS Bedrock:**

- **Fine-tuning:** The LLM model provided by Bedrock was further fine-tuned using domain-specific datasets. We built a custom training pipeline that trained the model on specific VALORANT terminology, game mechanics, and player/team analytics. This significantly improved the model’s accuracy in generating esports-related insights.
- **LLM Hosting and Scalability:** The fine-tuned model was deployed using Amazon Bedrock, which offers a robust infrastructure for hosting LLMs. Bedrock’s capabilities ensure that the assistant can handle multiple simultaneous queries with low latency and scale according to the load.

5. **Information Retrieval & Analysis:**

- The assistant uses vector-based semantic search for efficient information retrieval, ensuring that even complex, natural language queries return relevant results quickly. For example, when asked to build a team, the system pulls the necessary player stats, performs role-based analysis, and suggests a lineup.
Additionally, it uses algorithms for player role assignment based on team needs, considering various attributes like experience, team synergy, and flexibility in agent selection.
 
## **Key Features:**
- **Conversational AI Chat Interface:**

    - Users can interact with ValorScout through natural language queries. The LLM responds conversationally while delivering in-depth analysis based on the question.

- **Player Role Assignment:**

    - The assistant uses VALORANT player data to suggest roles like Duelist, Initiator, or Sentinel. It evaluates the strengths of each player and their synergy with others to form the best possible team compositions.
- **Team Synergy Analysis:**
    - The assistant evaluates potential team lineups, analyzes past team performance metrics, and gives insights on how well players perform together.
 
- **Query Capabilities:**

    - The assistant can handle complex, multi-part queries like. It processes the requests and responds with detailed, actionable insights.

## **Challenges & Learning:**

- **Fine-tuning LLM for Domain Specificity:**

    - One of the key challenges was fine-tuning the model to understand VALORANT-specific terms, player roles, and game mechanics. We overcame this by carefully selecting relevant datasets and performing multiple iterations of training.
- **Data Retrieval:**

    - Ensuring that the model retrieves trained data from esports sources required building a dynamic data pipeline integrated with APIs and databases that provide up-to-date player stats.
- **Scalability:**
    - Using Amazon Bedrock ensured that the solution could scale to accommodate high traffic loads and deliver low-latency responses, a crucial feature for a real-time esports assistant.
    
## Conclusion:
ValorScout is a highly specialized AI assistant designed to automate and enhance the esports recruitment process. By leveraging cutting-edge technology like Amazon Bedrock, LLMs, and Streamlit, we have created a powerful, user-friendly tool that delivers insightful recommendations on player roles, team compositions, and player synergy. It streamlines the decision-making process for esports managers, allowing them to focus on strategy and talent, while the AI handles data retrieval, analysis, and optimization.

This project demonstrates the potential of AI in esports by empowering team managers with real-time, data-driven insights that can be crucial for success in the competitive world of VALORANT.