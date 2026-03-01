Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import openai
... client = openai.OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
... 
... def get_recommendation(user_query):
...     with open("wardrobe.txt", "r") as f:
...         my_wardrobe = f.read()
... 
...     system_prompt = f"""
...     You are an AMD-powered Private AI Shopping Assistant. 
...     You have access to the user's LOCAL wardrobe data below:
...     {my_wardrobe}
...     Only suggest items that match their current style or fill a gap. 
...     Stay private and professional.
...     """
... 
...     response = client.chat.completions.create(
...         model="local-model", 
...         messages=[
...             {"role": "system", "content": system_prompt},
...             {"role": "user", "content": user_query}
...         ],
...         temperature=0.7,
...     )
...     return response.choices[0].message.content
... 
... print("--- AMD Private Eye Active ---")
... query = "I have a beach wedding this weekend. What should I wear from my wardrobe, and what one thing should I buy?"
