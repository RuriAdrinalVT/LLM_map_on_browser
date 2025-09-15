import json
import webbrowser
import ollama

class MapLLM:
   global coordinates_json
   coordinates_json = "test"
   address_to_find_str = "test"
   strlatitude = "0"
   strlongitude = "0"
   def decode_address(address):
        prompt = f"What are the latitude and longitude coordinates for '{address}'? Respond in a JSON format like: {{\"latitude\": float, \"longitude\": float}}"
        response = ollama.chat(
            model='mistral',
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )
        return response['message']['content']


   def STRING_PROCESS(str_response):
        coordinates_string = coordinates_json
        print("print latitude and longitude data from AI LLM OLLAMA json----->")
        substring1 = "{"
        substring2 = "}"
        index1 = coordinates_string.find(substring1)
        index2 = coordinates_string.find(substring2)
        coordinatestr = coordinates_string[index1:index2+1]
        json_data = json.loads(coordinatestr)
        latitude = json_data['latitude']
        longitude = json_data['longitude']
        print(latitude)
        print(longitude)
        strlatitude = str(latitude)
        strlongitude = str(longitude)

   def Address_to_find():
        address_to_decode = input("Adrinal->Please type what you want to find!--> ")
        return address_to_decode
   def OpenMap():
       webbrowser.open("https://www.google.com/maps/place/"+ strlatitude +","+ strlongitude)


MapLLMinstance = MapLLM
MapLLMinstance.address_to_find_str = MapLLMinstance.Address_to_find()
MapLLMinstance.STRING_PROCESS(MapLLMinstance.decode_address(MapLLMinstance.address_to_find_str))

