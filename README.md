# InsightGraph
Welcome to our project submission for the LLMs for Chemistry and Materials Science Heckatlon that took place on March 29th, 2023.

# Overview
Our project aims to create a simplified knowledge graph from article abstacts to discover concepts and relevant articles. During the hackathon, we were able to design a web application that automatically extracts entities and relationships from material-science abstracts using a pre-defined schema.. You can find our video submission here: https://twitter.com/DCirci/status/1641486022709059585?s=20.

# How to use

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install the packages
   ```sh
   pip install -r requirements.txt
   ```
3. Specify authentication details in config.py

   ```sh
   openai_api_key = "openai_api_key"
   neo4j_uri = "neo4j_uri"
   neo4j_username = "neo4j_username"
   neo4j_password = "neo4j_password"
   ```
   
   Get Neo4j credentials by first creating a user account, and then creating a free instance.
   On creation of an instance, you will be prompted to download authentication details containing uri,
   username and password.
   
  ![alt text](https://github.com/defnecirci/InsightGraph/blob/3754651d7f8163c16685656f7798e23b7d0d0029/neo4j.png)

   
5. Run 
   ```sh
   streamlit run app.py
   ```
   
6. To view and interact with the results on Neo4j Browser, you will be asked to authenticate with your credentials again (see config.py)

   
# Contributing
We are still working on developing our project and would greatly appreciate your feedback and contributions.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Contact
If you have any questions or comments, feel free to reach out to us at defne.circi@duke.edu.

Thank you for taking the time to check out our project!
