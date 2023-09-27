import math
from scipy.stats import t, ttest_ind

import System1_OutPuts
import System2_OutPuts

point_estimate_W_Aksbardari = System1_OutPuts.Y_1_W_Aksbardari - System2_OutPuts.Y_2_W_Aksbardari
point_estimate_W_Tashkil_Parvandeh = System1_OutPuts.Y_1_W_Tashkil_Parvandeh - System2_OutPuts.Y_2_W_Tashkil_Parvandeh
point_estimate_W_Takmil_Parvandeh = System1_OutPuts.Y_1_W_Takmil_Parvandeh - System2_OutPuts.Y_2_W_Takmil_Parvandeh
point_estimate_L_Aksbardari = System1_OutPuts.Y_1_L_Aksbardari - System2_OutPuts.Y_2_L_Aksbardari
point_estimate_L_Tashkil_Parvandeh = System1_OutPuts.Y_1_L_Tashkil_Parvandeh - System2_OutPuts.Y_2_L_Tashkil_Parvandeh
point_estimate_L_Takmil_Parvandeh = System1_OutPuts.Y_1_L_Takmil_Parvandeh - System2_OutPuts.Y_2_L_Takmil_Parvandeh

s_e_W_Aksbardari = math.sqrt((System1_OutPuts.Var_1_W_Aksbardari / System1_OutPuts.num_of_replications) + (
            System2_OutPuts.Var_2_W_Aksbardari / System2_OutPuts.num_of_replications))
s_e_W_Tashkil_Parvandeh = math.sqrt(
    (System1_OutPuts.Var_1_W_Tashkil_Parvandeh / System1_OutPuts.num_of_replications) + (
                System2_OutPuts.Var_2_W_Tashkil_Parvandeh / System2_OutPuts.num_of_replications))
s_e_W_Takmil_Parvandeh = math.sqrt((System1_OutPuts.Var_1_W_Takmil_Parvandeh / System1_OutPuts.num_of_replications) + (
            System2_OutPuts.Var_2_W_Takmil_Parvandeh / System2_OutPuts.num_of_replications))
s_e_L_Aksbardari = math.sqrt((System1_OutPuts.Var_1_L_Aksbardari / System1_OutPuts.num_of_replications) + (
            System2_OutPuts.Var_2_L_Aksbardari / System2_OutPuts.num_of_replications))
s_e_L_Tashkil_Parvandeh = math.sqrt(
    (System1_OutPuts.Var_1_L_Tashkil_Parvandeh / System1_OutPuts.num_of_replications) + (
                System2_OutPuts.Var_2_L_Tashkil_Parvandeh / System2_OutPuts.num_of_replications))
s_e_L_Takmil_Parvandeh = math.sqrt((System1_OutPuts.Var_1_L_Takmil_Parvandeh / System1_OutPuts.num_of_replications) + (
            System2_OutPuts.Var_2_L_Takmil_Parvandeh / System2_OutPuts.num_of_replications))

V_W_Aksbardari = (((System1_OutPuts.Var_1_W_Aksbardari / System1_OutPuts.num_of_replications) + (
            System2_OutPuts.Var_2_W_Aksbardari / System2_OutPuts.num_of_replications)) ** 2) / (
        ((System1_OutPuts.Var_1_W_Aksbardari / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)) + ((System1_OutPuts.Var_1_W_Aksbardari / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)))

V_W_Tashkil_Parvandeh = (((System1_OutPuts.Var_1_W_Tashkil_Parvandeh / System1_OutPuts.num_of_replications) + (
            System2_OutPuts.Var_2_W_Tashkil_Parvandeh / System2_OutPuts.num_of_replications)) ** 2) / (
        ((System1_OutPuts.Var_1_W_Tashkil_Parvandeh / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)) + ((System1_OutPuts.Var_1_W_Tashkil_Parvandeh / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)))

V_W_Takmil_Parvandeh = (((System1_OutPuts.Var_1_W_Takmil_Parvandeh / System1_OutPuts.num_of_replications) + (
            System2_OutPuts.Var_2_W_Takmil_Parvandeh / System2_OutPuts.num_of_replications)) ** 2) / (
        ((System1_OutPuts.Var_1_W_Takmil_Parvandeh / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)) + ((System1_OutPuts.Var_1_W_Takmil_Parvandeh / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)))

V_L_Aksbardari = (((System1_OutPuts.Var_1_L_Aksbardari / System1_OutPuts.num_of_replications) + (
            System2_OutPuts.Var_2_L_Aksbardari / System2_OutPuts.num_of_replications)) ** 2) / (
        ((System1_OutPuts.Var_1_L_Aksbardari / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)) + ((System1_OutPuts.Var_1_L_Aksbardari / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)))

V_L_Tashkil_Parvandeh = (((System1_OutPuts.Var_1_L_Tashkil_Parvandeh / System1_OutPuts.num_of_replications) + (
            System2_OutPuts.Var_2_L_Tashkil_Parvandeh / System2_OutPuts.num_of_replications)) ** 2) / (
        ((System1_OutPuts.Var_1_L_Tashkil_Parvandeh / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)) + ((System1_OutPuts.Var_1_L_Tashkil_Parvandeh / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)))

V_L_Takmil_Parvandeh = (((System1_OutPuts.Var_1_L_Takmil_Parvandeh / System1_OutPuts.num_of_replications) + (
            System2_OutPuts.Var_2_L_Takmil_Parvandeh / System2_OutPuts.num_of_replications)) ** 2) / (
        ((System1_OutPuts.Var_1_L_Takmil_Parvandeh / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)) + ((System1_OutPuts.Var_1_L_Takmil_Parvandeh / System1_OutPuts.num_of_replications) ** 2 / (
                                  System1_OutPuts.num_of_replications - 1)))

alpha = 0.05
t_alpha_2_W_Aksbardari = t.ppf(1-alpha/2, V_W_Aksbardari)
t_alpha_2_W_Tashkil_Parvandeh = t.ppf(1-alpha/2, V_W_Tashkil_Parvandeh)
t_alpha_2_W_Takmil_Parvandeh = t.ppf(1-alpha/2, V_W_Takmil_Parvandeh)
t_alpha_2_L_Aksbardari = t.ppf(1-alpha/2, V_L_Aksbardari)
t_alpha_2_L_Tashkil_Parvandeh = t.ppf(1-alpha/2, V_L_Tashkil_Parvandeh)
t_alpha_2_L_Takmil_Parvandeh = t.ppf(1-alpha/2, V_L_Takmil_Parvandeh)


right_c_i_W_Aksbardari = point_estimate_W_Aksbardari + t_alpha_2_W_Aksbardari * s_e_W_Aksbardari
left_c_i_W_Aksbardari = point_estimate_W_Aksbardari - t_alpha_2_W_Aksbardari * s_e_W_Aksbardari
print([left_c_i_W_Aksbardari,right_c_i_W_Aksbardari])
if right_c_i_W_Aksbardari > 0 and left_c_i_W_Aksbardari > 0 :
    print("By using W_Aksbardari, there is strong evidence that system2 is better than system1")
elif right_c_i_W_Aksbardari < 0 and left_c_i_W_Aksbardari < 0 :
    print("By using W_Aksbardari, there is strong evidence that system1 is better than system2")
else:
    print("By using W_Aksbardari, with the data at hand, there is no strong statistical evidence that one system design is better than the other")



right_c_i_W_Tashkil_Parvandeh = point_estimate_W_Tashkil_Parvandeh + t_alpha_2_W_Tashkil_Parvandeh * s_e_W_Tashkil_Parvandeh
left_c_i_W_Tashkil_Parvandeh = point_estimate_W_Tashkil_Parvandeh - t_alpha_2_W_Tashkil_Parvandeh * s_e_W_Tashkil_Parvandeh
print([left_c_i_W_Tashkil_Parvandeh,right_c_i_W_Tashkil_Parvandeh])
if right_c_i_W_Tashkil_Parvandeh > 0 and left_c_i_W_Tashkil_Parvandeh > 0 :
    print("By using W_Tashkil_Parvandeh, there is strong evidence that system2 is better than system1")
elif right_c_i_W_Tashkil_Parvandeh < 0 and left_c_i_W_Tashkil_Parvandeh < 0 :
    print("By using W_Tashkil_Parvandeh, there is strong evidence that system1 is better than system2")
else:
    print("By using W_Tashkil_Parvandeh, with the data at hand, there is no strong statistical evidence that one system design is better than the other")


right_c_i_W_Takmil_Parvandeh = point_estimate_W_Takmil_Parvandeh + t_alpha_2_W_Takmil_Parvandeh * s_e_W_Takmil_Parvandeh
left_c_i_W_Takmil_Parvandeh = point_estimate_W_Takmil_Parvandeh - t_alpha_2_W_Takmil_Parvandeh * s_e_W_Takmil_Parvandeh
print([left_c_i_W_Takmil_Parvandeh,right_c_i_W_Takmil_Parvandeh])
if right_c_i_W_Takmil_Parvandeh > 0 and left_c_i_W_Takmil_Parvandeh > 0 :
    print("By using W_Takmil_Parvandeh, there is strong evidence that system2 is better than system1")
elif right_c_i_W_Takmil_Parvandeh < 0 and left_c_i_W_Takmil_Parvandeh < 0 :
    print("By using W_Takmil_Parvandeh, there is strong evidence that system1 is better than system2")
else:
    print("By using W_Takmil_Parvandeh, with the data at hand, there is no strong statistical evidence that one system design is better than the other")


right_c_i_L_Aksbardari = point_estimate_L_Aksbardari + t_alpha_2_L_Aksbardari * s_e_L_Aksbardari
left_c_i_L_Aksbardari = point_estimate_L_Aksbardari - t_alpha_2_L_Aksbardari * s_e_L_Aksbardari
print([left_c_i_L_Aksbardari,right_c_i_L_Aksbardari])
if right_c_i_L_Aksbardari > 0 and left_c_i_L_Aksbardari > 0 :
    print("By using L_Aksbardari, there is strong evidence that system2 is better than system1")
elif right_c_i_L_Aksbardari < 0 and left_c_i_L_Aksbardari < 0 :
    print("By using L_Aksbardari, there is strong evidence that system1 is better than system2")
else:
    print("By using L_Aksbardari, with the data at hand, there is no strong statistical evidence that one system design is better than the other")


right_c_i_L_Tashkil_Parvandeh = point_estimate_L_Tashkil_Parvandeh + t_alpha_2_L_Tashkil_Parvandeh * s_e_L_Tashkil_Parvandeh
left_c_i_L_Tashkil_Parvandeh = point_estimate_L_Tashkil_Parvandeh - t_alpha_2_L_Tashkil_Parvandeh * s_e_L_Tashkil_Parvandeh
print([left_c_i_L_Tashkil_Parvandeh,right_c_i_L_Tashkil_Parvandeh])
if right_c_i_L_Tashkil_Parvandeh > 0 and left_c_i_L_Tashkil_Parvandeh > 0 :
    print("By using L_Tashkil_Parvandeh, there is strong evidence that system2 is better than system1")
elif right_c_i_L_Tashkil_Parvandeh < 0 and left_c_i_L_Tashkil_Parvandeh < 0 :
    print("By using L_Tashkil_Parvandeh, there is strong evidence that system1 is better than system2")
else:
    print("By using L_Tashkil_Parvandeh, with the data at hand, there is no strong statistical evidence that one system design is better than the other")


right_c_i_L_Takmil_Parvandeh = point_estimate_L_Takmil_Parvandeh + t_alpha_2_L_Takmil_Parvandeh * s_e_L_Takmil_Parvandeh
left_c_i_L_Takmil_Parvandeh = point_estimate_L_Takmil_Parvandeh - t_alpha_2_L_Takmil_Parvandeh * s_e_L_Takmil_Parvandeh
print([left_c_i_L_Takmil_Parvandeh,right_c_i_L_Takmil_Parvandeh])
if right_c_i_L_Takmil_Parvandeh > 0 and left_c_i_L_Takmil_Parvandeh > 0 :
    print("By using L_Takmil_Parvandeh, there is strong evidence that system2 is better than system1")
elif right_c_i_L_Takmil_Parvandeh < 0 and left_c_i_L_Takmil_Parvandeh < 0 :
    print("By using L_Takmil_Parvandeh, there is strong evidence that system1 is better than system2")
else:
    print("By using L_Takmil_Parvandeh, with the data at hand, there is no strong statistical evidence that one system design is better than the other")


