import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"))

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job):
        prompt_email = PromptTemplate.from_template(
            """
            JOB DESCRIPTION:
        {job_description}

        INSTRUCTION:
        You are Shiva Khatri, a Software Engineer/Data Science Engineer at North American Stainless (NAS). 
        Write a cover letter to the client regarding the job mentioned above. Highlight NAS’s capabilities
          and your extensive expertise, including:

        Advanced Data Analysis: Python, R, PowerBI, NumPy, Pandas
        Real-Time Monitoring & Anomaly Detection: Vertex AI, Flask, React, BigQuery
        ETL & Data Integration: Google Cloud (PubSub, Dataflow, BigQuery), RabbitMQ
        Web & Application Development: Node.js, SQL, Next.js, Angular
        Machine Learning & AI: GPT4ALL, multi-threaded programming
        Technical Proficiency: Java, Typescript, C, C#, C++, Ruby, Solidity
        Project Impact: Process optimization, scalability, cost efficiency, product quality enhancement
        Emphasize NAS’s innovative approach to technology and how your diverse skill set aligns with and can meet the client’s specific needs.

        COVER LETTER (NO PREAMBLE):

        """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job)})
        return res.content
    
    def resume_points(self, job):
        prompt_resume = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are a resume expert. Your job is to extract key points from the job description that can be used to tailor a resume. 
            Provide me relevant skills, technologies, and experiences. Provide the points in bullet format. Along with all that, try to give
            me the ideal resume points that match the job description which matches the skills and experiences and pass the ATS.
            In total I want relevant skills, technologies, and experiences with ideal resume bullet points starting with action verb.

            ### RESUME POINTS (NO PREAMBLE):
            """
        )
        chain_resume = prompt_resume | self.llm
        res = chain_resume.invoke({"job_description": str(job)})
        return res.content

        