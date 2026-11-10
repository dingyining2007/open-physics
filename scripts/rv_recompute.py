#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Running Vacuum 模型约束复算 (arXiv:2608.23633 Model B, nu = 0.109)

用法: python3 rv_recompute.py
无第三方依赖。
"""
import math

# ============ 输入（全部来自 arXiv:2608.23633 Table 4 / Eq.3）============
OM   = 0.2978      # Model B, Omega_m0
OML  = 1.0 - OM    # flat
NU   = 0.109       # Model B, nu
H0   = 69.31       # km/s/Mpc

M_P_UNRED = 1.220890e28     # eV, 未约化普朗克质量
M_T       = 173e9           # eV, 顶夸克


def E2(a, Om=OM, OmL=OML, nu=NU):
    """RVM 自洽方程: E^2(a)(1-nu) = Om*a^-3 + OmL - nu"""
    return (Om * a ** -3 + OmL - nu) / (1.0 - nu)


def rho_vac_ratio(a, Om=OM, OmL=OML, nu=NU):
    """rho_vac(H)/rho_vac0 = (OmL + nu*(E^2-1))/OmL"""
    return (OmL + nu * (E2(a, Om, OmL, nu) - 1.0)) / OmL


def main():
    print("=" * 66)
    print("① nu_QFT: 论文 Eq.(3) 的 QFT 预期 vs 论文自己的拟合值")
    print("=" * 66)
    for name, MP in [("未约化 M_P", M_P_UNRED),
                     ("约化 M_P/sqrt(8pi)", M_P_UNRED / math.sqrt(8 * math.pi))]:
        print("  %-22s nu_QFT = %.4e" % (name, (M_T / MP) ** 2 / (6 * math.pi)))
    print("  %-22s nu_fit = %.4e" % ("论文拟合值", NU))
    print("\n  反解: nu = (1/6pi)(M/M_P)^2  =>  M/M_P = sqrt(6*pi*nu)")
    print("  nu = %.3f  =>  M/M_P = %.4f  (约 %.2e GeV)"
          % (NU, math.sqrt(6 * math.pi * NU),
             math.sqrt(6 * math.pi * NU) * M_P_UNRED / 1e9))

    print("\n" + "=" * 66)
    print("② 归一化自检 (必须等于 1.0)")
    print("=" * 66)
    print("  E^2(a=1) = %.15f" % E2(1.0))

    print("\n" + "=" * 66)
    print("③ rho_vac 演化")
    print("=" * 66)
    for z in [0, 1, 10, 1100]:
        print("  z=%7.0f  E^2=%.4e  rho_vac/rho_vac0=%.4e"
              % (z, E2(1 / (1 + z)), rho_vac_ratio(1 / (1 + z))))

    print("\n" + "=" * 66)
    print("④ Omega_m(z) 与增长率 f(z)=Om^0.55 的偏离")
    print("=" * 66)
    for z in [0.5, 1, 2, 5]:
        a = 1 / (1 + z)
        om_rv = OM * a ** -3 / E2(a)
        om_l = OM * a ** -3 / E2(a, nu=0.0)
        print("  z=%.1f  Omega_m 偏 %+.2f%%   f 偏 %+.2f%%"
              % (z, 100 * (om_rv / om_l - 1),
                 100 * ((om_rv ** 0.55) / (om_l ** 0.55) - 1)))

    print("\n" + "=" * 66)
    print("⑤ BBN 判据: z=1100 时 rho_vac / rho_rad  (判据 < 0.1)")
    print("=" * 66)
    om_rad0 = 9.15e-5          # Omega_rad0 (含 3 nu), rho_rad ~ (1+z)^4
    for nu in [1e-4, 1e-3, 1e-2, 5e-2, 0.109]:
        a = 1 / 1101.0
        rv = (OML + nu * (E2(a, nu=nu) - 1.0)) / OML
        ratio = (OML * rv) / (om_rad0 * 1101 ** 4)
        print("  nu=%-7.4f  rho_vac/rho_rad = %.4e  %s"
              % (nu, ratio, "OK" if ratio < 0.1 else "VIOLATES BBN"))

    # 二分找临界 nu
    lo, hi = 0.0, 0.109
    for _ in range(60):
        mid = (lo + hi) / 2
        a = 1 / 1101.0
        rv = (OML + mid * (E2(a, nu=mid) - 1.0)) / OML
        if (OML * rv) / (om_rad0 * 1101 ** 4) < 0.1:
            lo = mid
        else:
            hi = mid
    print("  临界 nu (ratio=0.1) ~= %.5f   =>  论文拟合值 0.109 超出 %.1f 倍"
          % (lo, 0.109 / lo))

    print("\n" + "=" * 66)
    print("⑥ Delta AIC -> sigma")
    print("=" * 66)
    for daic in [6.113, 7.535, 9.440]:
        print("  DeltaAIC=%.3f  =>  DeltaChi2~%.3f  =>  %.2f sigma"
              % (daic, daic, math.sqrt(daic)))
    print("  5 sigma 需 DeltaChi2 ~ 25")


if __name__ == "__main__":
    main()
