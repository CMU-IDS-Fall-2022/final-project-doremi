import json
import os
import csv
 
# Get the list of all files and directories
path = "json_files"
files = os.listdir(path)
 
print("Files and directories in '", path, "' :",files)
files.sort()
print('files->',files)
songs=0
artists=0
header=['name','bio','linkName','linkUrl','monthlyListeners','worldRank','L0_city','L0_country','L0_numberOfListeners','L0_region',
'L1_city','L1_country','L1_numberOfListeners','L1_region',
'L2_city','L2_country','L2_numberOfListeners','L2_region',
'L3_city','L3_country','L3_numberOfListeners','L3_region',
'L4_city','L4_country','L4_numberOfListeners','L4_region']

rows=[]
# track=[]
artist=[]
for file in files[1:]:

    print('-----------------------------')
    print('--->'+file)
    print('-----------------------------')
    f = open(path+'/'+file)
    jsonObj=json.load(f)
    
    for i,items in enumerate(jsonObj['data']['artist']):
        

        if items=='profile':
            print('->name',jsonObj['data']['artist']['profile']['name'])
            print('->bio',jsonObj['data']['artist']['profile']['biography']['text'])

            artist.append(jsonObj['data']['artist']['profile']['name'])
            artist.append(jsonObj['data']['artist']['profile']['biography']['text'])

            try:
                print('->linkName',jsonObj['data']['artist']['profile']['externalLinks']['items'][0]['name'])
                print('->linkUrl',jsonObj['data']['artist']['profile']['externalLinks']['items'][0]['url'])
                artist.append(jsonObj['data']['artist']['profile']['externalLinks']['items'][0]['name'])
                artist.append(jsonObj['data']['artist']['profile']['externalLinks']['items'][0]['url'])
            except:
                artist.append('None')
                artist.append('None')


            
            
        if items=='stats':
            print('->monthlyListeners',jsonObj['data']['artist']['stats']['monthlyListeners'])
            print('->worldRank',jsonObj['data']['artist']['stats']['worldRank'])
            artist.append(jsonObj['data']['artist']['stats']['monthlyListeners'])
            artist.append(jsonObj['data']['artist']['stats']['worldRank'])
            print('')

            print('->L0_city',jsonObj['data']['artist']['stats']['topCities']['items'][0]['city'])
            print('->L0_country',jsonObj['data']['artist']['stats']['topCities']['items'][0]['country'])
            print('->L0_numberOfListeners',jsonObj['data']['artist']['stats']['topCities']['items'][0]['numberOfListeners'])
            print('->L0_region',jsonObj['data']['artist']['stats']['topCities']['items'][0]['region'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][0]['city'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][0]['country'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][0]['numberOfListeners'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][0]['region'])
            print('')

            print('->L1_city',jsonObj['data']['artist']['stats']['topCities']['items'][1]['city'])
            print('->L1_country',jsonObj['data']['artist']['stats']['topCities']['items'][1]['country'])
            print('->L1_numberOfListeners',jsonObj['data']['artist']['stats']['topCities']['items'][1]['numberOfListeners'])
            print('->L1_region',jsonObj['data']['artist']['stats']['topCities']['items'][1]['region'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][1]['city'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][1]['country'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][1]['numberOfListeners'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][1]['region'])
            print('')

            print('->L2_city',jsonObj['data']['artist']['stats']['topCities']['items'][2]['city'])
            print('->L2_country',jsonObj['data']['artist']['stats']['topCities']['items'][2]['country'])
            print('->L2_numberOfListeners',jsonObj['data']['artist']['stats']['topCities']['items'][2]['numberOfListeners'])
            print('->L2_region',jsonObj['data']['artist']['stats']['topCities']['items'][2]['region'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][2]['city'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][2]['country'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][2]['numberOfListeners'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][2]['region'])
            print('')

            print('->L3_city',jsonObj['data']['artist']['stats']['topCities']['items'][3]['city'])
            print('->L3_country',jsonObj['data']['artist']['stats']['topCities']['items'][3]['country'])
            print('->L3_numberOfListeners',jsonObj['data']['artist']['stats']['topCities']['items'][3]['numberOfListeners'])
            print('->L3_region',jsonObj['data']['artist']['stats']['topCities']['items'][3]['region'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][3]['city'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][3]['country'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][3]['numberOfListeners'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][3]['region'])
            print('')

            print('->L4_city',jsonObj['data']['artist']['stats']['topCities']['items'][4]['city'])
            print('->L4_country',jsonObj['data']['artist']['stats']['topCities']['items'][4]['country'])
            print('->L4_numberOfListeners',jsonObj['data']['artist']['stats']['topCities']['items'][4]['numberOfListeners'])
            print('->L4_region',jsonObj['data']['artist']['stats']['topCities']['items'][4]['region'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][4]['city'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][4]['country'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][4]['numberOfListeners'])
            artist.append(jsonObj['data']['artist']['stats']['topCities']['items'][4]['region'])
            print('')

    rows.append(artist)
    artists+=1
    print(artist)
    print('len(artist)',len(artist))
    print('')
    artist=[]

print('')
print('headers',header)
print(len(header))
print('total artists',artists)
print('data len',len(rows))

with open('spotify_data.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(header)
    write.writerows(rows)


        

        


    
