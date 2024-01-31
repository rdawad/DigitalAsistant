import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu



# Some important links for fonts and style to build UI
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Kalam:wght@700&family=Permanent+Marker&display=swap" rel="stylesheet">',unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


# Menu Bar for Multipages
selected2 = option_menu(None, ["Data", "App", "Summary"], 
    icons=['bar-chart-line-fill', 'app-indicator', "person-badge"], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected2 == "Data":
    def main():
        st.header("KPH Digital Assistant 💬")
        # upload file
        pdf = st.file_uploader("Upload your RFP details", type=["pdf","xlsx"])

        if pdf is not None:
            pdf_reader = "Test UI"
            st.write("File uploaded sucessfully")
    main()

elif selected2 == "App":
    def main():
        # st.set_page_config(page_title="KPH Digital Assistant")
        st.header("💬 KPH RFP Assistant ")

        prompt = st.text_area("Ask a question", height=100)
        #logdata()

        if st.button("Submit Query", type="primary"):

        # embeddings = OpenAIEmbeddings(deployment="deploymnet-embeddings", chunk_size= 16)
            vector_db=None
            #persist_directory="KPH_KnowledgeDB/"
            #vector_db = Chroma(embedding_function=embeddings,
                    # persist_directory=persist_directory)
            # Create a retriever from the Chroma vector database
            #k=3
            #retriever = vector_db.as_retriever(search_kwargs={"k": k})

            # Use a ChatOpenAI model
            #llm = AzureChatOpenAI(model_name='gpt-3.5-turbo',deployment_name="deployment-gptturbo35", temperature=0)

            # Create a RetrievalQA from the model and retriever
            #qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever,return_source_documents = True)
                

            # Run the prompt and return the response
            result="Describe your ability to work with any selected medical plan to develop management of annual out of pocket member maximums, a real-time shared accumulator for clients offering High Deductible Health Plans (“HDHP”). Please include any first year start up fees and annual services fees if any for these services. Confirmed"
            #logger.info("Response:",response)
            st.write("**Answer:**",result)
            
            metadatastr = "source_documents: Document(page_content=\" \", metadata={'source': 'Section II - Questionnaire.pdf_Page_25'})"
            st.write("**Source:**","Section II - Questionnaire.pdf_Page_25")
            st.write("**Content:**","Confidential and Proprietary  |  ©2023 ProAct, Inc. All Rights Reserved.  \\n  \\n \\n  The Customer Service Representatives use all their resources to correct any difficulty while still on the telephone \\nwith the member or the pharmacy. In 95% of the cases, any problems are handled that business day or within")
    main()

elif selected2 == "Summary":
    def file_preprocessing(file):
    
        final_texts = ""
        
        return final_texts

#LLM pipeline
    def llm_pipeline(filepath):
        result = []

        summary=""
        result.append(summary)

        return result

    @st.cache_data
    #function to display the PDF of a given file 
    def displayPDF(file):
        return ""
        
    # st.set_page_config(layout="wide")

    def main():
        st.title("Document Summarization App")

        uploaded_file = st.file_uploader("Upload your PDF file", type=['pdf'])

        if uploaded_file is not None:
            if st.button("Summarize"):
                col1, col2 = st.columns(2)
                filepath = "data/"+uploaded_file.name
                with open(filepath, "wb") as temp_file:
                    temp_file.write(uploaded_file.read())
                #with col1:
                    #st.info("Uploaded File")
                    #pdf_view = displayPDF(filepath)

                #with col2:
                #summary = llm_pipeline(filepath)
                summary = "Test Summarization details"
                st.info("Summarization Complete")
                st.success(summary)  
    main()              



# Top  nav bar head
st.markdown("""

<nav class="navbar fixed-top navbar-expand-lg" style="background-color: #444e5a;margin-top:40px;height:15vh;">
  <a class="navbar-brand" style='color:	#F5F5F5;font-size:38px; margin-left:520px;font-weight:bold;'>tieto<span style='font-family:Kalam,cursive;font-size:33px;'>EVRY</span></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
</nav>
""", unsafe_allow_html=True)


# some important scrips to function the application
st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)




# The Footer
footer = """
    <style>
        .footer {
            position: fixed;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: white;
            padding: 10px;
            text-align: center;
            border-top: 1px solid gray;
            color:black
        }
    </style>
    <div class="footer">
        Copyright © TietoEVRY 2021
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)





# Embeded App
# st.markdown("""
#     <style>
#         .embedded-iframe {
#             width: 50vw; /* 100% of the viewport width */
#             height: 100vh; /* 100% of the viewport height */
#             border: none; /* Remove border */
#         }
#     </style>
#     <iframe class="embedded-iframe" src="https://30days.streamlit.app/?embed=true"></iframe>
# """, unsafe_allow_html=True)