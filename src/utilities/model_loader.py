from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

bedrock_client = boto3.client(service_name="bedrock-runtime")

def get_trained_model():
    return Bedrock(model_id="anthropic.claude-v2:2", client=bedrock_client, model_kwargs={"max_tokens_to_sample": 700})

def handle_llm_interaction(llm, vectorstore, question):
    prompt_template = """
    Human: I have some context from a VALORANT game match dataset.

    You are hired as a data scientist on a new VALORANT esports team and have been tasked by the team’s general manager to support the scouting and recruitment process.

    Build a LLM-powered digital assistant with a chat interface using Amazon Bedrock’s native capabilities. Use this new technology to build teams and answer various questions about VALORANT esports players, leveraging provided data sources and demonstrating effective information retrieval and analysis.

    For each team composition:
    Answer questions about player performance with specific agents (in-game playable characters)
    Assign roles to players on the team and explain their contribution
    Offensive vs. defensive roles
    Category of in-game playable character / agent (duelist, sentinel, controller, initiator)
    Assign a team IGL (team leader, primary strategist and shotcaller)
    Provide insights on team strategy and hypothesize team strengths and weaknesses
    
    Please use the following context to answer the question.
    <context>
    {context}
    </context>

    Question: {question}

    Assistant: 
    """

    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="map_reduce",
        retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    
    response = qa({"query": question})
    return response['result']
