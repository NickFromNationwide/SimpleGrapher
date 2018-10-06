import statistics


def sort_by_median(input_dict, return_dict_size=1, descending_order=True):
    median_dict = {}
    return_dict = {}

    for label in input_dict:
        data = input_dict[label]
        median_dict[label] = statistics.median(data)

    median_dict = sorted(median_dict, key=median_dict.get, reverse=descending_order)

    for current_number in range(return_dict_size):
        return_dict[median_dict[current_number]] = input_dict[median_dict[current_number]]

    return return_dict


def sort_by_mean(input_dict, return_dict_size=1, descending_order=True):
    mean_dict = {}
    return_dict = {}

    for label in input_dict:
        data = input_dict[label]
        mean_dict[label] = statistics.mean(data)

    mean_dict = sorted(mean_dict, key=mean_dict.get, reverse=descending_order)

    for current_number in range(return_dict_size):
        return_dict[mean_dict[current_number]] = input_dict[mean_dict[current_number]]

    return return_dict
