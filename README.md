## Medical Chatbot using GenAI

#### Setup Environment
- create a vitual environmet using below command
        ```
        conda create -p env python=3.8 -y
        ```
- Activate virtual environmet using below command
        ```
        conda activate env
        ```
- Install the project dependency using below command
           ```
        pip install -r requirements.txt
        ``` 
-   Check  install libraries using command
        ```
        pip list
        ```
- if face any error reqgarding kernel execute below command
                ```
                pip install ipykernel
                ```

##### About Environment setup
- setup.py---> This one use to install the local package created for project 
- requirements.txt --> In the end of line, we mentioned ```-e .```   so that it  will install local package(exceute the ```setup.py``` file) along with global libraries/package mentioned in file

##### Folder structure of Medical chatbot
```
    ├── experiments
    │   ├── experiment.ipynb
    │   ├── .env
    ├── data
    │   ├── medical_book.pdf
    ├── src
    │   ├── helper.py
    │   ├── propmt.py
    │   ├── __init__.py
    ├── static
    │   ├── style.css
    ├── template
    │   ├── chat.html
    ├── .env
    ├── app.py
    ├── store_index.py
    ├── setup.py
    ├── template.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore
```

##### LLD Diagram
[](images\LLD.png)

##### Implementation Details
- .env--> add pinecone credentials and openapi credentials
        ```
        PINECONE_API_KEY ="********"
        OPENAI_API_KEY ="************"
        ```
- template.py--> create the folder using this file don't require to create the above mention folder structure manually
- data/.pdf--> provided the static medical book pdf.LLM use pdf content to get trained
- experiments/experiment.ipynb--> Jupiter file to do the experiment and create the project in single file and exceute cell by cell manually
- templates/chat.html--> Simple html file for medical chat bot
- static/style.css--> css file for the chat.html file
- src --> backend logic for medical chatbot
            
    - helper.py--> define helper method like loading the pdf file, text splitter logic , split documnets in particular chunk size and downloading the Hugging face embedding mentioned in file
    - prompt.py--> prompt temaplate with input variable and llm instruction message
    - ```__init__.py```--->created file to convert the normal folder to python package
- app.py---> logic to create the server endpoint using flask and integarted with html page
- store_index.py-->logic to store the documents vector in pinecone data base(Manually create the index using pinecone console and provide the same index in this file to load the vector)

#### Techstack Used
- Python
- LangChain
- Flask
- Openai
- Pinecone

#### Run the Project ```python app.py```


