import json
import matplotlib.pyplot as plt
import requests
import re
import pandas as pd
import seaborn as sns

sns.set()
def mergeDict(dict1, dict2):
   dict3 = {**dict1, **dict2}
   for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = dict1[key] + dict2[key]
   return dict3

def get_asn_name(asn):
    url='https://stat.ripe.net/data/as-overview/data.json?resource={}'.format(asn)
    json_data = requests.get(url)
    if (json_data.status_code == 200):
        json_data = json.loads(json_data.content.decode('utf-8'))
        short_asn_name = re.split(' |-', json_data['data']['holder'])[0]
        return(short_asn_name)
    else:
        return(asn)

with open('inter_transit.json', 'r') as f:
    country_neighbours=json.load(f) 
    merged_country_neighbours = dict()
    for country in country_neighbours:
        merged_country_neighbours = mergeDict(merged_country_neighbours, country_neighbours[country])

    total_v4_peers = sum(merged_country_neighbours.values())
    merged_country_neighbours = {k: 100*merged_country_neighbours[k]/total_v4_peers
                                    for k in merged_country_neighbours.keys()}
    # Top neighbours have more than 1% of v4 peers
    filtered_country_neighbours = {k: merged_country_neighbours[k] for k in merged_country_neighbours
                                    if merged_country_neighbours[k] >= 3}
    other_v4_peers = 100 - sum(filtered_country_neighbours.values())
    filtered_country_neighbours['Others < 3%'] = other_v4_peers

    sorted_country_neighbours = {k: v for k, v in sorted(filtered_country_neighbours.items(), key=lambda item: item[1])}

    labels = [get_asn_name(asn) for asn in sorted_country_neighbours.keys()]
    #print(sorted_country_neighbours,labels)

    fig1, ax1 = plt.subplots()
    ax1.pie(sorted_country_neighbours.values(), labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('transit_pie.eps')

    ex_filtered_country_neighbours = {k: merged_country_neighbours[k] for k in merged_country_neighbours
                                    if merged_country_neighbours[k] >= 3}
    country_neighbours_selected=dict()
    for country in country_neighbours:
        country_neighbours_selected[country] = []
        tmp_total_v4_peers = sum(country_neighbours[country].values())
        for transit in ex_filtered_country_neighbours:
            if transit in country_neighbours[country].keys(): 
                country_neighbours_selected[country].append(100*country_neighbours[country][transit]/tmp_total_v4_peers)
            else:
                country_neighbours_selected[country].append(0)

    cluster_labels = [get_asn_name(asn) for asn in ex_filtered_country_neighbours.keys()]
    df = pd.DataFrame.from_dict(country_neighbours_selected, orient='index', columns = cluster_labels)
    df = df.T
    print(df)
    fig2, ax2 = plt.subplots()
    ax2 = sns.clustermap(df, method="single", metric="correlation", figsize=(15, 12), vmin=0, vmax=5, cmap="YlGnBu")
    ax2.ax_row_dendrogram.set_visible(False)
    #ax.ax_col_dendrogram.set_visible(False)
    plt.savefig('transit_cluster.eps')
 