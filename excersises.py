import pandas as pd
df1 = pd.DataFrame(columns=['id', 'company', 'name', 'price', 'complex', 'floor', 'rooms', 'area'])
df1.set_index('id', inplace=True)
print(df1.head(5))
data = [{'id': '51945', 'company': 'Yekta Homes', 'name': 'Квартира 1+1 в Газипаше, Анталья, Турция №51945', 'price': '€ 199 000', 'complex': 'Жилой комплекс Yekta Sungate Residence в Газипаше, Анталья, Турция №50121', 'floor': '1', 'rooms': '1+1', 'area': '52 м²'}, {'id': '430', 'company': 'ALTOP Real Estate', 'name': 'Вилла 5+1 в Джикджилли, Анталья, Турция №430', 'price': '€ 715 000', 'complex': None, 'floor': None, 'rooms': '5+1', 'area': '565 м²'}, {'id': '3016', 'name': 404}, {'id': '22031', 'name': 404}]
df1 = df1.append(data, sort=False)
df1.set_index('id', inplace=True)
print(df1.head(5))
