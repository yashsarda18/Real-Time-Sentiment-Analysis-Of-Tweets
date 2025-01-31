# Real-Time-Sentiment-Analysis-Of-Tweets

## Project Description

The Real-Time Twitter Sentiment Analysis project aims to analyze sentiments expressed on Twitter regarding various topics in real time. By leveraging the Twitter API, this application collects tweets based on specified keywords, processes the text data, and predicts sentiment using a machine learning model. The results are visualized in a real-time dashboard, providing insights into public sentiment trends.

### Key Features
- **Real-Time Data Collection**: Continuously collects tweets based on user-defined topics.
- **Sentiment Analysis**: Uses advanced NLP techniques to classify tweets as positive, negative, or neutral.
- **Dashboard Visualization**: Displays sentiment trends and statistics in a user-friendly dashboard.
- **API Integration**: Provides an API endpoint for real-time predictions.

## Tech Stack
- **Programming Languages**: Python
- **Libraries/Frameworks**:
  - Data Collection: Tweepy (Twitter API)
  - Data Preprocessing: NLTK, TextBlob
  - Machine Learning: Hugging Face Transformers
  - API Development: FastAPI
  - Containerization: Docker
  - Visualization: Streamlit

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)

### Clone the Repository
```bash
git clone https://github.com/yashsarda18/Real-Time-Sentiment-Analysis-Of-Tweets.git
cd Real-Time-Sentiment-Analysis-Of-Tweets
```
### Set Up Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv venv # Create a virtual environment named 'venv'
source venv/bin/activate # Activate on macOS/Linux
.\venv\Scripts\activate # Activate on Windows
```

### Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### Configuration
1. **Twitter API Credentials**: Obtain your Twitter API credentials by creating a Twitter Developer account and setting up an application. Update the credentials in your code where indicated (in `main.py` and `twitter_data.py`).

### Running the Application

#### Start the Data Collection and Sentiment Analysis
Run the main application script to start collecting tweets and analyzing sentiment:
```bash
python main.py
```

#### Start the FastAPI Server for Predictions (Optional)
If you want to run the API separately:
```bash
uvicorn model.api:app --host 0.0.0.0 --port 8000 --reload
```

#### Start the Dashboard (Optional)
To run the Streamlit dashboard:
```bash
streamlit run dashboard/dashboard.py
```

## Usage Instructions

1. **Data Collection**: The application will collect tweets every second based on the specified topic in `main.py`.
2. **Sentiment Prediction**: Each collected tweet will be processed and analyzed for sentiment.
3. **Dashboard Visualization**: Access the Streamlit dashboard to view real-time sentiment trends.

## Acknowledgments

- Thanks to [Tweepy](https://www.tweepy.org/) for providing an easy way to access the Twitter API.
- Thanks to [Hugging Face](https://huggingface.co/) for their powerful NLP models.
