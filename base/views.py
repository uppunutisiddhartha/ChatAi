from django.shortcuts import render
import google.generativeai as genai
from django.conf import settings

def index(request):
    return render(request,"index.html")

def chat(request):
    user_input = ""
    response_text = ""

    if request.method == "POST":
        user_input = request.POST.get("user_input", "")

        try:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            model = genai.GenerativeModel("gemini-1.5-flash")
            chat = model.start_chat(history=[])
            response = chat.send_message(user_input)
            response_text = response.text
        except Exception as e:
            response_text = f"Error: {e}"

    return render(request, "chatai.html", {
        "user_input": user_input,
        "response": response_text
    })
