#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V2 自查：确认 (ℏc/G)^{3/2}/m_N² 是质量量纲，不是无量纲。
起因：我方第74轮在三处误称其为「无量纲组合」，被核验方第74轮复算指出（其 V2）。
对应文件：四_公开信_把重述和预言分开.md 第四节「自曝」段。
"""
import math
hbar = 1.054571817e-34; c = 2.99792458e8; G = 6.67430e-11
mp = 1.67262192369e-27; mn = 1.67492749804e-27
Msun = 1.98892e30

print("="*66)
print("① 量纲核验（自建 M/L/T 代数，不调外部库）")
print("="*66)
M, L, T = (1,0,0), (0,1,0), (0,0,1)
def mul(a,k): return tuple(k*x for x in a)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
hbar_d = add(add(M, mul(L,2)), mul(T,-1))
c_d     = add(L, mul(T,-1))
G_d     = add(add(mul(M,-1), mul(L,3)), mul(T,-2))
hcG     = add(add(hbar_d, c_d), mul(G_d,-1))
combo   = add(mul(hcG, 1.5), mul(M,-2))
print(f"   [ℏ]      = {hbar_d} = M L² T⁻¹")
print(f"   [c]      = {c_d} = L T⁻¹")
print(f"   [G]      = {G_d} = M⁻¹ L³ T⁻²")
print(f"   [ℏc/G]   = {hcG} = M²")
print(f"   组合量纲 = {combo} = M   ← 质量量纲，非无量纲")
assert combo == (1.0,0.0,0.0), "量纲核验失败"
print("   ✅ 结论：核验方 V2 正确，我方第74轮「无量纲」表述错误")

print()
print("="*66)
print("② 数值")
print("="*66)
for name, m in [("proton ", mp), ("neutron", mn)]:
    v = (hbar*c/G)**1.5 / m**2
    print(f"   m_N={name}: {v:.4e} kg = {v/Msun:.4f} M☉")
scale_n = (hbar*c/G)**1.5 / mn**2
Mch = 1.44*(2/2.0)**2*Msun
print(f"   M_Ch (μ_e=2, 1.44式) = {Mch:.4e} kg = 1.44 M☉")
print(f"   M_Ch / 质量尺度       = {Mch/scale_n:.4f}   ← 这才是 1.44 背后的无量纲内容")

print()
print("="*66)
print("③ 修正后的正确表述（公开信采用）")
print("="*66)
print("   ❌ 旧：「真判据是无量纲组合 (ℏc/G)^{3/2}/m_N² 达 O(1)」")
print("   ✅ 新：「(ℏc/G)^{3/2}/m_N² 是自然质量尺度 ≈ 1.85 M☉；")
print("           真无量纲判据是 天体质量/该尺度 是否 O(1)（=0.779 × M/M_Ch）」")
print()
print("   ⚠️ 此修正不改 E1 结论：六尺度仅恒星有真判据，仍成立。")
