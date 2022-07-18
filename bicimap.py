import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests
import math
import geopandas
import argparse

if __name__ == '__main__':
 def argument_parser():
  parser = argparse.ArgumentParser(description= 'Quieres saber todos los parques con la estacion de bici mas cercana o un solo parque con su estacion de bici' )
  parser.add_argument('-f', '--function', type=str)
  args = parser.parse_args()
  return args

 n1 = str(input ("¿Quieres ver un parque o uno en concreto?:"))
 n2 = str(input('¿En que parque estas interesado?'))


 if __name__ == '__main__':
    print(type(argument_parser()))
    if argument_parser().function == 'todas':
        result = pd.read_csv('/Users/FVILLALOBOS/Ironhack//data_project_m1_Fvp/dataframe_final.csv')
        print(result)
    elif argument_parser().function == 'un':
        df_final = df_final.loc[df_final['Place of interest']==Name_park]
        print(df_final)
    else:
        result = 'FATAL ERROR...you need to select the correct method'
    print(f'The result is => {result}')


 def to_mercator(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

 def distance_meters(lat_start, long_start, lat_finish, long_finish):
    # return the distance in metres between to latitude/longitude pair point in degrees (i.e.: 40.392436 / -3.6994487)
    start = to_mercator(lat_start, long_start)
    finish = to_mercator(lat_finish, long_finish)
    return start.distance(finish)


 def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dtlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dtlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia

 #def mad_bicimad():
    i = str(input("Please enter your park of interest: "))
    a = pk_conexion_min['df_final'] == i
    return a


 response = requests.get('https://datos.madrid.es/egob/catalogo/200761-0-parques-jardines.json')
 json = response.json()
 json.keys()


 json_trabajando = json['@graph']
 json_trabajando

 df_flat_graph = pd.json_normalize(json_trabajando) 
 df_flat_graph 

 df_jardines = df_flat_graph[['title', 'address.street-address', 'location.latitude', 'location.longitude']]
 df_jardines


 df_park = df_jardines.rename({'title': 'Name_park', 'address.street-address': 'address_park', 'location.latitude': 'latitude_park', 'location.longitude': 'longitude_park'}, axis=1)
 df_park

 df_park = df_park.dropna()
 df_park

 ##TABLA SQL
 connectionDB = 'mysql+pymysql://ironhack_user:%Vq=c>G5@173.201.189.217/BiciMAD'
 engineDB = create_engine(connectionDB)
 inspector_db = inspect(engineDB)


 inspector_db.get_table_names() 

 query_1 = '''
 SELECT *
 FROM bicimad_stations

 '''

 df_1 = pd.read_sql_query(query_1, engineDB)
 df_1

 df_1[["longitude","latitude"]]=df_1["geometry.coordinates"].str.split(",",expand=True)
 df_1['longitude'] = df_1['longitude'].str.replace('[','',regex=True)
 df_1["latitude"]=df_1['latitude'].str.replace(']','',regex=True)
 df_1['latitude'] = pd.to_numeric(df_1['latitude'])
 df_1['longitude'] = pd.to_numeric(df_1['longitude'])
 df_1

 df_bici = df_1[['name', 'address','latitude','longitude']]
 df_bici

 df_bici_map = df_bici.rename({'name': 'Name to bici_map', 'address': 'address to station', 'latitude': 'latitude_bici', 'longitude': 'longitude_bici'}, axis=1)
 df_bici_map

 pk_conexion = df_park.assign(key=2).merge(df_bici_map.assign(key=2), how='left', on='key')
 pk_conexion.head().head()


 pk_conexion['distance'] = pk_conexion.apply(lambda x: haversine(x['latitude_park'], x['longitude_park'], x['latitude_bici'], x['longitude_bici']),axis=1)
 pk_conexion  

 pk_conexion_min = pk_conexion.sort_values(by=['distance'])
 pk_conexion_min

 pk_conexion_min = pk_conexion_min.groupby(['distance']).agg('min')
 pk_conexion_min = pk_conexion_min.sort_values(by=['Name_park', 'distance'])
 pk_conexion_min

 pk_conexion_min = pk_conexion_min.drop_duplicates('Name_park', keep='first')
 pk_conexion_min

 df_final = pk_conexion_min[[ 'Name_park', 'address_park', 'Name to bici_map', 'address to station' ]]
 df_final

 df_final = df_final.rename({'Name_park': 'Place of interest', 'address_park': 'Place address', 'Name to bici_map': 'BiciMAD station', 'address to station': 'Station location'}, axis=1)
 df_final

 #Name_park = input ("Please Enter your park of Interest:")
 #df_final = df_final.loc[df_final['Place of interest']==Name_park]
 #print(df_final)
