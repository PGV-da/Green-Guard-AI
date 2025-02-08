import random
from flask import Blueprint, request, jsonify
from utils.authentication import require_login

chat_bp = Blueprint('chat', __name__)

class GardeningAssistant:
    """A simple chatbot assistant for gardening-related queries."""
    
    def __init__(self):
        self.greetings = [
            "Hi there! I'm your gardening assistant Bloom. How can I help you today?",
            "Hello! Welcome to the gardening assistant. I am Bloom. What do you need assistance with?",
            "Greetings! I'm Bloom, your gardening companion. How can I assist you today?",
            "Hey there! I'm Bloom, ready to help you with all things gardening.",
            "Hello, gardening enthusiast! I'm Bloom, here to assist you with your gardening needs."
        ]

        self.goodbyes = [
            "Goodbye! Happy gardening!",
            "See you later!",
            "Farewell! May your garden bloom beautifully.",
            "Until next time! Happy gardening!",
            "Take care! Happy gardening with Bloom!"
        ]

        self.plant_info = {
                "Rice": "Rice is a staple food in Tamil Nadu, typically grown in flooded fields called paddies. Main varieties include Samba, Ponni, and Kuruvai. Requires plenty of water and fertile soil.",
    "Wheat": "Wheat is not as commonly grown in Tamil Nadu as rice but is still important. Cultivated in the winter season (Rabi crop), requires well-drained soil and cool temperatures.",
    "Maize": "Maize is an important crop in Tamil Nadu, grown mainly in the rainy season (Kharif crop). Requires well-drained soil and is relatively drought-tolerant.",
    "Sugarcane": "Sugarcane is a major cash crop in Tamil Nadu, requires fertile soil and a tropical climate. Harvested after about 10-12 months of growth.",
    "Cotton": "Cotton is grown in Tamil Nadu for its fiber. Requires a warm climate and well-drained soil. Planted in summer and harvested in the fall.",
    "Groundnut": "Groundnut, or peanut, is grown in Tamil Nadu for its edible oil and protein-rich seeds. Requires well-drained soil and is usually planted in the summer.",
    "Millets": "Millets such as pearl millet (bajra) and finger millet (ragi) are important food crops in Tamil Nadu. Drought-tolerant and can grow in poor soil conditions.",
    "Pulses": "Pulses such as black gram, green gram, and chickpeas are grown in Tamil Nadu for their protein-rich seeds. Require well-drained soil and are usually planted in winter.",
    "Oilseeds": "Oilseeds such as sesame, groundnut, and sunflower are grown in Tamil Nadu for their oil-rich seeds. Require well-drained soil and warm temperatures.",
    "Tea": "Tea is grown in the Nilgiri Hills of Tamil Nadu, requires cool temperatures and well-drained soil. Harvested throughout the year.",
    "Coffee": "Coffee is grown in the Nilgiri Hills and other parts of Tamil Nadu. Requires a cool climate and well-drained soil. Harvested once a year."
}
        self.crops_in_tamilnadu = ["Rice", "Wheat", "Maize", "Sugarcane", "Cotton", "Groundnut", "Millets", "Pulses", "Oilseeds", "Tea", "Coffee"]

        self.modules = {
            "Disease Detection": "diseasedetection",
            "Crop Prediction": "cropprediction",
            "Fertilizer Recommendation": "fertilizerrecommendation",
            "Price Prediction": "priceprediction",
            "Commodity Prices": "commodityprices",
            "Current Weather": "currentweather",
            "Upcoming Weather": "upcomingweather",
            "News": "news",
            "Community": "community"
        }

    def greet(self):
        return random.choice(self.greetings)

    def say_goodbye(self):
        return random.choice(self.goodbyes)

    def get_crops_in_tamilnadu(self):
        return "Crops available in Tamil Nadu include: {}".format(", ".join(self.crops_in_tamilnadu))

    def suggest_modules(self):
        return "You can get help from the following modules: " + ", ".join(self.modules.keys())

    def get_module_url(self, module_name):
        return self.modules.get(module_name, None)

    def get_plant_info(self, plant):
        if plant.capitalize() in self.plant_info:
            return self.plant_info[plant.capitalize()]
        else:
            return "I'm sorry, I don't have information about that plant. Can I help you with something else?"

    def handle_user_input(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input or "hi" in user_input:
            return self.greet()
        elif "bye" in user_input or "goodbye" in user_input:
            return self.say_goodbye()
        elif "help" in user_input or "module" in user_input:
            return self.suggest_modules()
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase or ask a different question?"

assistant = GardeningAssistant()

@chat_bp.route('/chat', methods=['POST'])
@require_login
def chat():
    """Handles chatbot interactions."""
    user_input = request.json.get('message')
    response = assistant.handle_user_input(user_input)
    return jsonify({'message': response})

@chat_bp.route('/chatassistant')
@require_login
def chatassistant():
    return render_template('chat-assistant.html')