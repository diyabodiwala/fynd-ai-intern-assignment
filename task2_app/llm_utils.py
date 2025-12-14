import json

def call_llm(review, rating):
    # Simulated LLM (replace with API later)
    if rating <= 2:
        return {
            "user_response": "We’re sorry to hear that you had a negative experience. Could you please share more details?",
            "summary": f"The user gave a {rating}-star rating with negative feedback.",
            "recommended_action": "Follow up with the user to resolve the issue."
        }
    else:
        return {
            "user_response": "Thank you for your feedback! We're glad you had a good experience.",
            "summary": f"The user gave a {rating}-star rating with positive feedback.",
            "recommended_action": "No action needed."
        }
