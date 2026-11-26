#!/usr/bin/env python3
"""
P8-2  复核 Aghaie-Sato (arXiv:2601.18248v2) §3.2 式(3.39)-(3.40)

原文主张（读码，p.20）：
  Z(theta,beta;Delta) ≃ (1/2) sqrt(pi/(K beta e^-S)) exp[-1/2 omega beta + 2K beta e^-S ...]
  => -(1/beta) log Z -> (1/2)omega - 2K e^-S - (1/(2beta)) log[ pi/(K beta e^-S) ]
  末项 "vanishes slowly as beta->inf but introduces a log beta correction,
  which prevents a well-defined extraction of the ground-state energy."

本脚本做的是：不采用原文的鞍点近似，而是**数值精确**地算
  Z(theta, beta; Delta) = (1/2pi) ∫ dtheta' f(theta';theta,Delta) Z(theta',beta)
其中 Z(theta',beta) 取精确 dilute-gas 形式 exp[-omega beta/2 + 2K beta e^-S cos theta']
（等价于式 3.23），f 为 Dirichlet 核。然后按 (1/beta) log 检验是否有 log beta。

关键点：Delta 固定、beta 增大的极限里，这个积分是**高斯**的，
末项系数只依赖 Delta、不依赖 beta 与否要靠数值看。
"""
import math

def dirichlet_kernel(theta, Delta):
    """f(theta; Delta) = sum_{dn=-Delta..Delta} e^{i dn theta} = sin((D+1/2)theta)/sin(theta/2)"""
    s = math.sin(theta / 2)
    if abs(s) < 1e-15:
        return 2 * Delta + 1
    return math.sin((Delta + 0.5) * theta) / s

def logZ_full(theta, beta, omega=1.0, K=1.0, S=1.0):
    """精确 Z(theta,beta)，式(3.23) 形式：log Z = -omega beta/2 + 2K beta e^-S cos theta"""
    return -0.5 * omega * beta + 2.0 * K * beta * math.exp(-S) * math.cos(theta)

def Z_truncated_numeric(theta, beta, Delta, omega=1.0, K=1.0, S=1.0, N=20001):
    """数值积分 (1/2pi)∫ f(theta';theta,Delta) Z(theta',beta) dtheta'，[-pi,pi] 等距辛普森"""
    a, b = -math.pi, math.pi
    h = (b - a) / (N - 1)
    tot = 0.0
    for i in range(N):
        th = a + i * h
        w = 1.0 if i in (0, N - 1) else (4.0 if i % 2 == 1 else 2.0)
        f = dirichlet_kernel(th - theta, Delta)
        # log 域还原，注意 Z 可能极大 → 减去参考最大值
        tot += w * f * math.exp(logZ_full(th, beta, omega, K, S))
    return tot * h / 3.0 / (2 * math.pi)

print("=" * 74)
print("[1] 检验式(3.40) 的 log beta 项：-(1/beta)log Z_trunc 对 beta 的行为")
print("    (−beta·log Z) 若线性于 beta 则 E0 可选；若含 log beta 则否")
print("=" * 74)
omega, K, S = 1.0, 1.0, 1.0
Delta = 2
theta = 0.0
print(f"参数: omega={omega}, K={K}, e^-S={math.exp(-S):.4f}, Delta={Delta}, theta={theta}")
print()
print(f"{'beta':>10} {'log Z_trunc':>18} {'(1/beta)logZ':>16} {'+log(beta)/(2beta)':>20}")
rows = []
for beta in (2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0, 1000.0):
    Z = Z_truncated_numeric(theta, beta, Delta, omega, K, S)
    lz = math.log(Z)
    rows.append((beta, lz, lz / beta))
    print(f"{beta:>10.0f} {lz:>18.6f} {lz/beta:>16.6f} {lz/beta + math.log(beta)/(2*beta):>20.6f}")

print()
print("=" * 74)
print("[2] 与原文式(3.40) 的解析形对比：-(1/beta)logZ = A - (1/(2beta))log[pi/(K beta e^-S)]")
print("    即 -(1/beta)logZ 应 ~ A + (1/(2beta))log(beta) - (1/(2beta))log[pi e^S/K]")
print("=" * 74)
A_fit = 0.5 * omega - 2 * K * math.exp(-S)
print(f"  原文给定的 A = omega/2 - 2K e^-S = {A_fit:.6f}")
print()
print(f"{'beta':>10} {'数值 -lz/beta':>16} {'原文式(3.40)预测':>20} {'差':>14}")
for beta, lz, val in rows:
    pred = A_fit - (1.0 / (2 * beta)) * math.log(math.pi / (K * beta * math.exp(-S)))
    print(f"{beta:>10.0f} {-val:>16.6f} {pred:>20.6f} {(-val) - pred:>14.6f}")

print()
print("=" * 74)
print("[3] 关键判断：log beta 项是否真让 E0 无定义？")
print("    检验 beta*[-(1/beta)logZ] = -logZ 是否 ~ A*beta + (1/2)log beta + const")
print("    若斜率 d(-logZ)/d(beta) 趋于常数且修正为 (1/2)log beta 慢变 → 极限存在")
print("=" * 74)
prev = None
for beta, lz, val in rows:
    if prev:
        db = beta - prev[0]
        slope = (-lz + prev[1]) / db
        print(f"  beta {prev[0]:>6.0f}->{beta:>6.0f}: d(-logZ)/dbeta = {slope:.6f}")
    prev = (beta, lz)
print()
print("  → 若 d(-logZ)/dbeta 单调趋近 A = {:.6f} ⇒ E0 极限存在，".format(A_fit))
print("    原文'log beta 阻止 E0 抽取'只是**收敛慢**（O(log beta/beta)），不是无定义。")

print()
print("=" * 74)
print("[4] 反事实检验：把 log beta 项人为扣除后，数值是否与原文 A 一致？")
print("=" * 74)
for beta, lz, val in rows[-4:]:
    corr = -val + math.log(beta) / (2 * beta)
    print(f"  beta={beta:>7.0f}: -lz/beta={-val:.6f}, 扣 log 项后={corr:.6f}, 原文A={A_fit:.6f}, 差={corr-A_fit:>+.2e}")
