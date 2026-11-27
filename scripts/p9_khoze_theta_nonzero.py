#!/usr/bin/env python3
"""
P9  补 Khoze (arXiv:2512.06827v2) 式(26) 在 θ̄≠0 的版本

P8 已证：Khoze 式(26) 的 (2N+1) 发散因子只在 θ̄=0 成立
         （θ̄≠0 时 Dirichlet 核 D_N(θ̄) 被 1/|sin(θ̄/2)| 界住，不随 N 发散）。

本脚本答 P9 的核心问题：
  在 ACGT 次序（x→∞ 先于 N→∞）下，
  Z(θ̄) ≡ Σ_{Δn=-N}^{N} e^{iΔn θ̄} I_{Δn}(x)
  对 θ̄≠0 是否仍有 (2N+1) 那样的发散？

记归一化比值
  R(N, x, θ) = Z(N,x,θ) / ( e^x / sqrt(2π x) )
            = sqrt(2π x) · Σ_{|n|≤N} e^{i n θ} I_n(x) / e^x

三段证据：
  [A] ACGT 次序（x→∞ 先于 N 固定）：R 应 → D_N(θ)（Dirichlet 核），
      因 x≫n 时 I_n(x) ≈ e^x/sqrt(2πx)，与 n 无关。
  [B] N-扫描（固定大 x）：θ̄=0 时 R ~ 2N+1 发散；θ̄≠0 时 R 被
      2/|sin(θ̄/2)| 界住，不发散。
  [C] 生成函数恒等式：Σ_{n=-∞}^{∞} e^{i n θ} I_n(x) = e^{x cos θ}，
      θ̄≠0 时为有限值（< e^x），说明拓扑求和本身收敛、不发散。
"""
import math

# ---------- 稳定的 Bessel I 计算（log 域级数） ----------
def _logI(m, x):
    if x == 0.0:
        return 0.0 if m == 0 else -math.inf
    logs = []
    k = 0
    kmax = int(2 * x + abs(m)) + 200
    while k <= kmax:
        logs.append((2 * k + m) * math.log(x / 2.0) -
                    (math.lgamma(k + 1) + math.lgamma(k + m + 1)))
        k += 1
    mx = max(logs)
    return mx + math.log(math.fsum(math.exp(t - mx) for t in logs))


def dirichlet(N, th):
    """D_N(θ) = Σ_{n=-N}^{N} e^{i n θ} = 1 + 2 Σ_{n=1}^{N} cos(nθ)。"""
    return 1.0 + 2.0 * math.fsum(math.cos(n * th) for n in range(1, N + 1))


def R_finite(N, x, th):
    """R(N,x,θ) = sqrt(2πx) · Σ_{|n|≤N} e^{i n θ} I_n(x) / e^x
       （虚部因 I_{-n}=I_n 抵消，只剩实部）。"""
    logI0 = _logI(0, x)
    s = math.exp(logI0 - x)  # n=0
    for n in range(1, N + 1):
        s += 2.0 * math.cos(n * th) * math.exp(_logI(n, x) - x)
    return math.sqrt(2 * math.pi * x) * s


print("=" * 74)
print("[A] ACGT 次序：x→∞ 先于 N 固定，R(N,x,θ) 应 → D_N(θ)")
print("=" * 74)
print(f"{'N':>6} {'θ':>6} {'x=10':>14} {'x=50':>14} {'x=200':>14} {'x=1000':>14} {'D_N(θ)':>12}")
for N in (5, 10, 20):
    for th in (0.0, 0.1, 1.0):
        vals = [R_finite(N, x, th) for x in (10, 50, 200, 1000)]
        print(f"{N:>6} {th:>6.1f} " +
              " ".join(f"{v:>14.4f}" for v in vals) +
              f" {dirichlet(N, th):>12.4f}")
print("→ 各列随 x 增大趋于 D_N(θ)（右列）。θ̄=0 时 D_N(0)=2N+1；")
print("  θ̄≠0 时 D_N(θ̄) 为有限有界值，不随 x 发散。ACGT 次序下")
print("  '被破坏' 的判据 (2N+1) 仅对应 θ̄=0 一行。")

print()
print("=" * 74)
print("[B] N-扫描（固定 x=200）：θ̄=0 发散 vs θ̄≠0 有界")
print("=" * 74)
x = 200.0
print(f"{'N':>6} {'θ=0 (→2N+1)':>16} {'θ=0.1':>14} {'θ=1.0':>14} "
      f"{'bound(0.1)':>12} {'bound(1.0)':>12}")
for N in (2, 5, 10, 20, 50, 100, 200, 400):
    r0 = R_finite(N, x, 0.0)
    r1 = R_finite(N, x, 0.1)
    r2 = R_finite(N, x, 1.0)
    b1 = 2.0 / abs(math.sin(0.05))
    b2 = 2.0 / abs(math.sin(0.5))
    print(f"{N:>6} {r0:>16.2f} {r1:>14.3f} {r2:>14.3f} {b1:>12.2f} {b2:>12.2f}")
print("→ θ̄=0：R 随 N 线性增长（2N+1 式发散，符合 Khoze）。")
print("  θ̄=0.1：R 在 ±%.1f 内有界振荡；θ̄=1.0：在 ±%.1f 内有界振荡。" % (b1, b2))
print("  ⇒ θ̄≠0 时拓扑求和归一化比值有界，'通量和被破坏'不出现。")

print()
print("=" * 74)
print("[C] 生成函数恒等式（归一化，避免大 x 灾难性相消）：")
print("    G(x,θ) := e^{-x} Σ_{n=-∞}^{∞} e^{i n θ} I_n(x) = e^{x(cos θ - 1)}")
print("    右端 θ̄≠0 时为有限值（且 < 1），说明拓扑求和本身收敛。")
print("    说明：θ̄=1.0 时 e^{x(cosθ-1)} 在 x=100 已是 e^{-46} 量级，")
print("    由 ~e^{100} 量级 Bessel 项相消得到，数值相消 60+ 阶、不可独立核验；")
print("    故 θ̄=1.0 仅演示 x≤50（数值稳定），θ̄=0.1 可到 x=100。")
print("=" * 74)
def G_norm(N, x, th):
    """G(x,θ) = e^{-x} Σ_{|n|≤N} cos(nθ) I_n(x)，逐顶乘 e^{-x} 保持数值稳定。"""
    s = math.exp(_logI(0, x) - x)  # n=0
    for n in range(1, N + 1):
        s += 2.0 * math.cos(n * th) * math.exp(_logI(n, x) - x)
    return s
for th, xs in ((0.1, (10.0, 50.0, 100.0)), (1.0, (10.0, 50.0))):
    for x in xs:
        N = int(x) + 200
        g = G_norm(N, x, th)
        target = math.exp(x * (math.cos(th) - 1.0))
        print(f"  x={x:>6.0f} θ={th:>4.1f}  G=e^{{-x}}Σ e^{{inθ}}I_n = {g:.6e}   "
              f"e^{{x(cosθ-1)}} = {target:.6e}   比值={g/target:.8f}")
print("→ 归一化拓扑求和收敛到 e^{x(cos θ̄ - 1)}，θ̄≠0 时为有限值（< 1），")
print("  不存在 Khoze 式(26) 那种发散。其发散完全来自 θ̄=0 特例。")

print()
print("=" * 74)
print("P9 总判（全部【复算+实测·数值】）")
print("=" * 74)
print(" 1. ACGT 次序下，θ̄≠0 时归一化比值 R → D_N(θ̄)，为有限有界值，")
print("    不随 N 发散；发散只在 θ̄=0（D_N(0)=2N+1）。")
print(" 2. 完整拓扑求和 Σ_n e^{i n θ̄} I_n(x) = e^{x cos θ̄}，θ̄≠0 时有限、")
print("    收敛，说明'通量和被破坏'这一结论在 θ̄≠0 处不成立。")
print(" 3. 判定：Khoze 式(26) 的 (2N+1) 发散是 θ̄=0 专属伪影；")
print("    CP 破坏恰在 θ̄≠0，故其'破坏通量和'论证对实际 QCD（θ̄≠0）")
print("    需撤回/重写——结论反而更弱，而非更强。")
