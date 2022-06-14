import requests
import os
import json
import pandas as pd
from bs4 import BeautifulSoup
from app.utils import get_item
from app.models.opinion import Opinion

class Product():
    def __init__(self, product_id=0, opinions=[], product_name="", opinions_count=0, pros_count=0, cons_count=0,average_score=0):
        self.product_id = product_id
        self.opinions = opinions
        self.product_name = product_name
        self.opinions_count = opinions_count
        self.pros_count = pros_count
        self.cons_count = cons_count 
        self.average_score = average_score

        return self

    def __str__(self, product_id, opinions, product_name, opinions_count, pros_count, cons_count,average_score):
        print(product_id.__str__())
        print(opinions.__str__())
        print(product_name.__str__())
        print(opinions_count.__str__())
        print(pros_count.__str__())
        print(cons_count.__str__())
        print(average_score.__str__())
        retur

    def __repr__(self, product_id, opinions, product_name, opinions_count, pros_count, cons_count,average_score ):
        print(product_id.__repr__())
        print(opinions.__repr__())
        print(product_name.__repr__())
        print(opinions_count.__repr__())
        print(pros_count.__repr__())
        print(cons_count.__repr__())
        print(average_score.__repr__())

    def to_dict(self):  
        

    def opinions_to_dict(self opinion):
        for key, value in selectors.items():
            setattr(self, key, get_item(opinion, *value))
        self.opinion_id = opinion ["data-entry-id"]
        return self

    def extract_product(self):
        url = f"https://www.ceneo.pl/{self.product_id}#tab=reviews"
        response = requests.get(url)
        page = BeautifulSoup(response.text, 'html.parser')
        self.product_name = get_item(page, "h1.product-top__product-info__name")
        while(url):
            response = requests.get(url)
            page = BeautifulSoup(response.text, 'html.parser')
            opinions = page.select("div.js_product-review")
            for opinion in opinions:
                self.opinions.append(Opinion().extract_opinion())
            try:    
                url = "https://www.ceneo.pl"+get_item(page,"a.pagination__next","href")
            except TypeError:
                url = None

    def process_stats(self):
        opinions = pd.read_json(json.dumps(self.opinions))
        self.opinions_count: len(self.opinions.index)
        self.pros_count: self.opinions.pros.map(bool).sum()
        self.cons_count: self.opinions.cons.map(bool).sum()
        self.average_score: self.opinions.stars.mean().round(2)
        
        return self


    def opinions_do_df(self):
        opinions = pd.read_json(j)

        return opinions    
    
    def save_opinions(self):
        if not os.path.exists("app/opinions"):
            os.makedirs("app/opinions")
        with open(f"app/opinions/{self.opinionsproduct_id}.json", "w", encoding="UTF-8") as jf:
            json.dump(self.opinions, jf, indent=4, ensure_ascii=False)

    def save_stats(self):
        if not os.path.exists("app/opinions"):
            os.makedirs("app/opinions")
        with open(f"app/opinions/{self.opinionsproduct_id}.json", "w", encoding="UTF-8") as jf:
            json.dump(self.opinions, jf, indent=4, ensure_ascii=False)

    def read_from_json(self):
        with open("fapp/products/{self.product_id}.json", "r", encoding="UTF-8") as jf:
            product = json.load(jf)
        for opinion in opinions:
            self.opinions.append(Opinion(**opinion))