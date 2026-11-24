#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Q1 / Q5 复算（2026-11-24）
Q1：Blum et al. 2026 的 0.0050 是 theta 还是 theta-bar？
Q5：1.18e-10 与复算 1.208e-10 的 2.3% 差异来自哪？
无第三方依赖。文本原文取自 arXiv:2608.22587 HTML 全文。
"""
import math, json

PSI_STAT, PSI_SYST = 1.1e-26, 0.2e-26
ILL_2006 = 2.9e-26
Z90 = 1.6448536269514722   # 单侧 90%，精确值

cases = {}
def add(cid, claim, got, verdict, note=""):
    cases[cid] = {"claim": claim, "got": got, "verdict": verdict, "note": note}

sigma = math.hypot(PSI_STAT, PSI_SYST)
dn90 = Z90 * sigma

# ---------- Q1 ----------
# 原文 Eq.(1): bar-theta = theta_QCD + Arg Det M_q  （物理 theta 角，含质量矩阵相位）
add("Q1_definition_explicit",
    "Blum et al. 是否显式定义 theta-bar = theta + Arg Det M_q",
    "是，Eq.(1) 原文：'where θ̄ = θ_QCD + Arg Det M_q is the physical theta-angle (including the phase of the quark mass matrix M_q)'",
    "ANSWERED",
    "与 sum rule 的 θ̄ 同一物理量定义")

add("Q1_fit_variable",
    "格点实际拟合的是哪个量",
    "Δn/θ̄ = c0 mπ² + c1 mπ² log(...)（Eq.18），拟合的是 d_n/θ̄ 比值",
    "ANSWERED",
    "d_n 与 θ̄ 成正比，拟合斜率即系数")

C_lat = 0.0050e-13  # e·fm -> e·cm
add("Q1_unit",
    "0.0050 e·fm 换 e·cm",
    f"{C_lat:.1e} e·cm（×1e-13）",
    "ANSWERED" if abs(C_lat-5e-16)/5e-16 < 1e-9 else "ERROR", "")

# 若实际算 theta 而非 theta-bar，则系数需乘 2.15（Arg Det M_q 贡献）
add("Q1_2p15_factor",
    "原「差 2.15 倍」疑虑的量级",
    "2.15 来自 |Arg Det M_q| 的估计值；本文显式含此项，故此因子不适用",
    "RETIRED",
    "结论：Q1 疑虑解除。但保留一句保留意见——论文未给出 Arg Det M_q 的数值，"
    "若格点组把 Yukawa 相位取实（Arg Det M_q = 0），则数值上 θ̄ 退化为 θ。"
    "这影响的是 theta_QCD 与 theta-bar 的归因，不影响 d_n/θ̄ 这个比值本身")

# 副发现：正文内两个电极化强度给两个值
add("Q1_side_nz",
    "|n_z|=1 与 |n_z|=2 的物理点外推结果",
    "|n_z|=1: -0.0050(4)(4); |n_z|=2: -0.0043(3)(3)；取 n_z=1 为中心值，"
    "系统误差含两者之差",
    "RECORDED",
    "差异 16%，在总误差 -0.0050(4)(8) 的 (8) 里有交代；不是矛盾，是保守取值")

# ---------- Q5 ----------
C_ill = ILL_2006 / 2.4e-16
add("Q5_reproduce_1208",
    "ILL2006 2.9e-26 / PR1999 2.4e-16",
    f"{C_ill:.6e}",
    "ANSWERED", "= 1.2083e-10")

# 反解：要让 1.18e-10 成立，三种可能
target = 1.18e-10
C_needed = ILL_2006 / target
dn_needed = target * 2.4e-16
add("Q5_required_coefficient",
    "若上限固定 2.9e-26，要得 1.18e-10 需要系数多少",
    f"{C_needed:.4e} e·cm  （相对 2.4e-16 差 {(C_needed/2.4e-16-1)*100:+.2f}%）",
    "ANSWERED", "该值不在任何一版 Pospelov-Ritz 系数里（2.4 / 1.2 / 2.5 / 2.46）")

add("Q5_required_dn",
    "若系数固定 2.4e-16，要得 1.18e-10 需要实验上限多少",
    f"{dn_needed:.4e} e·cm  （相对 2.9e-26 差 {(dn_needed/2.9e-26-1)*100:+.2f}%）",
    "ANSWERED", "ILL 2006 各版本上限在 2.9~3.0e-26 之间，无法给到 2.83e-26")

# 用 2006 年的 Pospelov-Ritz 2005 综述值 2.5e-16
C_25 = ILL_2006 / 2.5e-16
add("Q5_with_2p5",
    "PR 2005 综述 2.5e-16 代入",
    f"{C_25:.4e}",
    "ANSWERED", "= 1.160e-10，与 1.18 差 2.0%，方向变了（变小）")

# 用他引常见的 2.46e-16
C_246 = ILL_2006 / 2.46e-16
add("Q5_with_2p46",
    "2.46e-16 代入",
    f"{C_246:.4e}",
    "ANSWERED", "= 1.1789e-10 ≈ 1.18e-10 ✓ 差 0.09% —— 这是唯一对得上的组合")

add("Q5_verdict",
    "2.3% 差异的溯源结论",
    "1.18e-10 = 2.9e-26 / 2.46e-16（差 0.09%）。"
    "前三候选（2.4 / 2.5 / 1.2）分别给 1.208 / 1.160 / 2.417e-10，均对不上",
    "ANSWERED",
    "【推断】2.46e-16 常见于二手文献引用，其原始出处未核到。"
    "但数值匹配度 0.09% 远优于其他候选，可作工作假设")

counts = {}
for v in cases.values():
    counts[v["verdict"]] = counts.get(v["verdict"], 0) + 1

out = {
    "target": "open-physics Q1 / Q5",
    "date": "2026-11-24",
    "method": "自建脚本；原文取自 arXiv:2608.22587 HTML 全文（PDF 通道三次截断，已登记）",
    "counts": counts,
    "sigma_comb": sigma, "dn90": dn90, "C_lattice_e_cm": C_lat,
    "theta_bar_90CL": dn90 / C_lat,
    "cases": cases,
}
json.dump(out, open("q1_q5_result.json","w"), ensure_ascii=False, indent=1)

print(json.dumps(counts, ensure_ascii=False))
print(f"sigma_comb = {sigma:.4e}  |dn|<{dn90:.4e}")
print(f"C_lat = {C_lat:.3e} e·cm   => |theta_bar| < {dn90/C_lat:.3e}")
for k,v in cases.items():
    print(f"{v['verdict']:<11} {k}")
