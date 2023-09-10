import os
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

# os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'
HUGGINGFACEHUB_API_TOKEN = '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'

def usermessage(usermessage):

    question = usermessage

    template = """ what are problem we can suffered when {question} traffic management . we are using cameras to detect traffic and when car disobey the the rule he/she we get fine give mme in points """

    prompt = PromptTemplate(template=template, input_variables=["question"])
    repo_id = "gpt2"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 0.8},
        huggingfacehub_api_token='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'
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print(llm_chain.run(question))

    return (llm_chain.run(question))

print(usermessage('building'))