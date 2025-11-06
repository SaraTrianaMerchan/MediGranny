"""
MediGranny Backend - Flask API
Connects CIMA API (Spanish meds) + OpenAI
"""
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# ===== CONFIG =====
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
CIMA_BASE_URL = "https://cima.aemps.es/cima/rest"


# ===== SEARCH MEDICATION IN CIMA =====
def search_medication_in_cima(query):
    """Search medication in Spanish government database"""
    try:
        url = f"{CIMA_BASE_URL}/medicamentos"
        params = {'nombre': query.strip()}
        
        print(f"🔍 Searching CIMA for: {query}")
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data and 'resultados' in data and len(data['resultados']) > 0:
                first_med = data['resultados'][0]
                nregistro = first_med.get('nregistro')
                
                if nregistro:
                    # Get detailed info
                    detail_url = f"{CIMA_BASE_URL}/medicamento/{nregistro}"
                    detail_response = requests.get(detail_url, timeout=10)
                    
                    if detail_response.status_code == 200:
                        detail_data = detail_response.json()
                        
                        return {
                            'name': detail_data.get('nombre', 'Unknown'),
                            'active_ingredient': detail_data.get('principiosActivos', [{}])[0].get('nombre', 'N/A') if detail_data.get('principiosActivos') else 'N/A',
                            'lab': detail_data.get('labtitular', 'N/A'),
                        }
                
                # Fallback
                return {
                    'name': first_med.get('nombre', 'Unknown'),
                    'active_ingredient': 'Available',
                    'lab': 'N/A',
                }
        
        return None
        
    except Exception as e:
        print(f"❌ CIMA Error: {e}")
        return None


# ===== GENERATE RESPONSE WITH OPENAI =====
def generate_grandma_response(med_data, user_question):
    """Call OpenAI to generate warm, simple explanation"""
    try:
        system_prompt = """You are MediGranny, a warm and caring grandmother who helps people understand medications.

RULES:
- Use simple, everyday language (no medical jargon)
- Be patient and empathetic like a grandmother
- Keep responses SHORT (3-4 sentences max)
- Always end with: "Remember dear, always check with your doctor or pharmacist."
- NEVER diagnose or prescribe

Example:
Medical: "Antipyretic analgesic"
You say: "It's medicine that lowers fever and reduces pain, like headaches."
"""

        user_message = f"""Medication:
- Name: {med_data['name']}
- Active ingredient: {med_data['active_ingredient']}

User asks: {user_question}

Explain in simple, warm language."""

        headers = {
            'Authorization': f'Bearer {OPENAI_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7,
            'max_tokens': 200
        }
        
        print("🤖 Calling OpenAI...")
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            answer = result['choices'][0]['message']['content']
            print("✅ Got OpenAI response")
            return answer
        else:
            print(f"❌ OpenAI error: {response.status_code}")
            return "I'm having trouble thinking right now, dear. Please try again."
            
    except Exception as e:
        print(f"❌ OpenAI Error: {e}")
        return "I'm having trouble understanding right now, dear."


# ===== MAIN ENDPOINT =====
@app.route('/api/ask', methods=['POST'])
def ask():
    """Main endpoint: question → CIMA → OpenAI → answer"""
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({'error': 'Please ask a question'}), 400
        
        print(f"\n📝 Question: {question}")
        
        # Step 1: Search in CIMA
        med_data = search_medication_in_cima(question)
        
        if not med_data:
            return jsonify({
                'answer': "I couldn't find that medication, dear. Check the spelling?",
                'found': False
            })
        
        print(f"✅ Found: {med_data['name']}")
        
        # Step 2: Generate response
        answer = generate_grandma_response(med_data, question)
        
        # Step 3: Return
        return jsonify({
            'answer': answer,
            'medication': med_data['name'],
            'found': True,
            'disclaimer': '⚠️ This is info only. Always consult your doctor.'
        })
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'error': 'Something went wrong'}), 500


# ===== HEALTH CHECK =====
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'MediGranny is running! 👵'
    })


# ===== RUN =====
if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 MediGranny Backend Starting...")
    print("="*50)
    print(f"📍 URL: http://localhost:5000")
    print(f"🤖 OpenAI: {'✅ Set' if OPENAI_API_KEY != 'YOUR_OPENAI_KEY_HERE' else '❌ NOT SET'}")
    print("="*50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
