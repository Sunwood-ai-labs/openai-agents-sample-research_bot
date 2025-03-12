# Agent used to synthesize a final report from the individual summaries.
from pydantic import BaseModel
from openai import OpenAIChatCompletionsModel

from agents import Agent
from .provider import create_client, create_model_settings

PROMPT = (
    "You are a senior researcher tasked with writing a cohesive report for a research query. "
    "You will be provided with the original query, and some initial research done by a research "
    "assistant.\n"
    "You should first come up with an outline for the report that describes the structure and "
    "flow of the report. Then, generate the report and return that as your final output.\n"
    "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
    "for 5-10 pages of content, at least 1000 words."
)


class ReportData(BaseModel):
    short_summary: str
    """A short 2-3 sentence summary of the findings."""

    markdown_report: str
    """The final report"""

    follow_up_questions: list[str]
    """Suggested topics to research further"""


# OpenAIクライアントとモデル名を取得
client, model_name = create_client("gpt-4")

writer_agent = Agent(
    name="WriterAgent",
    instructions=PROMPT,
    model=OpenAIChatCompletionsModel(
        model=model_name,
        openai_client=client,
    ),
    model_settings=create_model_settings(temperature=0.7),
    output_type=ReportData,
)
