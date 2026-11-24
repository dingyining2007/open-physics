#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q2 / Q3 / Q4 结案复算
=====================
只用 Python 标准库，可直接重跑：
    python3 scripts/q2_q3_q4_resolve.py

对应 issue：
    Q2  PSI nEDM 2020 用的是频率派还是贝叶斯上限
    Q3  Mir et al. 2026 的 |theta_bar| <= pi/N 是否已被实验排除
    Q4  为什么两个 CP 相位差 11 个数量级

数据来源（外部源）：
    PSI 2020 : arXiv:2001.11966  (= PRL 124, 081803)
               d_n = (0.0 +- 1.1_stat +- 0.2_sys) x 1e-26 e.cm
               原文直接给 |d_n| < 1.8e-26 e.cm (90% C.L.)
    ILL 2006 : hep-ex/0602020, |d_n| < 2.9e-26 e.cm (90% CL)
    Sum rule : d_n = C * theta_bar,  C = 0.0050 e.fm = 5.000e-16 e.cm
    CKM      : delta_CKM = 1.14 rad (~65.4 deg), PDG
"""

import math

# ---------------------------------------------------------------- 常量
DN_PSI_SIGMA = math.hypot(1.1, 0.2)        # 组合不确定度 (x 1e-26 e.cm)
DN_PSI_LIMIT = 1.8                          # 原文直接给定的 90% CL 上限
DN_ILL2006 = 2.9                            # ILL 2006 上限
C_SUM_RULE = 5.000e-16                      # e.cm per unit theta_bar (0.0050 e.fm)
DELTA_CKM = 1.14                            # rad

Z_90_GAUSS = 1.6448536                      # 单侧 90% 高斯分位点


def q2():
    """PSI 2020 的 90% CL 上限口径"""
    print("=" * 62)
    print("Q2  PSI nEDM 2020 的统计口径")
    print("=" * 62)

    sigma = DN_PSI_SIGMA
    naive = Z_90_GAUSS * sigma              # 若按频率派 1.645 sigma 自己推
    z_implied = DN_PSI_LIMIT / sigma        # 原文的 1.8 反推出来的等效 z

    print(f"组合不确定度  sigma_comb = sqrt(1.1^2+0.2^2) = {sigma:.4f} (x1e-26)")
    print()
    print(f"(a) 频率派自推  1.645 * sigma            = {naive:.4f}  (x1e-26)")
    print(f"(b) 原文直接给定                      = {DN_PSI_LIMIT:.4f}  (x1e-26)")
    print(f"    反推等效 z = {DN_PSI_LIMIT}/{sigma:.4f}      = {z_implied:.4f}")
    print()
    print(f"结论: 原文的 1.8 对应 z ~= {z_implied:.2f}，不是 1.645。")
    print("      1.8 是 PSI 对自己数据直接给的 90% CL 上限，")
    print("      既非纯频率派 1.645 sigma，也非贝叶斯 UCL。")
    print()

    print("对 theta_bar 上限的影响：")
    for dn, tag in [(naive, "1.645 sigma 自推"),
                    (DN_PSI_LIMIT, "原文 1.8"),
                    (DN_ILL2006, "ILL 2006 2.9")]:
        val = dn * 1e-26 / C_SUM_RULE
        print(f"  |d_n| < {dn:.4f}e-26 ({tag:16s}) -> |theta_bar| < {val:.4e}")
    print()
    print("=> 3.60e-11 (原文口径) 与 3.68e-11 (1.645 sigma 口径) 必须并存，")
    print("   不能只留一个。差 2.2%，来源是我自己多加的一步。")
    print()


def q3():
    """Mir et al. 的 |theta_bar| <= pi/N 需要的 N"""
    print("=" * 62)
    print("Q3  Mir et al. 2026  |theta_bar| <= pi/N")
    print("=" * 62)

    print("机制（式 3.6，鸽笼原理，纯几何，无物理输入）：")
    print("  单位圆上 N 个等距点，必有一个距原点 <= pi/N")
    print("  => |theta_bar_eff| <= pi/N   [不会被反驳的一步]")
    print()

    for tb, tag in [(3.60e-11, "原文 1.8 口径"),
                    (3.68e-11, "1.645 sigma 口径")]:
        n_min = math.pi / tb
        print(f"要满足 |theta_bar| < {tb:.2e} ({tag}):")
        print(f"  N > pi / {tb:.2e} = {n_min:.4e}")
    print()

    print("N 有没有独立下界？")
    print("  论文: N 由 discrete clockwork 链的层数给出，")
    print("        'modest microscopic inputs multiply into")
    print("         exponentially large effective identifications'")
    print("  => 层数自由 => N 自由。未找到任何量子引力对 N 的上/下界约束。")
    print()
    print("论文反而论证离散规范对称是 QG *尊重* 的:")
    print("  'quantum gravity admits no exact global symmetries")
    print("   but does permit exact discrete gauge symmetries'")
    print("  => 不能反过来用 QG 卡 N 的上下界。")
    print()
    print("结论: N 是自由参数 -> 这条路径能'符合'任何更严格的上限 (= 被数据泡软)")
    print("      但它有一个格点可测的特征预言：")
    print("        theta 依赖分段解析，在约化周期奇分数倍处有 cusp")
    print("        全局曲率按 1/N^2 标度")
    print("      => 不判死：机制正确、参数自由、有一个可独立定 N 的观测")
    print()


def q4():
    """两个 CP 相位的量级差"""
    print("=" * 62)
    print("Q4  两个 CP 相位为何差 11 个数量级")
    print("=" * 62)

    for tb in (3.60e-11, 3.68e-11):
        ratio = DELTA_CKM / tb
        decades = math.log10(ratio)
        print(f"  delta_CKM = {DELTA_CKM:.2f} rad, "
              f"theta_bar < {tb:.2e} -> ratio < {ratio:.3e} "
              f"({decades:.1f} decades, {decades:.1f} 个数量级)")
    print()
    print("判别标准（本 issue 的真正成果）：")
    print("  不问'你的理论对不对'，问'你的额外输入能不能被独立测量'")
    print()
    rows = [
        ("PQ 轴子",        "新全局对称 + 破缺能标 f_a", "能 (轴子耦合, ADMX/SN1987A)", "解释"),
        ("Nelson-Barr",    "新粒子 + 质量矩阵强制实",   "能 (CKM CP 相位偏差)",        "解释"),
        ("高能 CP 守恒",   "一个新假设 + 破缺机制",     "部分 (须说明破缺能标)",       "改名"),
        ("Mir Z_N 投影",   "N 自由",                     "能 (格点 cusp 位置反解 N)",   "改名*"),
        ("无质量上夸克",   "无",                         "-",                          "已被格点排除"),
    ]
    w = [16, 26, 30, 12]
    hdr = ("方案", "额外输入", "该输入可否独立测量", "判定")
    print("  " + "".join(h.ljust(x) for h, x in zip(hdr, w)))
    print("  " + "-" * (sum(w) + 4))
    for r in rows:
        print("  " + "".join(c.ljust(x) for c, x in zip(r, w)))
    print()
    print("  * Mir 的判定为'改名'，但它的 N 理论上有格点反解路径；")
    print("    在 N 被格点定下来之前，它仍属自由参数。")
    print()
    print("结论: 不是'为什么差 11 个量级'的问题，")
    print("      是'哪个方案的额外输入能被独立测量'的问题。")
    print()


if __name__ == "__main__":
    q2()
    q3()
    q4()
    print("=" * 62)
    print("全部完成。本脚本只用标准库，可直接重跑。")
    print("=" * 62)
