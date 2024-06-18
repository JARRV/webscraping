import serpapi
import json
import sys
from django.core.management.base import BaseCommand
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('GOOGLE_LENS_API')
print("api_key",api_key)
from webapp.models import Item

from webapp.models import Similar_Item
class Command(BaseCommand):
    
    def test(self):
        #print(Item.objects.values('item_id','picture_link'))
        #print('-------------------')
        #print(type(Item.objects.values('item_id','picture_link')))
        
        for original_item_id, url in Item.objects.values_list('item_id','picture_link'):
            print(original_item_id,url)

    def handle(self,*args, **options):
        #get rows from ItemTable to retreive item_id and url
        #values returns dictionaries..
        idx = 0
        for original_item_id, url in Item.objects.values_list('item_id','picture_link'):
            if idx == 5:
                break
            results, original_item_id = self.fetch_similar_images(url, original_item_id)
            self.save_to_file(results)
            
            parsed_data = self.select_items(results, original_item_id) #parse_items(results)
            self.store_items(parsed_data) 
            idx +=1
        #self.test()



    def fetch_similar_images(self, url, original_item_id):
        print('--call to fetch similar images--')
        params = {
            "engine": "google_lens",
            "url": url,
            "no_cache": False,
            "api_key":api_key 
        }

        search = serpapi.search(params)
        visual_matches = search["visual_matches"]
    
        return visual_matches, original_item_id
        

    def select_items(self,visual_matches, original_item_id):
        recommerce_stores = ["Poshmark", "Depop", "Vinted", "Next", "ThredUp"]
        selected_items = []
        for item in visual_matches:
           if item.get("source") in recommerce_stores:
                chosen_item = self.parse_item(item, original_item_id)
                selected_items.append(chosen_item)
        return(selected_items)



    def save_to_file(self,images_data):
        with open('similar_image_results.json', 'w', encoding='utf-8') as file:
            json.dump(images_data, file, ensure_ascii=False, indent=4)


    def parse_item(self,item, original_item_id):
        if item.get("price"):
            price = item.get("price")
        else:
            price = "Unknown"

        item = {
            "original_item_id" : original_item_id,
            "store" : item.get("source"),
            "item_name" : item.get("title"),
            "picture_link" : item.get("thumbnail"),
            "price": price,
            "link": item.get("link")
        }
        return item
    
        
    # def parse_items(visual_matches, original_item_id):
        
    #     items = []
        
    #     for item in visual_matches:
    #         if item.get("price"):
    #             price = item.get("price")
    #         else:
    #             price = "Unknown"

    #         item = {
    #             "original_item_id" : original_item_id,
    #             "store" : item.get("source"),
    #             "item_name" : item.get("title"),
    #             "picture_link" : item.get("thumbnail"),
    #             "price": price,
    #             "link": item.get("link")
    #         }
    
    #         items.append(item)
    #     return items

    
    def store_items(self,items):
        for item in items:
            Similar_Item.objects.create(
                original_item_id = item["original_item_id"],
                store = item["store"],
                item_name = ["item_name"],
                picture_link = ["picture_link"] ,
                price = item["price"],
                link = item["link"]
            )


#handle()













