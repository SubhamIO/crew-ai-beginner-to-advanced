from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

product_name = "energy drink"

strategist_backstory = "and marketing strategy"

market_researcher = Agent(
    role="Market Researcher",
    goal="Analyze market trends for the product launch",
    backstory="Experienced in market trends and consumer behavior analysis",
    tools=[SerperDevTool()],
    verbose=True,
)

strategist = Agent(
    role="Product Strategist",
    goal="Create effective positioning strategies for the product",
    backstory=f"Skilled in competitive positioning {strategist_backstory}",
    verbose=True,
)

gather_market_insights_task = Task(
    description=f"Browse the internet to gather insights on current market trends for the launch of the {product_name} product.",
    expected_output=f"List of relevant market trends and consumer preferences, relevant to {product_name}",
    agent=market_researcher,
)

develop_positioning_strategy_task = Task(
    description="Based on the market insights,"
                f"create a positioning strategy for the {product_name} product, including analysis for impact and target audience.",
    expected_output="A positioning strategy with target audience and impact notes",
    agent=strategist,
    verbose=True,
)

crew = Crew(
    agents=[market_researcher, strategist],
    tasks=[gather_market_insights_task, develop_positioning_strategy_task],
    planning=True,
)

crew.kickoff()
