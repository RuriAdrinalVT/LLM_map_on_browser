import ollama
import webbrowser
import json

def decode_address(address):
        prompt = f"What are the latitude and longitude coordinates for '{address}'? Respond in a JSON format like: {{\"latitude\": float, \"longitude\": float}}"
        response = ollama.chat(
            model='mistral',
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )
        return response['message']['content']

address_to_decode = input("Adrinal->Please type what you want to find!--> ")
coordinates_json = decode_address(address_to_decode)
coordinates_string = coordinates_json
print("print latitude and longitude data from AI LLM OLLAMA json----->")
substring1 = "{"
substring2 = "}"
index1 = coordinates_string.find(substring1)
index2 = coordinates_string.find(substring2)
coordinatestr = coordinates_string[index1:index2+1]
json_data = json.loads(coordinatestr)
print(type(json_data))
latitude = json_data['latitude']
longitude = json_data['longitude']
print(latitude)
print(longitude)
strlatitude = str(latitude)
strlongitude = str(longitude)
webbrowser.open("https://www.google.com/maps/place/"+ strlatitude +","+ strlongitude)
