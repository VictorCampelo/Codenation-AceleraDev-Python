# -*- coding: utf-8 -*-
import json
import hashlib

class Caesar:
    @staticmethod
    def abstract_sha1(json_list):
        # initializing string 
        str = json_list['decifrado']
        # encoding using encode() 
        # then sending to SHA1() 
        print(str)
        json_list['resumo_criptografico'] = hashlib.sha1(str.encode()).hexdigest()
        return json_list

    def cesar_alg_decrypt(self, json_list):
        key = json_list['numero_casas']
        text = json_list['cifrado']
        LETTERS = 'abcdefghijklmnopqrstuvwxyz'
        text_decode = ''
        for ch in text:
            if ch in LETTERS:
                idx = LETTERS.find(ch) - key
                text_decode += LETTERS[idx]
            else:
                text_decode+=ch
        json_list['decifrado']=text_decode
        return text_decode.lower(), Caesar.abstract_sha1(json_list)
