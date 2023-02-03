import json

for i in range(20):
    json_open = open(f'checkpoint/mctaco_dev_scores_epoch_{i}.json', 'r')
    json_load = json.load(json_open)

#print(json_load['predictions'])

    yn_lst = []

    for lst in json_load['predictions']:
        if lst == 0:
            yn_lst.append("no")
        elif lst == 1:
            yn_lst.append("yes")
    yn_str = "\n".join(yn_lst)
#print(yn_lst)

    with open(f'yn_output/al_mc-co15000/yn_epoch_{i}.txt','w') as f:
        f.write(yn_str)



