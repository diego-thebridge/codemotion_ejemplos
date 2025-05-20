from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.callbacks import get_openai_callback

from tools import get_circle_area, get_square_area

from dotenv import load_dotenv
import os
from pprint import pprint

def create_main_agent():

    load_dotenv()

    tools = [get_circle_area, get_square_area]

    ''' 
    react_template = """You are an assistant than helps people with geometry.
                        Answer the following questions as best you can
                        You have access to the following tools:

                        {tools}

                        Use the following format:

                        Question: the input question you must answer
                        Thought: you should always think about what to do
                        Action: the action to take, should be one of [{tool_names}]
                        Action Input: the input to the action
                        Observation: the result of the action
                            ... (this Thought/Action/Action Input/Observation can repeat N times)
                        Thought: I now know the final answer
                        Final Answer: the final answer to the original input question

                        Begin!

                        {chat_history}
                        Question: {input}
                        Thought:{agent_scratchpad}"""
    '''

    #react_prompt = PromptTemplate.from_template(react_template)
    react_prompt = hub.pull("hwchase17/react")

    # Added input_key and output_key params because the extra {plan} variable in the prompt. TODO: why?
    # You need to add set the input_key when you define your memory so that the memory save_context method knows
    # where to place the user input. If not, arises an error because there's ambiguity about whether "input" or "plan"
    # are the keys that should contain the new user input.
    memory = ConversationBufferMemory(memory_key="chat_history")

    # Choose the LLM to use
    llm = ChatOpenAI(model="gpt-4o",temperature=0)

    # Construct the ReAct agent
    main_agent = create_react_agent(llm, tools, react_prompt)

    # Create an agent executor by passing in the agent and tools
    agent_executor = AgentExecutor(agent=main_agent,
                                   tools=tools,
                                   memory=memory,
                                   verbose=True,
                                   handle_parsing_errors=True,
                                   return_intermediate_steps=True)

    return agent_executor


def main():

    main_agent = create_main_agent()

    while True:
        query = input("Type yor query: ")
        result = main_agent.invoke({"input":query})
        print(result['output'])
        print(result["intermediate_steps"][0][0].log)

if __name__ == "__main__":
    main()
