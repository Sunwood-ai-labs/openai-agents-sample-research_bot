from agents import Agent, WebSearchTool
from openai import OpenAIChatCompletionsModel

from .provider import create_client, create_model_settings

INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term and"
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300"
    "words. Capture the main points. Write succintly, no need to have complete sentences or good"
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the"
    "essence and ignore any fluff. Do not include any additional commentary other than the summary"
    "itself."
)

# OpenAIクライアントとモデル名を取得
client, model_name = create_client("gpt-3.5-turbo")

search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    model=OpenAIChatCompletionsModel(
        model=model_name,
        openai_client=client,
    ),
    tools=[WebSearchTool()],
    model_settings=create_model_settings(temperature=0.5),
)
