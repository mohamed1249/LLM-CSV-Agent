from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_ollama import ChatOllama
from langchain.schema import OutputParserException
from langchain_core.output_parsers import JsonOutputParser
from langchain.callbacks.tracers import ConsoleCallbackHandler

load_dotenv()

# Define a custom output parser
# This regex pattern will parse outputs in a specific structure we expect
output_parser = JsonOutputParser()

def main():
    print("Start...")

    # Create the CSV agent with the custom output parser
    csv_agent = create_csv_agent(
        llm=ChatOllama(
            model="deepseek-coder-v2",
            temperature=0.9,
        ),
        path="episode_info.csv",
        verbose=True,
        allow_dangerous_code=True,
        output_parser=output_parser,
        handle_parsing_errors=True
    )

    # Use the agent to perform the task with structured output
    try:
        result = csv_agent.invoke(
            input={
                "input": "Sort the seasons by the number of episodes they have.",
                'handle_parsing_errors': True},
                # config={"callbacks":[ConsoleCallbackHandler()]},
                handle_parsing_errors = True
        )
        print(result)
    except OutputParserException as e:
        print("Failed to parse output:", e)

if __name__ == "__main__":
    main()
