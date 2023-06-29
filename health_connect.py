import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/ussd", methods=['POST'])
def ussd():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == '':
        response = "CON Welcome to the HealthConnect Platform?\n"
        response += "1. English\n"
        response += "2. Kiswahili"

    elif text == '1':
        response = "CON Select the disease you want information about:\n"
        response += "1. Malaria\n"
        response += "2. Diabetes\n"
        response += "3. Cancer\n"
        response += "4. SickleCell\n"
        response += "5. Tuberculosis"

    elif text == '1*1':
        response = "END Common symptoms of Malaria include:\n"
        response += "- High fever\n"
        response += "- Headache\n"
        response += "- Fatigue\n"
        response += "- Muscle aches\n"
        response += "- Chills"

    elif text == '1*2':
        response = "END Treatment regimens for Malaria include:\n"
        response += "- Antimalarial medications\n"
        response += "- Rest and hydration\n"
        response += "- Fever-reducing medications\n"
        response += "- Prevention measures (e.g., bed nets, insect repellents)"

    elif text == '1*3':
        response = "END Self-care tips for Malaria include:\n"
        response += "- Get plenty of rest\n"
        response += "- Drink fluids to prevent dehydration\n"
        response += "- Take prescribed medications\n"
        response += "- Avoid mosquito bites\n"
        response += "- Seek medical attention if symptoms worsen"

    elif text == '1*4':
        response = "END Here are some hotline numbers for Malaria support:\n"
        response += "- Malaria Helpline: 123456789\n"
        response += "- National Malaria Institute: 987654321\n"
        response += "- Malaria Support Network: 567890123"

    elif text == '2':
        response = "END Chagua ugonjwa tehe: ...\n"  # Add logic to fetch account information

    elif text == '3':
        response = "CON Select the information you want about Cancer:\n"
        response += "1. Symptoms to watch out for\n"
        response += "2. Treatment regimens for cancer diagnosis\n"
        response += "3. Self-care and help groups for cancer\n"
        response += "4. Hotline Numbers for cancer support"

    elif text == '3*1':
        response = "END Common symptoms of Cancer include:\n"
        response += "- Unexplained weight loss\n"
        response += "- Persistent coughing\n"
        response += "- Abnormal bleeding\n"
        response += "- Chronic fatigue\n"
        response += "- Severe pain"

    elif text == '3*2':
        response = "END Treatment regimens for Cancer depend on the type and stage of cancer. They may include:\n"
        response += "- Surgery\n"
        response += "- Chemotherapy\n"
        response += "- Radiation therapy\n"
        response += "- Immunotherapy\n"
        response += "- Targeted therapy"

    elif text == '3*3':
        response = "END Self-care tips for Cancer patients:\n"
        response += "- Maintain a healthy lifestyle\n"
        response += "- Seek emotional support\n"
        response += "- Engage in relaxation techniques\n"
        response += "- Join support groups\n"
        response += "- Follow medical recommendations"

    elif text == '3*4':
        response = "END Here are some hotline numbers for Cancer support:\n"
        response += "- Cancer Helpline: 123456789\n"
        response += "- National Cancer Institute: 987654321\n"
        response += "- Cancer Support Network: 567890123"

    # Add elif blocks for Diabetes, SickleCell, and Tuberculosis

    else:
        response = "END Invalid choice"

    return response

if __name__ == '__main__':
    app.run(debug=True)
