from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writter


##Research Task
research_task = Task(
    description=(
        "Identify the video {topic}.",
        "Get the detailed information  about the video from the  channel."
        ),
    expected_output="A  comprehensive 3 paragraphs long report based upon the {topic} of the video content",
    tools=[yt_tool],
    agent=blog_researcher
)

##Writting task with language model configuration
write_task = Task(
    description=(
        "Get the info from the Youtube channel video on the topic {topic}."
        ),
    expected_output="Summerize the in info from the youtube channel video on the topic{topic} and create the content for the blog",
    tools=[yt_tool],
    agent=blog_writter,
    async_execution =  False, ##Both the agects are not parellay working
    output_file="new-blog-post.md" 
)