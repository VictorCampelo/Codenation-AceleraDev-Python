# -*- coding: utf-8 -*-
import json

class Json_manipulation:
    def write_json(self, lst):
        with open('answer.json', 'w') as f:
            json.dump(lst, f)

    def read_json(self):
        with open('answer.json', 'r') as f:
            return json.load(f)