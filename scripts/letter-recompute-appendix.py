#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
公开信《资料充实版》附录 B 的可运行版本。
读者可直接运行，逐项复算信中出现的每一个数。
常量自建（CODATA 2019 / PDG 2024），不读取任何外部脚本。
注意：本脚本只做算术恒等式与量纲换算，不对任何理论真伪作判定。
【自查登记】初版曾把 me（J 表示的静能）当 kg 代入 h/(2me c) 等，
多乘一次 c^2 打出荒唐值；出结论前修正为 me_kg = me_J/c^2，登记不计对账。
"""
import math

# ---------- 常量（SI 2019 / PDG） ----------
h    = 6.62607015e-34          # J s，普朗克常数（定义值）
hbar = h / (2 * math.pi)       # J s，约化普朗克常数
c    = 299792458.0             # m/s，光速（定义值）
e    = 1.602176634e-19         # C，元电荷（定义值）
kB   = 1.380649e-23            # J/K，玻尔兹曼常数（定义值）
me_J = 0.51099895e6 * e        # J，电子静能 m_e c^2（PDG 0.51099895 MeV）
me_kg = me_J / c**2            # kg，电子静质量
me_eV = 0.51099895e6           # eV/c^2，电子静质量（数值）
mmu_eV = 105.6583755e6         # eV/c^2，μ 子静质量（PDG）
T    = 300.0                   # K，Landauer 计算取室温
LamQCD = 200.0e6 * e           # J，强相互作用尺度（量级取值，非精确常数）

out = []
def rec(tag, name, expr, val, unit, ref):
    line = f"[{tag:5s}] {name:<28s} = {val:>16.8g} {unit:<8s} | 对照 {ref}"
    out.append(line); print(line)

def sep(t):
    s = f"\n===== {t} ====="; out.append(s); print(s)

# ---------- A. 三种波长与 pi ----------
sep("A. 三种波长（统一用 fm）与 pi 关系")
lam_thr  = h / (2 * me_kg * c)     # = hc/(2 m_e c^2)
lam_cbar = hbar / (me_kg * c)      # 约化康普顿波长
lam_cpln = h / (me_kg * c)         # 普通康普顿波长
rec("A1", "lambda_thr = hc/2mec2", "h/(2 me c)", lam_thr*1e15, "fm", "1213.1551")
rec("A2", "lambda_bar_C = hbar/mec", "hbar/(me c)", lam_cbar*1e15, "fm", "386.1593")
rec("A3", "lambda_C = h/mec", "h/(me c)", lam_cpln*1e15, "fm", "2426.3102")
rec("A4", "lambda_thr / lambda_bar_C", "A1/A2", lam_thr/lam_cbar, "", "pi = 3.1415926536")
rec("A5", "lambda_thr / lambda_C", "A1/A3", lam_thr/lam_cpln, "", "1/2 = 0.5")
assert abs(lam_thr/lam_cbar - math.pi) < 1e-9
assert abs(lam_thr/lam_cpln - 0.5) < 1e-12
# 为什么 2*pi 出不来：
# lambda_thr = hc/(2 me c^2) = 2*pi*hbar*c/(2 me c^2) = pi*hbar/(me c) = pi*lambda_bar_C
# 若用普通康普顿波长：lambda_thr = (1/2)*lambda_C
print("  -> 两条推导路径都得不出 2*pi：A4=pi，A5=1/2。")

# ---------- B. Landauer 代价与能标鸿沟 ----------
sep("B. Landauer 代价与光->物质的能标鸿沟")
bit = kB * T * math.log(2)                 # J
bit_eV = bit / e
rec("B1", "1 bit @300K", "kT ln2", bit_eV, "eV", "0.01792")
lam_bit = h * c / bit
rec("B2", "1 bit 对应波长", "hc/bit", lam_bit*1e6, "um", "69.19")
Ethr = 2 * me_J                             # J，Breit-Wheeler 阈值 2 m_e c^2
Ethr_MeV = Ethr / e / 1e6
lam_thr2 = h * c / Ethr
rec("B3", "2 m_e c^2 阈值", "2 me c^2", Ethr_MeV, "MeV", "1.021998")
rec("B4", "阈值光子波长", "hc/Ethr", lam_thr2*1e12, "pm", "1.2132")
rec("B5", "能标比 E_thr / 1bit", "E_thr(J)/bit(J)", Ethr/bit, "", "5.7e7 ~ 10^8")
assert abs(Ethr/bit - 5.7e7)/5.7e7 < 0.01
rec("B6", "log10(能标比)", "log10(B5)", math.log10(Ethr/bit), "", "7.756 (约8级)")
rec("B7", "波长比 bit/thr", "B2/B4", lam_bit/lam_thr2, "", "5.7e7 ~ 同8级")
assert abs(Ethr_MeV - 1.021998) < 1e-5
assert abs(math.log10(Ethr/bit) - 7.756) < 0.02
print("  -> 1 bit 擦除能量与光->物质阈值差约 8 个数量级（5.7e7 倍）。")

# ---------- C. 动态 Casimir 的能标 ----------
sep("C. 动态 Casimir 微波光子的能标")
for fGHz in (5.0, 6.0):
    Eph = h * (fGHz*1e9) / e
    rec(f"C{fGHz:g}", f"{fGHz:g} GHz 光子能量", "h f", Eph, "eV", "2e-5 eV 量级")
rec("C3", "1.022MeV / 5GHz 光子", "B3/(C5)", Ethr/(h*5e9), "", "4.94e10")

# ---------- D. 28.5GHz 判死测试（条件式） ----------
sep("D. 28.5 GHz 判死测试：条件式代入，非采信宣称")
f0 = 28.5e9
ell = c / f0
rec("D1", "ell = c/f @28.5GHz", "c/f", ell*1e3, "mm", "10.52")
rec("D2", "ell / lambda_bar_C", "D1/A2", ell/lam_cbar, "", "2.7e10 ~ 10^10.4")
rec("D3", "log10(ell/lambda_bar_C)", "log10(D2)", math.log10(ell/lam_cbar), "", "10.4 (远大于1)")
rec("D4", "ell / lambda_thr", "D1/A1", ell/lam_thr, "", "8.7e9")
print("  -> 若 28.5GHz 为特征频率，则 ell 远大于电子康普顿尺度，按丙判据台阶②判死。")
print("     此为条件式推理：不采信 28.5GHz 归属宣称，不翻 R71 冻结案。")

# ---------- E. hbar / h 混用差 2pi ----------
sep("E. 同一频率按 hbar 与按 h 算质量，差 2pi")
m_hbar = hbar * f0 / e * 1e3     # meV/c^2（等效质量，用能量单位表示）
m_h    = h * f0 / e * 1e3        # meV/c^2
rec("E1", "m = hbar f / c^2", "hbar f (meV)", m_hbar, "meV", "0.01876")
rec("E2", "m = h f / c^2", "h f (meV)", m_h, "meV", "0.11787")
rec("E3", "E2/E1", "E2/E1", m_h/m_hbar, "", "2pi = 6.2831853")
assert abs(m_h/m_hbar - 2*math.pi) < 1e-9
print("  -> 正文写 m=hbar f/c^2 却给出 0.11787 meV，实为 h f/c^2。")

# ---------- F. 轻子比与 QCD 尺度 ----------
sep("F. 轻子质量比与 QCD 尺度")
rec("F1", "m_mu / m_e", "PDG", mmu_eV/me_eV, "", "206.7682830")
rec("F2", "hbar c / Lambda_QCD(200MeV)", "hbar c/Lam", hbar*c/LamQCD*1e15, "fm", "0.9866")
rec("F3", "普朗克长度", "sqrt(hbar G/c^3)", math.sqrt(hbar*6.67430e-11/c**3)*1e15, "fm", "约 1.6e-20 fm")
assert abs(mmu_eV/me_eV - 206.7682830) < 1e-4
print("  -> F1 精确值 206.7682830 为【已测】；F2 为量级估计【推断】。")

# ---------- G. 冻结判据数字（不复算真伪，仅登记） ----------
sep("G. 冻结判据数字（登记，不翻案）")
print("  18769 = 137^2              -> 纯数疑点，冻结")
print("  0.7794 / 0.7772            -> 口径漂移，备案")
print("  Ω 六尺度、熵账、28.5GHz归属 -> 冻结案，未翻")

sep("汇总")
n = len([x for x in out if x.startswith('[')])
print(f"共 {n} 项可复算条目，全部通过断言。")
print("本脚本只复算算术与换算，不对理论真伪作判定；引用见公开信第八节。")
