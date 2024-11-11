# LLM CSV Agent

This project provides a Language Model (LLM) Agent capable of processing and interacting with CSV data. It’s designed to allow seamless interaction with structured datasets in CSV format, using a natural language interface powered by an LLM.

## Features

- **Interactive CSV Data Analysis**: This agent reads and interprets CSV data, allowing for intuitive data exploration and analysis through language prompts.
- **LLM-Powered Interface**: The agent leverages the power of language models for flexible and advanced data querying.
- **Customizable**: Designed for ease of customization, allowing you to tailor the LLM’s behavior to specific CSV data processing needs.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

You can install the dependencies by running:
```bash
pip install -r requirements.txt
```

## Usage

1. **Load the CSV Data**:
   Ensure the CSV file you wish to work with is placed in the appropriate directory or specify the path when initializing the agent.

2. **Run the Agent**:
   Run `main.py` to start interacting with the agent. You may input natural language queries, and the agent will process them to return relevant insights from the CSV data.

   ```bash
   python main.py
   ```

3. **Example Queries**:
   - "Show the summary statistics for the data."
   - "Find the highest value in column X."
   - "Filter rows where column Y is greater than 10."

## Files in This Repository

- **`main.py`**: The main script that initializes and runs the agent.
- **`episode_info.csv`**: Example CSV data file to demonstrate the agent’s capabilities.

## How It Works

The agent utilizes an LLM to interpret and respond to queries about the CSV data. By embedding the data into a format the LLM can understand, the agent makes it easy to ask questions in natural language, transforming typical CSV file analysis into a conversational experience.

## Customization

You can customize the model’s response format, add specific data-processing functionalities, or tailor the behavior of the agent to suit specific datasets.

## Contributions

Feel free to contribute by opening issues, improving documentation, or adding new features. Pull requests are welcome!
