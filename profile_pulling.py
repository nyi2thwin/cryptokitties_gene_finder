import requests
import time
import traceback

def child_gene(kitty_pair, gene=['fancy']):
    end_point = 'http://www.kitty.services/api/gene'
    result = requests.post(end_point, json=kitty_pair)
    if result.status_code == requests.codes.ok:
        gene_result = result.json()['results']
        check_gene = filter(lambda x: x, map(lambda x: [x[0], (('%.2f' % (x[1] * 100)))] if x[0] in gene else None, gene_result))       
        counter = 0
        for genes in check_gene:
            if counter == 0:
                print('Sire %s: Matron %s' % (kitty_pair[0],kitty_pair[1]))
            counter += 1
            print('Gene %s: %s%s' % (genes[0], genes[1],'%'))
        print('=' * 20)
        
    
    return False

def get_array_pair_by_address(ether_address):
    remaining = True
    offset = 0
    kitties_id_list = []
    if remaining:
        url = "https://api.cryptokitties.co/kitties?offset="+str(offset)+"&limit=20&parents=false&owner_wallet_address="+ether_address
        kitty_json = requests.get(url).json()
        for each in kitty_json['kitties']:
            kitties_id_list.append(str(each['id']))
        offset += 20
        if len(kitty_json['kitties']) == 0:
            remaining = False

    #build a pair of array
    kitties_pair_list = []
    for each in kitties_id_list:
        for inner in kitties_id_list:
            if each != inner:
                kitties_pair_list.append([each,inner])

    print(len(kitties_pair_list),'unique pair found')
    return kitties_pair_list

#ether(cryptokitties) addresss here
address = "0x4ce15b37851a4448a28899062906a02e51dee267"
kouples = get_array_pair_by_address(address)
kouples_babe_gene = ['fancy','jaguar','violet']
for kouples_genes in kouples:
    time.sleep(1)
    child_gene(kouples_genes, kouples_babe_gene)
