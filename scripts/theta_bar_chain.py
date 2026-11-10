#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""theta-bar_QCD 全链复算: nEDM 实验 -> d_n 上限 -> |theta-bar| 上限 -> 轴子质量

用法: python3 theta_bar_chain.py
无第三方依赖。
"""
import math

# ============ ① 实验输入 ============
# PSI nEDM 2020, Phys.Rev.Lett. 124, 081803 (arXiv:2001.11966)
DN_STAT = 1.1e-26      # e.cm
DN_SYST = 0.2e-26      # e.cm
# ILL nEDM 2006, Phys.Rev.Lett. 97, 131801
DN_ILL  = 2.9e-26      # e.cm, 90% CL

# ============ ② 理论系数 d_n / theta_bar  (e.cm) ============
COEF = {
    "CDVW 1979 (Phys.Lett.B 88,123)":      3.6e-16,
    "Pospelov-Ritz 1999 (PRL 83,2526)":    2.4e-16,
    "Pospelov-Ritz 2000 (NPB 573,177)":    1.2e-16,
    "Blum et al. 2026 (arXiv:2608.22587)": abs(-0.0050) * 1e-13,   # e.fm -> e.cm
}

Z = {"1 sigma": 1.0, "90% CL": 1.645, "95% CL": 1.96}


def main():
    sigma = math.hypot(DN_STAT, DN_SYST)
    print("=" * 70)
    print("① 合并实验不确定度")
    print("=" * 70)
    print("  sigma_comb = sqrt(%.2e^2 + %.2e^2) = %.4e e.cm"
          % (DN_STAT, DN_SYST, sigma))
    for lab, z in Z.items():
        print("  %-8s => |d_n| < %.4e e.cm" % (lab, z * sigma))

    print("\n" + "=" * 70)
    print("② 各理论系数与对应的 |theta-bar| 上限 (90% CL)")
    print("=" * 70)
    for k, c in COEF.items():
        print("  %-40s C=%.2e  |theta|<%.3e" % (k, c, 1.645 * sigma / c))

    print("\n" + "=" * 70)
    print("③ 旧值 1.18e-10 的来源反查")
    print("=" * 70)
    print("  ILL2006 上限 %.1e / PR1999-PRL 系数 %.1e = %.4e"
          % (DN_ILL, 2.4e-16, DN_ILL / 2.4e-16))
    print("  => 1.18e-10 是 [2006 实验 + 1999 理论] 的组合")

    print("\n" + "=" * 70)
    print("④ 更新后 vs 旧值")
    print("=" * 70)
    new = 1.645 * sigma / COEF["Blum et al. 2026 (arXiv:2608.22587)"]
    old = DN_ILL / 2.4e-16
    print("  old = %.3e   new = %.3e   收紧 %.1f 倍" % (old, new, old / new))

    print("\n" + "=" * 70)
    print("⑤ 精细调谐量级")
    print("=" * 70)
    for lab, v in [("CKM 相位 delta", 1.14),
                   ("theta-bar (new)", new),
                   ("theta-bar (paper claim)", 1e-11)]:
        print("  %-26s %.3e   1/x = %.3e" % (lab, v, 1 / v))

    print("\n" + "=" * 70)
    print("⑥ QCD 轴子质量: m_a * f_a = sqrt(chi(0))")
    print("=" * 70)
    chi14 = 75.5e6              # eV, chi(0)^(1/4)  <-- 未核原始文献
    chi_half = chi14 ** 2       # eV^2
    print("  chi(0)^(1/4) = %.1f MeV  =>  chi(0)^(1/2) = %.4e eV^2"
          % (chi14 / 1e6, chi_half))
    for fa in [1e9, 1e10, 1e11, 1e12]:
        ma = chi_half / (fa * 1e9)
        print("  f_a=%.0e GeV -> m_a=%.3e eV (%8.2f ueV)  口诀 %.1f ueV"
              % (fa, ma, ma * 1e6, 5.70 * 1e12 / fa))


if __name__ == "__main__":
    main()
