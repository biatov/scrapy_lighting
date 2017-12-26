import csv
from datetime import datetime


class LightingPipeline(object):

    def open_spider(self, spider):
        if spider.name == 'info':
            self.file = csv.writer(open('info.csv', 'w'), quoting=csv.QUOTE_MINIMAL)
            self.file.writerow([
                'Title',
                'Id',
                'Category',
                'Reg. Price',
                'Price',
                'Image',
                'Description',
                'Height',
                'Width',
                'Length',
                'Glass',
                'Safety Listing',
                'Weight',
                'Chain',
                'Wire',
                'Number of Bulbs',
                'Max Wattage',
                'Bulb Base',
                'Light Sourse',
                'Dimmable',
                'Bulb Voltage',
                'Manufacturers_warranty',
                'Finish',
                'UPC',
                'Instructions',
                'Parts Diagram',
                'Extension',
                'Shipped Via',
                'Bulbs Included',
                'Bulb Type',
                'Color Temp',
                'CRI',
                'Light Output',
                'Rated Avg Life',
                'Canopy',
            ])

    def process_item(self, item, spider):
        if spider.name == 'info':
            self.file.writerow([
                item['title'],
                item['id'],
                item['category'],
                item['reg_price'],
                item['price'],
                item['img'],
                item['description'],
                item['height'],
                item['width'],
                item['length'],
                item['glass'],
                item['safety_listing'],
                item['weight'],
                item['chain'],
                item['wire'],
                item['number_of_bulbs'],
                item['max_wattage'],
                item['bulb_base'],
                item['light_sourse'],
                item['dimmable'],
                item['bulb_voltage'],
                item['manufacturers_warranty'],
                item['finish'],
                item['upc'],
                item['instructions'],
                item['parts_diagram'],
                item['extension'],
                item['shipped_via'],
                item['bulbs_included'],
                item['bulb_type'],
                item['color_temp'],
                item['cri'],
                item['light_output'],
                item['rated_avg_life'],
                item['canopy']
            ])
        return item
