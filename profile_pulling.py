import requests
import time
import traceback

def get_array_pair_by_address(ether_address):
    remaining = True
    offset = 0
    kitties_id_list = []
    if remaining:
        url = "https://api.cryptokitties.co/kitties?offset="+str(offset)+"&limit=20&parents=false&owner_wallet_address="+ether_address
        kitty_json = requests.get(url).json()
        for each in kitty_json['kitties']:
            kitties_id_list.append(each['id'])
        offset += 20
        if len(kitty_json['kitties']) == 0:
            remaining = False

    #build a pair of array
    kitties_pair_list = []
    for each in kitties_id_list:
        for inner in kitties_id_list:
            if each != inner:
                kitties_pair_list.append([each,inner])

    print(len(kitties_pair_list))
    return kitties_pair_list

get_array_pair_by_address("0x4ce15b37851a4448a28899062906a02e51dee267")
