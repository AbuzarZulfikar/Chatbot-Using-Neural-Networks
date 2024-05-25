# Chatbot Using Neural Networks

Welcome to the Chatbot Using Neural Networks repository! This project implements a simple chatbot using neural networks and natural language processing techniques. The chatbot is trained on a set of intents and can respond to user queries based on the trained model's predictions.

## Requirements

- Python 3.x
- TensorFlow
- Keras
- NumPy
- NLTK (Natural Language Toolkit)
- Streamlit (for running the web application)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Chatbot-Using-Neural-Networks.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Chatbot-Using-Neural-Networks
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Download NLTK data by running the following Python script:

   ```bash
   python setup_nltk.py
   ```

## Usage

1. Prepare your intents data in JSON format and save it as `corpus.json` in the `data` directory. The JSON should have the following structure:

   ```json
   {
       "intents": [
           {
               "tag": "greeting",
               "patterns": ["Hi", "Hello", "Hey"],
               "responses": ["Hello, how can I help you?", "Hi there! What can I do for you?", "Hey, how's it going?"]
           },
           {
               "tag": "goodbye",
               "patterns": ["Bye", "Goodbye", "See you later"],
               "responses": ["Goodbye! Have a great day.", "See you later! Take care.", "Bye bye!"]
           },
           ...
       ]
   }
   ```

2. Run the main script to train and use the chatbot:

   ```bash
   streamlit run chatbot.py
   ```

3. Follow the on-screen prompts to interact with the chatbot. Type "quit" to exit the chatbot.

## Additional Files

- `chatbot.ipynb`: Jupyter Notebook containing code snippets and explanations related to the chatbot implementation.
- `chatbot_app.py`: Streamlit web application for interacting with the chatbot through a user-friendly interface.
- `training_data.pkl`: Pickled data containing words, classes, training inputs, and outputs used for training the model.
- `model.h5`: Trained model file saved in HDF5 format.

## Files and Directory Structure

- `chatbot.py`: Main script containing the chatbot implementation.
- `setup_nltk.py`: Python script to download NLTK data.
- `data/`: Directory to store `corpus.json` and other data files.
- `model/`: Directory to store the trained model (`model.h5`).
- `streamlit_app/`: Directory containing the Streamlit web application files.

## Contributing

Contributions to improve the chatbot's functionality or add new features are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
