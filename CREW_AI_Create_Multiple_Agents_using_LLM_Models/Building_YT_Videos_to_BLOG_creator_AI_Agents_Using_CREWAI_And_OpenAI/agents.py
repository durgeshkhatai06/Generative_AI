from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv
load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPEN_MODEL_NAME"] = "gpt-4-0125-preview"

## Create a senior blog content researcher
blog_researcher = Agent(
    role="Blog rearchers for Youtube Videos",
    goal="get the relevant video content for the topic{topic} from yt channel",
    verboe=True,  #see some information out over here
    memory=True,
    backstory=(
        "Expert in understanding videos in AI data science, Machine Leanrning and GenAI and providing suggetions"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delagation=True
)

##Creating a senior blog writter agent with YT tool
blog_writter = Agent(
    role="Blog writter",
    goal="Narrate compelling tech stories about the video {topic} from YT channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics,you craft"
        "engaging narratives  that captivate and aducate,bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delagation=False
)