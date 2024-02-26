import json
import os

directory = r"C:/Users/Renan/OneDrive/Área de Trabalho/TCC2/Bot/actions"
file_name = "output.json"
file_path = os.path.join(directory, file_name)

with open(file_path, 'r', encoding='utf-8') as f:
    data = f.read()

data = json.loads(data)

# Extrai os dados relevantes
intents = []
responses = []
intent_counts = {}
for obj in data:
    for section in obj['sections']:
        intent_name = section['title']
        if intent_name in intent_counts:
            intent_counts[intent_name] += 1
            intent_name = f"{intent_name}_{intent_counts[intent_name]}"
        else:
            intent_counts[intent_name] = 1
        intents.append(intent_name)
        responses.append(section['content'])


# Cria o arquivo de intents
with open('data/intents.yml', 'w', encoding='utf-8') as f:
    f.write('intents:\n')  # adiciona a linha "intents:"
    for intent in intents:
        intent_name = intent.replace(" ", "_") # substitui espaços por underline
        f.write(f'  - {intent_name}\n')  # adiciona os intents com a formatação desejada


with open('data/responses.yml', 'w', encoding='utf-8') as f:
    for i, intent in enumerate(intents):
        intent_name = intent.replace(" ", "_") # substitui espaços por underline
        response = """{}""".format(responses[i].replace('"', '\\"'))  # adiciona aspas triplas e substitui aspas duplas por suas sequências de escape correspondentes
        response = response.replace('\n', '\\n')  # adiciona barra invertida antes de cada quebra de linha
        f.write(f'utter_{intent_name}:\n')
        f.write(f'  - text: "{response}"\n\n')

with open('domain.yml', 'w', encoding='utf-8') as f:
    f.write('version: "3.1"\n\n')  # adiciona a linha:
    f.write('intents:\n')  # adiciona a linha "intents:"

    f.write('  - mood_so\n')    # intents padroes do rasa
    f.write('  - cheer_up\n')
    f.write('  - greet\n')
    f.write('  - goodbye\n')
    f.write('  - affirm\n')
    f.write('  - deny\n')
    f.write('  - mood_greet\n')
    f.write('  - mood_unhappy\n')
    f.write('  - bot_challenge\n')
    f.write('  - creator\n')
    f.write('  - what_i_do\n')


    for intent in intents:
        intent_name = intent.replace(" ", "_") # substitui espaços por underline
        f.write(f'  - {intent_name}\n')  # adiciona os intents com a formatação desejada

    f.write('\nresponses:\n')  # adiciona a linha :

    f.write('  utter_mood_so:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_cheer_up:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_greet:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_goodbye:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_affirm:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_deny:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_mood_greet:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_happy:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_mood_unhappy:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_iamabot:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_creator:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_what_i_do:\n')
    f.write('    - text: "ok"\n')

    f.write('  utter_did_that_help:\n')
    f.write('    - text: "ok"\n')



    for i, intent in enumerate(intents):
        intent_name = intent.replace(" ", "_") # substitui espaços por underline
        response = """{}""".format(responses[i].replace('"', '\\"'))  # adiciona aspas triplas e substitui aspas duplas por suas sequências de escape correspondentes
        response = response.replace('\n', '\\n')  # adiciona barra invertida antes de cada quebra de linha
        f.write(f'  utter_{intent_name}:\n')
        f.write(f'    - text: "{response}"\n\n')
    
    f.write('session_config: \n')
    f.write('  session_expiration_time: 60\n')
    f.write('  carry_over_slots_to_new_session: true')

with open('data/rules.yml', 'w', encoding='utf-8') as f:

    f.write('version: "3.1"\n\nrules:\n\n')
    f.write('- rule: Say goodbye anytime the user says goodbye\n')
    f.write('  steps:\n')
    f.write('  - intent: goodbye\n')
    f.write('  - action: utter_goodbye\n')
    f.write('\n- rule: Say "I am a bot" anytime the user challenges\n')
    f.write('  steps:\n')
    f.write('  - intent: bot_challenge\n')
    f.write('  - action: utter_iamabot\n\n')

    for intent in intents:
        f.write('\n- rule: ' + intent)
        f.write('\n  steps:\n')

        intent_name = intent.replace(" ", "_") # substitui espaços por underline
        f.write('  - intent: 'f'{intent_name}\n')  # adiciona os intents com a formatação desejada
        intent_name = intent.replace(" ", "_") # substitui espaços por underline
        response = """{}""".format(responses[i].replace('"', '\\"'))  # adiciona aspas triplas e substitui aspas duplas por suas sequências de escape correspondentes
        response = response.replace('\n', '\\n')  # adiciona barra invertida antes de cada quebra de linha
        f.write('  - action: 'f'utter_{intent_name}\n')



# ################################ APAGAR DEPOIS ###############################

# with open('data/nlu.yml', 'w', encoding='utf-8') as f:
#     f.write('version: "3.1"\n\n')
#     f.write('nlu:\n')

# ###### add padrao
#     for intent in intents:
#         intent_name = intent.replace(" ", "_")
#         f.write('  - intent: 'f'{intent_name}\n')
#         f.write('    examples: | \n')
#         f.write('      - \n')
#         f.write('      - \n\n')