import boto3
from botocore.exceptions import ClientError

# Function to invoke the LLM-powered digital assistant for team compositions in VALORANT
def invoke_valorant_agent(agent_id, agent_alias_id, session_id, prompt):
    """
    This function interacts with the Amazon Bedrock service to generate
    team compositions and assign player roles based on the provided prompt.
    It leverages the Bedrock Agent Runtime API to fetch LLM responses.
    
    Parameters:
    - agent_id: The ID of the Bedrock agent to be used.
    - agent_alias_id: Alias ID for the agent.
    - session_id: A unique session identifier for the conversation.
    - prompt: The input prompt (questions/requests) for the digital assistant.
    
    Returns:
    A dictionary containing the generated output text, citations for data sources,
    and trace information (for debugging and analysis).
    """
    
    try:
        # Initialize the Bedrock Agent Runtime client
        client = boto3.session.Session().client(service_name="bedrock-agent-runtime")

        # Invoke the agent with the given prompt
        response = client.invoke_agent(
            agentId=agent_id,
            agentAliasId=agent_alias_id,
            enableTrace=True,  # Enable tracing for debug purposes
            sessionId=session_id,
            inputText=prompt,
        )

        # Initialize variables for output
        output_text = ""
        citations = []
        trace = {}

        # Flags and logic for processing the response
        has_guardrail_trace = False
        for event in response.get("completion"):
            # Combine the response chunks to form the final output text
            if "chunk" in event:
                chunk = event["chunk"]
                output_text += chunk["bytes"].decode()

                # Handle attributions for cited data sources
                if "attribution" in chunk:
                    citations.extend(chunk["attribution"]["citations"])

            # Extract trace information for debugging and analysis
            if "trace" in event:
                for trace_type in ["guardrailTrace", "preProcessingTrace", "orchestrationTrace", "postProcessingTrace"]:
                    if trace_type in event["trace"]["trace"]:
                        mapped_trace_type = trace_type
                        if trace_type == "guardrailTrace":
                            if not has_guardrail_trace:
                                has_guardrail_trace = True
                                mapped_trace_type = "preGuardrailTrace"
                            else:
                                mapped_trace_type = "postGuardrailTrace"
                        if trace_type not in trace:
                            trace[mapped_trace_type] = []
                        trace[mapped_trace_type].append(event["trace"]["trace"][trace_type])

    except ClientError as e:
        # Handle exceptions that may occur during the API call
        raise

    # Return the structured response
    return {
        "output_text": output_text,
        "citations": citations,
        "trace": trace
    }

