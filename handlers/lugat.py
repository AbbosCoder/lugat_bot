import requests


def get_definition(word):
    url = f'https://meanings.onrender.com/api/{word}'
    response = requests.get(url)
    umumiy = []
    tarif = []
    try:
        definitions = response.json()[0]['MEANINGS']
        for i in definitions:
            partsOfSpeech = i['partsOfSpeech']
            mano = i['definition']
            try:
                exampleSentence = i['exampleSentence'][0]
            except:
                exampleSentence = '<strike>no examples are given</strike>'

            tarif.append(f'<b>{word}:</b>  <code>{partsOfSpeech}</code> \n<b>DEFINITION:</b> <i>{mano}.</i>\n<b>EXAMPLE:</b> <i>{exampleSentence}.\n\n</i>')

        sinonim = response.json()[0]['SYNONYMS']
        manodosh = []
        for i in sinonim:
            manodosh.append(i)
        umumiy.append(tarif)
        umumiy.append(manodosh)
        try:
            ANTONYMS = response.json()[0]['ANTONYMS']
            zidmano = []
            for u in ANTONYMS:
                zidmano.append(u)
            umumiy.append(zidmano)
        except:
            pass    

        return  umumiy
    except:
    #print(sinonim)   
        return True
