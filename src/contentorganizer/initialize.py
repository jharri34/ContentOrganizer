from src.contentorganizer.output_filter import filter_specific_output  # Import the context manager
from nexa.gguf import NexaVLMInference, NexaTextInference  # Import model classes

# Initialize models
image_inference = None
text_inference = None

def ensure_nltk_data():
    """Ensure that NLTK data is downloaded efficiently and quietly."""
    import nltk
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)

def initialize_models():
    """Initialize the models if they haven't been initialized yet."""
    global image_inference
    if image_inference is None:
        # Initialize the models
        model_path = "llava-v1.6-vicuna-7b:q4_0"
        model_path_text = "Llama3.2-3B-Instruct:q3_K_M"
    

        # Use the filter_specific_output context manager
        with filter_specific_output():
            # Initialize the image inference model
            image_inference = NexaVLMInference(
                model_path=model_path,
                local_path=None,
                stop_words=[],
                temperature=0.3,
                max_new_tokens=3000,
                top_k=3,
                top_p=0.2,
                profiling=False
                # add n_ctx if out of context window usage: n_ctx=2048
            )
            # Initialize the text inference model
            text_inference = NexaTextInference(
                model_path=model_path_text,
                local_path=None,
                stop_words=[],
                temperature=0.5,
                max_new_tokens=3000,  # Adjust as needed
                top_k=3,
                top_p=0.3,
                profiling=False
                # add n_ctx if out of context window usage: n_ctx=2048

            )

        
    print("**----------------------------------------------**")
    print("**                                              **")
    print("**       Image inference model initialized      **")
    print("**       Text inference model initialized       **")
    print("**                                              **")
    print("**----------------------------------------------**")