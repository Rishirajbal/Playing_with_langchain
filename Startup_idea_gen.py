import os
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain


groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = groq_api_key 


model = ChatGroq(
    temperature=0.4,
    model="meta-llama/llama-4-scout-17b-16e-instruct"
)


prompt1 = PromptTemplate(
    input_variables=["company_purpose"],
    template=(
        "You are a startup generator. Based on the company purpose: '{company_purpose}', "
        "generate a unique and useful startup idea. Also provide reasons for its uniqueness and usefulness."
    )
)
chain1 = LLMChain(llm=model, prompt=prompt1, output_key="startup_idea")


prompt2 = PromptTemplate(
    input_variables=["startup_idea"],
    template="Create a catchy and relevant startup name for the following idea: {startup_idea}"
)
chain2 = LLMChain(llm=model, prompt=prompt2, output_key="startup_name")


prompt3 = PromptTemplate(
    input_variables=["startup_idea"],
    template="Based on the startup idea: {startup_idea}, describe the ideal structure and team roles for the startup."
)
chain3 = LLMChain(llm=model, prompt=prompt3, output_key="startup_structure")


prompt4 = PromptTemplate(
    input_variables=["startup_idea"],
    template="What are the step-by-step actions needed to set up this startup: {startup_idea}?"
)
chain4 = LLMChain(llm=model, prompt=prompt4, output_key="startup_steps")


prompt5 = PromptTemplate(
    input_variables=["startup_idea", "startup_steps"],
    template=(
        "Based on the idea: {startup_idea} and the setup steps: {startup_steps}, "
        "how can this startup grow and scale successfully?"
    )
)
chain5 = LLMChain(llm=model, prompt=prompt5, output_key="startup_growth_steps")


startup_chain = SequentialChain(
    chains=[chain1, chain2, chain3, chain4, chain5],
    input_variables=["company_purpose"],
    output_variables=["startup_idea", "startup_name", "startup_structure", "startup_steps", "startup_growth_steps"],
    verbose=True  # This shows the intermediate steps
)

# Run the chain with user input
def generate_startup_info(company_purpose: str) -> dict:
    return startup_chain.invoke({"company_purpose": company_purpose})
