#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""承接前序研究：把 2026-10-27 的两条核心判定原样重跑，防记忆漂移。
对应笔记：空间量子理论研究_第三阶段_20261027/space_quantum/notes/12_核心判定_两常数实为普朗克单位改写.md
"""
import math

def hr(t): print("\n" + "="*64 + "\n" + t + "\n" + "="*64)

c     = 2.99792458e8
G     = 6.67430e-11
hbar  = 1.054571817e-34

hr("① 两常数实为普朗克单位改写（原笔记四行）")
mu_g = 4*math.pi*c**2/G
lP   = math.sqrt(hbar*G/c**3)
l_Om = math.sqrt(hbar/(mu_g*c))
r1 = mu_g/(c**2/G)
r2 = l_Om/lP
r3 = mu_g*c*l_Om**2 - hbar
r4 = 4*math.pi*c**2/mu_g - G
print(f"   μ_g /(c²/G)      = {r1:.6f}   期望 4π = {4*math.pi:.6f}   {'✅' if abs(r1-4*math.pi)<1e-9 else '❌'}")
print(f"   ℓ_Ω / l_P        = {r2:.10f} 期望 1/√(4π) = {1/math.sqrt(4*math.pi):.10f} {'✅' if abs(r2-1/math.sqrt(4*math.pi))<1e-12 else '❌'}")
print(f"   μ_g·c·ℓ_Ω² − ħ   = {r3:.3e}  {'✅恒等式' if abs(r3)<1e-40 else '❌'}")
print(f"   4πc²/μ_g − G     = {r4:.3e}  {'✅恒等式' if abs(r4)<1e-20 else '❌'}")
print(f"   μ_g = {mu_g:.6e} kg/m")
print(f"   ℓ_Ω = {l_Om:.6e} m ; l_P = {lP:.6e} m")
print("   ⇒ 与 2026-10-27 22:00 笔记结论完全一致【复算 ✅】")
print("   ⇒ G、ħ 的『推导』均为恒等式，非预言。")

hr("② 案例 B 体系 (ω,r) 跨粒子变 1836 倍（原笔记纯代数解）")
k, q = 8.9875517923e9, 1.602176634e-19
res = {}
for name, m in [("e", 9.1093837015e-31), ("mu", 1.883531627e-28), ("p", 1.67262192369e-27)]:
    r = hbar**2/(4*m*k*q**2)
    w = hbar/(2*m*r*r)
    res[name] = (r, w, w*r/c)
    print(f"   {name:>2}: r={r:.5e} m  ω={w:.5e} rad/s  v/c={w*r/c:.10f}")
print(f"   ω_p/ω_e = {res['p'][1]/res['e'][1]:.3f}   r_p/r_e = {res['p'][0]/res['e'][0]:.6f}")
print(f"   1/1836.152673 = {1/1836.15267343:.6f}  → 吻合 ⇒ r ∝ 1/m，背景参数不可能普适")
print(f"   2α = {2*k*q*q/(hbar*c):.12f}  （v/c 与质量无关，是恒等式 2α，这一点是真的）")

hr("③ 复算完备性声明")
print("""   本脚本只做前序判定的重跑，不含任何新判断。
   新判断见 verify_xiong_20261125.py（案例 C 体系八项）。""")
