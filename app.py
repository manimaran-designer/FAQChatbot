from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import json
import os

app = Flask(__name__)
CORS(app)

# OpenRouter API Configuration
API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# FAQ Context - All Q&A pairs for SBI General Insurance Health Card
FAQ_CONTEXT = """You are a helpful FAQ assistant for SBI General Insurance Health Card services. Answer questions based on the following FAQ information:

Q.1 What do you mean by a health card?
A health card is provided with your insurance policy, which you can use at network hospitals to avail the benefit of cashless treatments.

Q.2 What do I do if my card is lost?
In case of loss or theft of card, contact our toll-free helpline number 1800 210 3366 / 1800 210 6366 or e-mail us at sbig.health@sbigeneral.in

Q.3 What do you mean by Network/ Non-Network Hospitalization?
A Hospital, which has an agreement with us for providing Cashless treatment, is referred to as a 'Network Hospital'. Cashless facility is provided ONLY at the network hospitals. Non-network hospitals are those with whom we do not have any agreement and any policyholder seeking treatment in these hospitals will have to pay for the treatment and later claim as per reimbursement procedure.

Q.4 What is the procedure for applying for cashless health insurance?
At SBI General Insurance, the process to apply for cashless treatment is simple. Listed below are the steps to avail the benefit of cashless health insurance:
1. Intimate the insurer at the earliest.
2. Visit the network hospital where the treatment is to be taken.
3. The third part administrator desk of the network hospital will connect with the insurance company for cashless treatment.
With us you do not have to worry, the hospital will verify the details and send the duly filled pre-authorization form. We verify all the details with the policy benefits. We intimate our decision within a day or so. Once the cashless claim is approved, a first response is sent to the healthcare provider within 60 minutes. The treatment expenses at the network hospital will be settled swiftly.

Q.5 How long does it take to receive a response for pre-authorization approval and final approval in a cashless claim?
You can expect to receive a response for pre-authorization approval and final approval within 120 minutes for a cashless claim.

Q.6 What is the current status of my cashless claim?
You will receive status updates at every process step/interval via email/SMS. The updates can also be checked on the mobile app. Alternatively, the toll-free number - 1800 210 3366 / 1800 210 6366 - can be dialled or e-mail us at sbig.health@sbigeneral.in where an update on the claim status will be provided by our Executive.

Q.7 Where can I see the status of my reimbursement claim?
To check your claim status: Mail us at sbig.health@sbigeneral.in or Call us on 1800 210 3366 / 1800 210 6366. You can also check claim status on our mobile app.

Q.8 What is pre and post hospitalization?
Pre-hospitalization expenses are the medical costs you pay before going to the hospital for the same illness. Post-hospitalization expenses are the medical costs you pay after leaving the hospital for the same illness.

Q.9 What are the reasons for the deduction in reimbursement claim?
Deductions in reimbursement claims can occur due to several reasons:
Non-medical expenses – As per IRDA regulations. Other deductions vary depending on the specific case.

Q.10 Where can I find the query letter and settlement letter?
In the Reimbursement process, once we initiate a query, we ensure prompt communication by sending a query letter to the customer via email. Upon resolving the query, we send a settlement letter detailing the outcome to the customer through the same email channel. For additional assistance, please contact us through our Toll-Free number at 1800 210 3366 / 1800 210 6366 or via email at sbig.health@sbigeneral.in

Q.11 Within what timeframe am I required to submit a reimbursement claim?
Reimbursement claims should be submitted within 30 days after discharge from the hospital.

Instructions:
- Answer questions clearly and concisely based on the FAQ information above
- If a question is related to the FAQ topics, provide the relevant information
- Be friendly and professional
- If asked about something not in the FAQ, politely inform the user and suggest contacting customer service
- Always provide contact information when relevant: 1800 210 3366 / 1800 210 6366 or sbig.health@sbigeneral.in
"""

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Prepare the request to OpenRouter API
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json',
            'HTTP-Referer': 'http://localhost:5000',
            'X-Title': 'SBI Health Card FAQ Chatbot'
        }
        
        payload = {
            'model': 'qwen/qwen-2-7b-instruct:free',
            'messages': [
                {
                    'role': 'system',
                    'content': FAQ_CONTEXT
                },
                {
                    'role': 'user',
                    'content': user_message
                }
            ],
            'temperature': 0.7,
            'max_tokens': 500
        }
        
        # Make request to OpenRouter API
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        bot_message = result['choices'][0]['message']['content']
        
        return jsonify({
            'response': bot_message,
            'status': 'success'
        })
        
    except requests.exceptions.RequestException as e:
        print(f"API Error: {str(e)}")
        return jsonify({
            'error': 'Failed to get response from AI service',
            'details': str(e)
        }), 500
    except Exception as e:
        print(f"Server Error: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'details': str(e)
        }), 500

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'FAQ Chatbot API'})

if __name__ == '__main__':
    print("🚀 Starting FAQ Chatbot Server...")
    print("📍 Server running at: http://localhost:5000")
    print("💬 Ready to answer SBI Health Card questions!")
    app.run(debug=True, port=5000)
