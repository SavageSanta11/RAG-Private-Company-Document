
<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">RAG-PRIVATE-COMPANY-DOCUMENT</h1>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/SavageSanta11/RAG-Private-Company-Document?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/SavageSanta11/RAG-Private-Company-Document?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/SavageSanta11/RAG-Private-Company-Document?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/SavageSanta11/RAG-Private-Company-Document?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/Babel-F9DC3E.svg?style=flat&logo=Babel&logoColor=black" alt="Babel">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<br>
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/Ray-028CF0.svg?style=flat&logo=Ray&logoColor=white" alt="Ray">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running RAG-Private-Company-Document](#-running-RAG-Private-Company-Document)
> - [ Project Roadmap](#-project-roadmap)

---

##  Overview

Coming soon

---

##  Features

Coming Soon

---

##  Modules

<details closed><summary>rag</summary>

| File                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [main.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/main.py)                   | The codebase consists of two APIs: Cache API and Conversation API, each designed with Docker and organized into models, schemas, and routes. Cache API manages database queries storage, enhancing speed and responsiveness, while Conversation API handles user interaction data, emphasizing user-focused features. An Evaluation section exists for performance analysis.                                                                                                            |
| [build.yaml](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/build.yaml)             | The build.yaml file, located in the rag directory of the RAG-Private-Company-Document repository, orchestrates the deployment of the web application. It manages the allocation of two replicas of the predictor container, each running the latest version of the rag image and exposes port 8080. Basically, it configures the Kubernetes deployment for the application.                                                                                                             |
| [Dockerfile](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/Dockerfile)             | This Dockerfile configures the environment for the rag component of the architecture, which appears responsible for some core operations of the repository. It installs dependencies specified in the requirements file and sets uvicorn server to run the main application, exposing it on port 8080.                                                                                                                                                                                  |
| [data.json](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/data.json)               | The data.json in rag folder of the repository serves as a temporary data holding or a loader file that provides communication between different systems or different parts of the same system. With no data currently, it plays the role of an empty shell to hold necessary data when required in the system operation.                                                                                                                                                                |
| [notes](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/notes)                       | The provided code snippet appears to essentially construct, run, and deploy a docker image for the rag component within a multi-component application. This ensures the component's consistent operation and seamless integration with the overarching application architecture. The rag component seems to be central in the system, interacting with other APIs and handling complex tasks, with its own cache and modeling substructures.                                            |
| [requirements.txt](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/requirements.txt) | This requirements.txt file, located in the rag directory of the RAG-Private-Company-Document repository, specifies the packages that are necessary for that directory's operations. These include FastAPI for building APIs, Pinecone-client for vector-based similarity search, Langchain for language processing, Sentence-Transformers for creating sentence embeddings, and Uvicorn for running the server.                                                                         |
| [test.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/test.py)                   | This repository is structured into two distinct APIs: the Cache API and the Conversation API. The Cache API is responsible for managing cache-related operations, including maintaining cache data models and providing routes to handle requests. The Conversation API, meanwhile, focuses on handling user interactions, managing user models, and providing user-related API routes. Both APIs are individually containerized with Docker and share a common database configuration. |

</details>

<details closed><summary>rag.cache</summary>

| File                                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [cache_db.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/cache/cache_db.py)                   | This repository, RAG-Private-Company-Document, has a microservice architecture with several APIs, including a cache API and a conversation API, each with its respective Docker configurations, routes, models, and schemas. It also contains an evaluation module, handling datasets and model performance analysis. The code is designed to enable document handling and storage, user conversation management, data analysis, and inter-service communication.                               |
| [cache_vectorstore.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/cache/cache_vectorstore.py) | This repository organizes the backend services for a private firm's document management system. It includes two microservices, cache_api and conversation_api, for handling cached data and user interactions respectively. Another directory, evaluation, is involved in assessing the system's performance using different datasets. Docker containerization is employed for consistent deployment.                                                                                           |
| [db_interact.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/cache/db_interact.py)             | This codebase contains two interconnected APIs: cache_api and conversation_api. The cache_api facilitates data caching, management, and retrieval, improving performance and response times. On the other hand, conversation_api manages user related operations, including user data handling, request routing and database operations. Their unified architecture supports seamless inter-service communication, optimizing the functionality of the RAG-Private-Company-Document repository. |

</details>

<details closed><summary>rag.conv_history</summary>

| File                                                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                             |
| [db_interact.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/conv_history/db_interact.py) | The code in rag/conv_history/db_interact.py interacts with a conversation database identified by user's email. It maintains conversation history by sending user queries and corresponding system responses to the database and retrieves the latest conversation history. This plays a significant role in preserving contextual accuracy in ongoing user-system interactions across sessions. |

</details>

<details closed><summary>rag.models</summary>

| File                                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [api.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/models/api.py)       | The api.py in the rag/models directory defines data models for transmitting information to and from the RAG API. These models detail the structure of requests for asking questions, getting files, updating files and fetching frequently asked questions. They also outline responses for successful file updates and question answering, including any sources utilized. As such, they play a crucial role in ensuring data consistency and validity when interacting with the RAG API. |
| [models.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/models/models.py) | This code from the RAG repository, specifically the rag/models/models.py file, defines abstract base models for essential operational components: Document storage and manipulation, application configurations, as well as a VectorStore and Language Learning Model (LLM). These models guide operations for document management, vector storage, and conversational interactions.                                                                                                       |

</details>

<details closed><summary>rag.llm</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [llm.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/llm/llm.py) | This repository builds a system for a private company to manage internal documents. It has two main components: the Cache API, and the Conversation API. The Cache API is responsible for temporary storage, retrieval, and management of frequently accessed data. The Conversation API takes care of interactions with the user data model. The repository also contains an evaluation module for testing and quality control. |

</details>

<details closed><summary>rag.vectorstore</summary>

| File                                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                        |
| [pinecone_vectorstore.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/rag/vectorstore/pinecone_vectorstore.py) | This codebase contains two main APIs-Cache API and Conversation API-and an Evaluation module. The APIs are used to manage and process private company documents, while the Evaluation module is for validating the performance. Cache API deals with caching aspects, whereas Conversation API handles user interactions. The evaluation sector examines response accuracy and efficiency. |

</details>

<details closed><summary>llm-api</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                               |
| [build.yaml](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/llm-api/build.yaml) | This code snippet outlines the architecture of a Repository, which contains APIs for managing documents and conversations within a private company. The `cache_api` uses a model, schema and route to work with cached data for optimal performance, while the `conversation_api` emphasizes on user interaction. |

</details>

<details closed><summary>llm-api.mistral-7b</summary>

| File                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dockerfile](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/llm-api/mistral-7b/Dockerfile)   | The provided Dockerfile in the /llm-api/mistral-7b directory is responsible for creating a Debian-based GPU-capable container environment for the Long-Length Model (llm) API. It validates the Python version and upgrades pip within the container, preparing a suitable setup for the model's execution in the parent repository's microservice architecture.                                                                          |
| [config.yaml](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/llm-api/mistral-7b/config.yaml) | This repository structures two API services for a private company's document management system: a cache API and a Conversation API. The cache API regulates the document cache, helping to enhance retrieval performance. The Conversation API manages user-related operations, likely central to authentication and preference setting. Both have Docker support and similar db configurations, indicating isolated microservice design. |

</details>

<details closed><summary>llm-api.mistral-7b.model</summary>

| File                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [model.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/llm-api/mistral-7b/model/model.py) | The repository is structured around maintaining the private company document records in a cache and managing user conversations. It contains two microservices: Cache API and Conversation API. The Cache API manages the documents in cache, handling storage, retrieval, among other operations, while the Conversation API manages user's conversation data. Each allows interaction with a dedicated database and contains models, routes, and schemas for configuring and managing the data accordingly. Supportive data for evaluation is also present. |

</details>

<details closed><summary>conversation_api</summary>

| File                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                              |
| [index.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/conversation_api/index.py)                 | The provided code snippet is from a file named index.py in the conversation_api directory. This part of the architecture initiates a FastAPI application and employs uvicorn to serve the application on a local server. It mainly pulls together user-related routes and starts the application, primarily facilitating user conversations within the system.                                                   |
| [build.yaml](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/conversation_api/build.yaml)             | The `build.yaml` within the `conversation_api` directory is a Kubernetes script that orchestrates deployment of the conversation application programming interface (API). It defines the deployment setup, particularly that two replicas of the web container are run, identifying them with labels. Notably, it's configured to pull and deploy image savagesanta11/conversation_api from a Docker repository. |
| [Dockerfile](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/conversation_api/Dockerfile)             | The Dockerfile, located in the `conversation_api` directory, plays a primary role in creating a Docker image for the Conversation API part of the application. It bundles the API, specifically written in Python, and its dependencies into a container. This containerized application can then be reliably executed in different environments.                                                                |
| [requirements.txt](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/conversation_api/requirements.txt) | The `conversation_api/requirements.txt` file outlines the precise library dependencies necessary for the `conversation_api` part of this project. This API manages user conversation data, and the required packages enable tasks like environment management, HTTP handling, web sockets usage, type checking, server hosting, and interfaction with MongoDB database.                                          |

</details>

<details closed><summary>conversation_api.schemas</summary>

| File                                                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                       |
| [user.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/conversation_api/schemas/user.py) | This repository hosts code for two separate microservices, namely cache_api and conversation_api. The cache_api holds code for managing in-memory data caching, while the conversation_api manages user-related functionalities. They both adhere to a shared structure, containing Docker support, routing, database configuration, and defined data models and schemas. |

</details>

<details closed><summary>conversation_api.models</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                          |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                              |
| [user.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/conversation_api/models/user.py) | The user.py in conversation_api/models serves as the data model for user details within the conversational interface. It chiefly manages the storage and structure of user-related data, involving the user's email and associated messages in the architecture. |

</details>

<details closed><summary>conversation_api.routes</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [user.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/conversation_api/routes/user.py) | The code snippet is part of the RAG private company document repository, designed to store, manage, and retrieve sensitive company data. It is divided into two main APIs: cache_api and conversation_api, which handle caching and conversation functionalities respectively. Besides, there's an evaluation module for performance assessment. Each API includes constructs for dockerizing the application, database configurations, and data models. |

</details>

<details closed><summary>conversation_api.config</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                      |
| [db.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/conversation_api/config/db.py) | This script is a crucial part of the `conversation_api` module in the RAG-Private-Company-Document repository. Its primary function is to establish a secure connection to a MongoDB database, verify the connection, and define a specific collection within capstonedb. This connection provides the groundwork for any data-oriented operations within the conversation interface of the application. |

</details>

<details closed><summary>evaluation</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                        |
| [repeat.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/repeat.py)               | This codebase maintains the infrastructure for a private company's document repository, segregated into two APIs: cache and conversation. The cache API ensures quick data access while the conversation API manages user interactions. Other components assist with configuration, schema definitions, and data evaluation methods.       |
| [data.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/data.py)                   | The `evaluation/data.py` file is part of the evaluation module in the repository, responsible for generating embeddings for evaluation data using specified models. It handles the initialization of the HuggingFaceEmbedding model with defined model names and batch size for embedding operations.                                      |
| [requirements.txt](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/requirements.txt) | This snippet represents a cache_api module in the RAG-Private-Company-Document repository. Its primary role is to handle caching for the system, improving performance by preventing redundant data operations. It creates Docker dependencies, manages cache database configurations, and sets out cache routes for increased efficiency. |

</details>

<details closed><summary>evaluation.retrieval</summary>

| File                                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [eval.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/retrieval/eval.py)   | This repository is primarily structured into two APIs: Cache API and Conversation API. The Cache API handles the storage and retrieval of company data into a cache while the Conversation API manages user-related operations, ensuring seamless communication within the repository. In addition, there's an evaluation section for data analysis and performance metrics.                                                                                                         |
| [utils.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/retrieval/utils.py) | This repository houses the RAG Private Company Document application, organized into separate logical components for caching and managing conversations. The cache_api section maintains caching services, and the conversation_api module handles conversation data & user interactions. Both are Dockerized and contain configurations, models, routes, and schemas related to their specific functionality. An evaluation module is also present for data analysis and evaluation. |

</details>

<details closed><summary>evaluation.datasets</summary>

| File                                                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [responses_iter2_page.json](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/datasets/responses_iter2_page.json)         | The repository consists of separate components for caching and conversation APIs, and a module for evaluation. The cache API handles storing and retrieving data efficiently, while the conversation API manages user-related operations. The evaluation module performs analysis and assessment of various iterations of responses.                                                                                                |
| [golden_sources.json](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/datasets/golden_sources.json)                     | This repository contains the architecture of a private company's document management system. It consists of two distinct services namely, `cache_api` and `conversation_api`. The `cache_api` handles caching of documents, while `conversation_api` manages user interactions. Both services utilize Docker for deployment and have a standardized structure with database configuration, models, routes and schemas.              |
| [responses_iter1_para.json](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/datasets/responses_iter1_para.json)         | The codebase constitutes two main APIs: Cache and Conversation, handling caching and user interaction aspects, respectively. It's structured for containerized deployment using Docker and supports a relational database for storing data. The evaluation directory holds datasets for assessing the system's performance.                                                                                                         |
| [responses_iter3.json](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/datasets/responses_iter3.json)                   | This repository structures the backbone of a private company’s document management system, facilitating diverse functionalities like caching, user conversation management and system evaluations. The cache_api and conversation_api modules manage document caching and user interactions, respectively. The evaluation module assesses system performance based on different iterations.                                         |
| [questions_human_response.json](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/datasets/questions_human_response.json) | This repository hosts code for a private company's document management system. It consists of two main sections: cache_api and conversation_api, responsible for managing cached data and user conversations respectively. The supporting evaluation folder contains resources for assessing system performance. This architecture is designed to ensure smooth operation, data storage, retrieval and efficient system evaluation. |

</details>

<details closed><summary>evaluation.generation</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [main.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/generation/main.py)   | The `main.py` script in the `evaluation/generation` folder of the repository plays a principle role in evaluating the conversation predictions from the document retrieval architecture. Specifically, it loads JSON-formatted responses, separates them into algorithmic and human responses, and subsequently utilizes these to generate the evaluation metrics summary. The information provided by these metrics is pivotal to assessing system reliability, accuracy and understanding pert-iteration improvements. |
| [eval.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/generation/eval.py)   | This repository comprises two API modules: cache_api and conversation_api, for handling cached data and user interactions respectively. It also includes an evaluation component for assessing data performance, including various sets of response data files. The whole architecture is dockerized, emphasizing containerization and easy deployment.                                                                                                                                                                  |
| [utils.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/evaluation/generation/utils.py) | This script in evaluation/generation/utils.py serves to load and print the first five entries of a JSON dataset named response.json, which is likely used for evaluating generated responses within the larger RAG-Private-Company-Document repository. This aids in understanding generated data behavior and performance.                                                                                                                                                                                              |

</details>

<details closed><summary>cache_api</summary>

| File                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [index.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/cache_api/index.py)                 | This code is the primary entry point for the Cache API, part of the RAG-Private-Company-Document repository. The API, leveraging FastAPI and Uvicorn, enables request routing for caching services, an essential feature in the overall repository's architecture. The cache operations play a key role in the repository's performance optimization strategy.                                                                                        |
| [build.yaml](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/cache_api/build.yaml)             | The `build.yaml` in the `cache_api` directory is a Kubernetes deployment file. Its key role is to manage the deployment and scaling of the Cache API service, controlling how it should run within the system's architecture. It specifies the use of 2 replicas, thus ensuring high availability, and utilizes a Docker image of the API for deployment.                                                                                             |
| [Dockerfile](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/cache_api/Dockerfile)             | As part of the RAG-Private-Company-Document repository, the cache_api/Dockerfile primarily manages the creation of a Docker container for the cache_api service. It's responsible for setting up a Python environment, installing the necessary dependencies, and launching the application on port 8080. It ultimately allows the cache_api service to function alongside other microservices, providing caching capabilities to the broader system. |
| [notes](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/cache_api/notes)                       | The cache_api/notes file in the RAG-Private-Company-Document repository comprises a set of Docker commands to build, run, and deploy the Cache API application. It's a guide for developers to automate software deployment, which is crucial for streamlining API accesses within the system architecture.                                                                                                                                           |
| [requirements.txt](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/cache_api/requirements.txt) | HTTP error 429 for prompt `cache_api/requirements.txt`                                                                                                                                                                                                                                                                                                                                                                                                |

</details>

<details closed><summary>cache_api.schemas</summary>

| File                                                                                                             | Summary                                                |
| ---                                                                                                              | ---                                                    |
| [cache.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/cache_api/schemas/cache.py) | HTTP error 429 for prompt `cache_api/schemas/cache.py` |

</details>

<details closed><summary>cache_api.models</summary>

| File                                                                                                            | Summary                                               |
| ---                                                                                                             | ---                                                   |
| [cache.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/cache_api/models/cache.py) | HTTP error 429 for prompt `cache_api/models/cache.py` |

</details>

<details closed><summary>cache_api.routes</summary>

| File                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [utils.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/cache_api/routes/utils.py) | HTTP error 429 for prompt `cache_api/routes/utils.py`                                                                                                                                                                                                                                                                                                                                                                                                          |
| [cache.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/cache_api/routes/cache.py) | This codebase organizes a private company's internal communication and document handling. It comprises two main applications: a Cache API handling data persistence and retrieval, and a Conversation API enabling user engagement and conversation. Supplementary evaluation tools are available for data analysis and performance tracking. Each API includes its Docker setup, model definitions, route handlers, and schemas for structured data handling. |

</details>

<details closed><summary>cache_api.config</summary>

| File                                                                                                      | Summary                                            |
| ---                                                                                                       | ---                                                |
| [db.py](https://github.com/SavageSanta11/RAG-Private-Company-Document/blob/master/cache_api/config/db.py) | HTTP error 429 for prompt `cache_api/config/db.py` |

</details>

---

##  Getting Started

###  Installation

1. Clone the RAG-Private-Company-Document repository:

```sh
git clone https://github.com/SavageSanta11/RAG-Private-Company-Document
```

2. Change to the project directory:

```sh
cd RAG-Private-Company-Document
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running RAG-Private-Company-Document

Use the following command to run RAG-Private-Company-Document:

```sh
python main.py
```
---
##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---
