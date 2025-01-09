from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

header_template = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Initialize WebBaseLoader with the header_template
loader = WebBaseLoader(
    web_path="https://www.tesla.com/careers/search/job/machine-learning-engineer-motion-planning-self-driving-221945",
    header_template=header_template
)


docs = loader.load()
page_data = loader.load().pop().page_content
print("Page data", page_data)

# print(docs)




# prompt_extract = PromptTemplate.from_template(
#             """
#             ### JOB DESCRIPTION:
#             {job_description}

#             ### INSTRUCTION:
#             You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
#             the seamless integration of business processes through automated tools. 
#             Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
#             process optimization, cost reduction, and heightened overall efficiency. 
#             Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
#             in fulfilling their needs.
#             Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
#             Remember you are Mohan, BDE at AtliQ. 
#             Do not provide a preamble.
#             ### EMAIL (NO PREAMBLE):

#             """
#         )

# chain_extract = prompt_extract | llm
# res = chain_extract.invoke(input={'job_description': page_data})
# print(res.content)



# from langchain_groq import ChatGroq
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(
#     model="mixtral-8x7b-32768",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     # other params...
# )

# messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to French. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
# ]
# ai_msg = llm.invoke(messages)
# print(ai_msg.content)

