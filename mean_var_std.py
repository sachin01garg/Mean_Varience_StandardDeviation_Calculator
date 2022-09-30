import numpy as np


def calculate(input_list):
    
    if len(input_list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:    
        input_list=np.array(input_list)
        input_matrix=input_list.reshape(3,3)
        # intianlize output dictionary
        output_calculations={'mean':[],
                             'variance':[],
                             'standard deviation':[],
                             'max':[],
                             'min':[],
                             'sum':[]
                            }
    # calculate mean  for [axis1,axis2,flattened] and store in output_calculations['mean']
    output_calculations['mean'].append(list(input_matrix.mean(axis=0)))
    output_calculations['mean'].append(list(input_matrix.mean(axis=1)))
    output_calculations['mean'].append(input_list.mean())

    #  calculate mean  for [axis1,axis2,flattened] and store in output_calculations['variance']
    output_calculations['variance'].append(list(input_matrix.var(axis=0)))
    output_calculations['variance'].append(list(input_matrix.var(axis=1)))
    output_calculations['variance'].append(input_list.var())

    #  calculate mean  for [axis1,axis2,flattened] and store in output_calculations['standard deviation']
    output_calculations['standard deviation'].append(list(input_matrix.std(axis=0)))
    output_calculations['standard deviation'].append(list(input_matrix.std(axis=1)))
    output_calculations['standard deviation'].append(input_list.std())

    #  calculate mean  for [axis1,axis2,flattened] and store in output_calculations['max']
    output_calculations['max'].append(list(input_matrix.max(axis=0)))
    output_calculations['max'].append(list(input_matrix.max(axis=1)))
    output_calculations['max'].append(input_list.max())
    
    # calculate mean  for [axis1,axis2,flattened] and store in output_calculations['min']
    output_calculations['min'].append(list(input_matrix.min(axis=0)))
    output_calculations['min'].append(list(input_matrix.min(axis=1)))
    output_calculations['min'].append(input_list.min())
    
    # calculate mean  for [axis1,axis2,flattened] and store in output_calculations['sum']
    output_calculations['sum'].append(list(input_matrix.sum(axis=0)))
    output_calculations['sum'].append(list(input_matrix.sum(axis=1)))
    output_calculations['sum'].append(input_list.sum())


    return output_calculations