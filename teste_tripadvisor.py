import requests

url = "https://tripadvisor1.p.rapidapi.com/answers/list"

querystring = {"limit":"10","question_id":"5283833"}

headers = {
    'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
    'x-rapidapi-key': "5feb988551msh3e92b7e9a2f012ep1c0544jsnc75ee9d48dc6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# funções para quem não está logado
# funções só para quem estiver logado - minhas compras