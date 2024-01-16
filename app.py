import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#Func to get response from Llama2 Model


def getLlamaresponse(input_text,no_words,content_style):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
    model_type = 'llama',
    config = {'max_new_tokens':256,
    'temperature':0.01})

    #####Prompt Template

    template = """
        Write a content for {content_style} job profile for a topic {input_text} within the {no_words} words.
        """

    prompt = PromptTemplate(input_variables=["content_style","input_text","no_words"], template = template)

    response = llm(prompt.format(content_style=content_style,input_text=input_text,no_words=no_words))

    print(response)
    return response




st.set_page_config(page_title = "Generate Content",
page_icon = 'Kyndryl',
layout = 'centered',
initial_sidebar_state= 'collapsed')

st.header("Generate the Contents !")

input_text = st.text_input("Enter the Content Topic")

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("Enter How much words you want?")

with col2:
    content_style = st.selectbox("Writing the Content for",('Researchers','DataScientist','CommonPeople'),index=0)


submit = st.button("Generate")

###Final Response

if submit:
    st.write(getLlamaresponse(input_text,no_words,content_style))