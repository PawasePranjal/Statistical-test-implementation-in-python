from utils import get_data, Is_data_is_normal_by_shapiro_test, Is_Sample_size_small, \
    Is_mean_of_two_population_equal_By_T_test, Is_mean_of_two_population_equal_By_Z_test, \
    Is_mean_of_two_population_equal_By_wilcoxon_rank_sum_test

input_file_path = "C:/Users/admin/Downloads/winequality-red.csv"
alpha = 0.05
data1, data2 = get_data(input_file_path)
print(data1)
print(data2)

data_normality_status = Is_data_is_normal_by_shapiro_test(data1, alpha)
print(data_normality_status)

if data_normality_status:
    small_sample_size = Is_Sample_size_small(data1)
    if small_sample_size:
        equal_mean_by_T_test = Is_mean_of_two_population_equal_By_T_test(data1, data2, alpha)
        if equal_mean_by_T_test:
            print(f"The mean of two population grp is Same by T test with alpha={alpha}")
        else:
            print(f"The mean of two population grp is not Same by T test with alpha={alpha}")
    else:
        equal_mean_by_Z_test = Is_mean_of_two_population_equal_By_Z_test(data1, data2, alpha)
        if equal_mean_by_Z_test:
            print(f"The mean of two population grp is Same by Z test with alpha={alpha}")
        else:
            print(f"The mean of two population grp is not Same by Z test with alpha={alpha}")

else:
    small_sample_size = Is_Sample_size_small(data1)
    if small_sample_size:
        equal_mean_by_wilcoxon_test = Is_mean_of_two_population_equal_By_wilcoxon_rank_sum_test(data1, data2, alpha)
        if equal_mean_by_wilcoxon_test:
            print(f"The mean of two population grp is Same by wilcoxon test with alpha={alpha}")
        else:
            print(f"The mean of two population grp is not Same by wilcoxon test with alpha={alpha}")
    else:
        equal_mean_by_T_test = Is_mean_of_two_population_equal_By_T_test(data1, data2, alpha)
        if equal_mean_by_T_test:
            print(f"The mean of two population grp is Same by T test with alpha={alpha}")
        else:
            print(f"The mean of two population grp is not Same by T test with alpha={alpha}")