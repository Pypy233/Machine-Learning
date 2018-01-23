from math import log
# shannon entropy


def cal_shannon_ent(data_set):
    enteries_num = len(data_set)
    label_counts = {}
    for feat_vec in data_set:
        current_label = feat_vec[-1]
        if current_label not in label_counts.keys():
            current_label[label_counts] = 1
            