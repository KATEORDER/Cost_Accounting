#全部原価計算による営業利益の演算
def Operating_profit_AC(S_p, M_c, F_p_c, F_SG_a_A_e, T_n_of_m, Sales):
    Sale = S_p * Sales
    C_of_s = (M_c * T_n_of_m + F_p_c) / T_n_of_m * Sales
    G_p = Sale - C_of_s
    O_p_AC = int(G_p - F_SG_a_A_e)
    return O_p_AC

#直接原価計算による営業利益の演算
def Operating_profit_DC(S_p, M_c, F_p_c, F_SG_a_A_e, Sales):
    Sale = S_p * Sales
    C_C_of_s = M_c * Sales
    C_m = Sale - C_C_of_s
    O_p_DC = int(C_m - F_p_c - F_SG_a_A_e)
    return O_p_DC


S_p = int(input("販売価格を入力してください"))

M_c = int(input("製造原価を入力してください"))

F_p_c = int(input("固定製造原価を入力してください"))

F_SG_a_A_e = int(input("固定販管費を入力してください"))

T_n_of_m = int(input("製造数を入力してください"))

Sales = int(input("販売数を入力してください"))

print("全部原価計算によって導出される営業利益は、",Operating_profit_AC(S_p, M_c, F_p_c, F_SG_a_A_e, T_n_of_m, Sales) , "円です")
print("直接原価計算によって導出される営業利益は、",Operating_profit_DC(S_p, M_c, F_p_c, F_SG_a_A_e, Sales) , "円です")
