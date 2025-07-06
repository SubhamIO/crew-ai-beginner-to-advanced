from crewai import Agent, Task, Crew, LLM

# Export your OPENAI_API_KEY

llm = LLM(model="gpt-4")

# User inputs
main_ingredient = "tomato"
dietary_restrictions = "shrimps"

culinary_assistant = Agent(
    llm=llm,
    role="Culinary Assistant",
    backstory="An experienced culinary assistant skilled in finding and tailoring recipes based on ingredients and dietary"
    "needs, and providing clear, step-by-step cooking instructions",
    goal="Find recipes, filter them to meet dietary preferences, and guide user through recipe steps.",
    verbose=True,
)

# Tasks
find_and_filter_recipes = Task(
    description=f"Find recipes that uses the ingredient: {main_ingredient} and"
    f" filter them to meet dietary restrictions: {dietary_restrictions}.",
    expected_output=f"One recipe using {main_ingredient} and matching {dietary_restrictions} restrictions.",
    agent=culinary_assistant,
)

guide_recipe_steps = Task(
    description="Provide step-by-step instructions for the selected recipe.",
    expected_output="Step-by-step cooking instructions for the chosen recipe.",
    agent=culinary_assistant,
)

crew = Crew(
    agents=[culinary_assistant],
    tasks=[find_and_filter_recipes, guide_recipe_steps],
    planning=True,
)

crew.kickoff()
