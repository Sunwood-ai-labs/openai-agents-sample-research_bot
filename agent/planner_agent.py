from pydantic import BaseModel
from openai import OpenAIChatCompletionsModel

from agents import Agent
from .provider import create_client, create_model_settings

PROMPT = (
    "You are a helpful research assistant. Given a query, come up with a set of web searches "
    "to perform to best answer the query. Output between 5 and 20 terms to query for."
)


class WebSearchItem(BaseModel):
    reason: str
    "Your reasoning for why this search is important to the query."

    query: str
    "The search term to use for the web search."


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
    """A list of web searches to perform to best answer the query."""


# OpenAIクライアントとモデル名を取得
client, model_name = create_client("gpt-4")

planner_agent = Agent(
    name="PlannerAgent",
    instructions=PROMPT,
    model=OpenAIChatCompletionsModel(
        model=model_name,
        openai_client=client,
    ),
    model_settings=create_model_settings(temperature=0.7),
    output_type=WebSearchPlan,
)
