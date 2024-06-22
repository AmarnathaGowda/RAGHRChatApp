# RAGHRChatApp
# RAG-Based Employee HR Query Assistant

![Project Architecture](path_to_image/HRQAfinal.drawio.svg)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Architecture](#project-architecture)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
The RAG-Based Employee HR Query Assistant is designed to help employees ask questions related to company policies and receive accurate, immediate responses. This application leverages advanced machine learning models and a retrieval-augmented generation (RAG) approach to deliver precise answers based on the company’s documentation.

## Features
- **Accurate Policy Information:** Provides answers to employees' questions based on company policy documents.
- **User-friendly Interface:** Easy-to-use interface built with Streamlit.
- **Efficient Document Processing:** Uses PyPDF for handling and parsing PDF documents.
- **Scalable Infrastructure:** Deployed on AWS using EC2 and utilizes Boto3 for interaction with AWS services.

## Technologies Used
- **Python:** Core programming language.
- **LangChain:** For integrating various components and managing workflows.
- **AWS:** Cloud infrastructure provider.
  - **EC2:** For hosting the application.
  - **Boto3:** For AWS service interactions.
- **Streamlit:** For building the web application interface.
- **PyPDF:** For processing PDF documents.
- **Anthropic:** For advanced natural language processing.

## Project Architecture
The architecture of the HR Query Assistant application is illustrated in the diagram below. This showcases the interaction between various components such as the user interface, backend services, and the cloud infrastructure.

![Project Architecture](path_to_image/HRQAfinal.drawio.svg)

## Setup and Installation
To set up and run this project locally, follow these steps:

### Prerequisites
- Python 3.8 or higher
- AWS Account
- Necessary AWS IAM permissions for EC2 and other used services

### Installation Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/hr-query-assistant.git
    cd hr-query-assistant
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up AWS credentials:**
    Ensure your AWS credentials are configured. You can do this by setting up `~/.aws/credentials` or using environment variables:
    ```bash
    export AWS_ACCESS_KEY_ID='your_access_key_id'
    export AWS_SECRET_ACCESS_KEY='your_secret_access_key'
    ```

5. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

## Usage
- **Upload Documents:** Use the interface to upload company policy documents in PDF format.
- **Ask Questions:** Enter your queries related to company policies in the provided text box.
- **Receive Answers:** The application will process your query and return the relevant information based on the uploaded documents.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions or need further information, please contact:

- **Name:** Amarnatha Gowda T
- **Email:** amarnathagowda@gmail.com



