#!/usr/bin/python
# http://adventofcode.com/2017/day/6

def main():
    input_file = open("dec06a_input.txt")
    data = input_file.read()
    
    initial_config = [ int(bank) for bank in data.split() ]
    #initial_config = [ 0, 2, 7, 0 ]
    
    bank_count = len(initial_config)
    configs = [ initial_config ]
    config_index = 0
    seen_before = False

    while not seen_before:
        config = configs[config_index]
        largest_bank = max(config)
        lb_index = config.index(largest_bank)
        blocks = config[lb_index]
        
        configs.append(configs[config_index][:])
        config_index += 1
        config = configs[config_index]
        config[lb_index] = 0

        while blocks > 0:
            lb_index = (lb_index + 1) % bank_count
            config[lb_index] += 1
            blocks -= 1

        for i in range(0, config_index - 1):
            if configs[i] == config:
                seen_before = True
                break

    print(config_index)

main()
