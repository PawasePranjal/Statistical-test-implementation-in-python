import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, ttest_ind, ttest_1samp
from scipy.stats import spearmanr
from numpy import random
from statsmodels.stats.weightstats import ztest
from scipy.stats import ranksums


def get_data(input_file_path):
    data = pd.read_csv(input_file_path)
    acidity_of_wine = data["fixed acidity"][0:-1]
    size = int(acidity_of_wine.shape[0] / 2)
    sample_1 = (random.choice(acidity_of_wine, size, replace=False))
    sample_2 = (random.choice(acidity_of_wine, size, replace=False))
    return sample_1, sample_2


def Is_data_is_normal_by_shapiro_test(data1, alpha):
    stat, p = shapiro(data1)
    print("stat=%.2f,p=%.20f" % (stat, p))
    if p > alpha:
        return True
    else:
        return False


def Is_Sample_size_small(data1):
    size = len(data1)
    small_sample_size = size < 50
    return small_sample_size


def Is_mean_of_two_population_equal_By_T_test(data1, data2, alpha):
    stat, p = ttest_ind(data1, data2, equal_var=True)
    print("stat=%.2f,p=%.20f" % (stat, p))
    if p > alpha:
        return True
    else:
        return False


def Is_mean_of_two_population_equal_By_Z_test(data1, data2, alpha):
    stat, p = ztest(data1, data2)
    print("stat=%.2f,p=%.20f" % (stat, p))
    if p > alpha:
        return True
    else:
        return False


def Is_mean_of_two_population_equal_By_wilcoxon_rank_sum_test(data1, data2, alpha):
    stat, p = ranksums(data1, data2)
    print("stat=%.2f,p=%.20f" % (stat, p))
    if p > alpha:
        return True
    else:
        return False

# def dependency_by_spearmanr_correlation(data1, data2, alpha):
#     stat, p = spearmanr(data1, data2)
#     print("stat=%.2f,p=%.20f" % (stat, p))
#     if p > alpha:
#         return True
#     else:
#         p < alpha
#         return False
