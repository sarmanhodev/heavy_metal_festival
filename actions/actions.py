# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
#

#
class ActionSayName(Action):
#
    def name(self) -> Text:
        return "action_say_name"
#
    def run(self, dispatcher: CollectingDispatcher,
       tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global nome
        nome = tracker.get_slot("nome")

        if not nome:
            dispatcher.utter_message(text="ERROR")
        else:
            dispatcher.utter_message(text=f"Olá, {nome.capitalize()}!")            

        return []    
    


class ActionOptions(Action):
#
    def name(self) -> Text:
        return "action_options"
#
    def run(self, dispatcher: CollectingDispatcher,
       tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        option = tracker.get_slot("option")
        estado_origem = tracker.get_slot("estado").capitalize()
               

        if str(option) == "Opção 1" or str(option) == "opção 1" or int(option) == 1:
            dispatcher.utter_message(text="O Heavy Metal Festival 2023 acontecerá em quatro dias, com as seguintes atrações: \n\
                                        02 de Setembro de 2023: Iron Maiden + Metallica\n\
                                        03 de Setembro de 2023: Guns N Roses + Kiss\n\
                                        09 de Setembro de 2023: Bullet For My Valentine + Avenged Sevenfold\n\
                                        10 de Setembro de 2023: Slipknot + Ghost")
            
        elif str(option) == "Opção 2" or str(option) == "opção 2" or int(option) == 2:
            dispatcher.utter_message(text="O desconto sobre o valor do ingresso será dado de acordo com a distância de deslocamento do comprador até o local do evento\n")
            with open ("dados.json") as dados:
                
                dados_json = json.load(dados)
                filtered_list = [dictionary for dictionary in dados_json if dictionary['cidade'] == str(estado_origem)]

                x = json.dumps(filtered_list)
                new_list = json.loads(x)
                for i in new_list:
                    print(f'A distância da cidade {estado_origem.title()} até o Rio de Janeiro é '+str(i['distancia'])+'Km')
                    dispatcher.utter_message(text=f'A distância da cidade {estado_origem.title()} até o Rio de Janeiro é '+str(i['distancia'])+'Km')
                    dispatcher.utter_message(text='Aguarde um instante, enquanto calculamos o valor do desconto obtido...')
                    valor_ingresso = 700
                    valor_desconto = int(i['distancia'])/20
                    x = valor_desconto*100
                    aux = x/700
                    valor_total = 700*(aux/100)
                    dispatcher.utter_message(text=f'O(a) senhor(a) obteve R$ {round(valor_total,2)} de desconto.')
                    novo_valor = valor_ingresso-valor_total

                    dispatcher.utter_message(text=f'O valor a ser pago, com o desconto da distância da cidade {estado_origem.title()} para o Rio de Janeiro é de R$ {round(novo_valor,2)}')

        elif str(option) == "Opção 3" or str(option) == "opção 3" or int(option) == 3:
            dispatcher.utter_message(text="O Heavy Metal Festival acontecerá na Cidade do Rio de Janeiro, nos dias 02,03, 09 e 10 de Setembro de 2023.\n\
                                     Os portões serão abertos à partir das 12h (horário de Brasília)")
                    

        
        return []



  

