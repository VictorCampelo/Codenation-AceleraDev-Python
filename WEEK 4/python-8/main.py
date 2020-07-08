import jwt

#  Complete a funções para rertornar um json web token, gerado usando o algoritmo HS256, 
#  que contenha a seguinte informação **{"language": "Python"}**,
#  com a palavra secreta **acelera**, complete a função para decifrar as informações tratando 
#  a exceção de quando a assinatura for inválida
#  devendo retornar o seguinte dicionário {"error": 2}.
#  Não havendo erro, retornar a informação decifrada.

def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')

def verify_signature(token):
    try:
        return jwt.decode(token, "acelera", algorithm='HS256')
    except jwt.exceptions.InvalidSignatureError:
        return {'error': 2}
    
