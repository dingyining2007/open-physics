# 外部源引用记录

每条记录：**引用对象 → 核验方式 → 核验结果 → 时间**

格式刻意保持可机器检查：任何人可以按 URL 重跑一遍。

---

## 1. arXiv:2608.23633 — Running vacuum under DESI-DR2

| 项 | 内容 |
|---|---|
| 标题 | Testing the running vacuum model in light of DESI-DR2 Measurements |
| 作者 | Lamiae Kardaddech, Safae Dahmani, A. Bouali, T. Ouali, A. Errahmani |
| 提交 | 2026-08-23 |
| 核验方式 | ① `https://arxiv.org/abs/2608.23633` → HTTP 200，作者与提交历史齐全<br>② `https://arxiv.org/html/2608.23633v1` → HTTP 200，303966 字节，式 (3) 与 Table 4 完整<br>③ Semantic Scholar `paper/arXiv:2608.23633` → 命中 paperId `fb21037ad110466af4e2347c5647d3cf0d239c38` |
| 结果 | ✅ 真实存在 |
| 时间 | 2026-11-10 21:40 (GMT+8) |

**为什么记这条**：某高能力 AI 模型断言此编号虚构。三源核验后确认其判断错误
（编号中 "2608" = 2026 年 8 月，可能超出该模型训练分布）。

**规则**：任何人说「这篇文献不存在」时，必须自己三源核查。

---

## 2. arXiv:2606.05352 — Solà 组 running vacuum 综述

| 项 | 内容 |
|---|---|
| 标题 | Running Vacuum in the expanding Universe: a unified QFT paradigm for Inflation and Dark Energy |
| 期刊 | Int.J.Mod.Phys.A 41, 2630009 |
| 核验方式 | `https://arxiv.org/abs/2606.05352` → HTTP 200 |
| 关键原文 | "ρ_vac evolves **very slowly** with the expansion, δρ_vac ~ O(m_Pl²H²)" |
| 时间 | 2026-11-10 21:42 |

**用途**：与 [1] 的拟合值 ν=0.109 对照 —— 综述自称 "very slowly"，
但 ν=0.109 时 z=10 的 ρ_vac 是今天 70 倍。**两文口径矛盾，待查。**

---

## 3. Phys.Rev.Lett. 124, 081803 — PSI nEDM 2020

| 项 | 内容 |
|---|---|
| DOI | 10.1103/PhysRevLett.124.081803 |
| arXiv | 2001.11966 |
| 标题 | Measurement of the Permanent Electric Dipole Moment of the Neutron |
| 作者 | C. Abel, S. Afach, N. Ayres, C. A. Baker, G. Ban, G. Bison, ... |
| 核验方式 | Semantic Scholar `paper/DOI:10.1103/PhysRevLett.124.081803` → 返回完整摘要 |
| 摘要原文 | "The measured value of the neutron EDM is d_n = (0.0 ± 1.1_stat ± 0.2_sys) × 10⁻²⁶ e·cm" |
| 时间 | 2026-11-10 22:08 |

**⚠️ PDF 下载失败**：`https://arxiv.org/pdf/2001.11966v2` 与 `v3` 返回 6213 字节的 HTML（404 页）；
`v1` 返回 432907 字节但 `pdftotext` 报 `Couldn't find trailer dictionary`。
**⇒ 只核了摘要，未核正文的上限计算方法（频率派 vs 贝叶斯）。**

---

## 4. Phys.Rev.Lett. 97, 131801 — ILL nEDM 2006

| 项 | 内容 |
|---|---|
| DOI | 10.1103/PhysRevLett.97.131801 |
| arXiv | hep-ex/0602020 |
| 作者 | C. A. Baker, D. D. Doyle, P. Geltenbort, K. Green, M. van der Grinten, P. Harris, ... |
| 摘要原文 | "The results may be interpreted as an upper limit on the neutron EDM of \|d(n)\| < 2.9 × 10⁻²⁶ e·cm (**90% C.L.**)" |
| 时间 | 2026-11-10 22:08 |

---

## 5. Phys.Rev.Lett. 83, 2526 — Pospelov & Ritz 1999

| 项 | 内容 |
|---|---|
| DOI | 10.1103/PhysRevLett.83.2526 |
| arXiv | hep-ph/9904483 |
| 标题 | Theta induced electric dipole moment of the neutron via QCD sum rules |
| 摘要原文 | "we calculate the EDM of the neutron induced by a vacuum theta-angle to approximately 40-50% precision, **d_n = 2.4 × 10⁻¹⁶ θ e·cm**. Combined with the new experimental bound, this translates into the limit **\|θ\| < 3 × 10⁻¹⁰**." |
| 时间 | 2026-11-10 22:11 |

---

## 6. Nucl.Phys.B 573, 177 — Pospelov & Ritz 2000

| 项 | 内容 |
|---|---|
| DOI | 10.1016/S0550-3213(99)00817-2 |
| arXiv | hep-ph/9908508 |
| 标题 | Theta vacua, QCD sum rules, and the neutron electric dipole moment |
| 摘要原文 | "At next-to-next-to-leading order in the operator product expansion, we find the result **d_n(θ) = 1.2 × 10⁻¹⁶ θ e·cm**, to approximately 40% precision." |
| 时间 | 2026-11-10 22:11 |

**⚠️ 关键观察**：同一作者、同一方法，**NNLO 计算把系数从 2.4×10⁻¹⁶ 砍到 1.2×10⁻¹⁶（差 2 倍）**。
这是个警示：理论系数的系综不确定度至少 2 倍。

---

## 7. Phys.Lett.B 88, 123 — Crewther, Di Vecchia, Veneziano, Witten 1979

| 项 | 内容 |
|---|---|
| DOI | 10.1016/0370-2693(79)90128-X |
| 标题 | Chiral Estimate of the Electric Dipole Moment of the Neutron in Quantum Chromodynamics |
| 核验方式 | Semantic Scholar 命中 paperId `d89a74aa2580ebf257cef91711d6d3b2324b5a57`；**摘要为空** |
| PDF 尝试 | `http://cds.cern.ch/record/133382/files/197909176.pdf` → 返回 7495 字节 HTML（**Anubis 反爬挑战页**） |
| 结果 | ⚠️ **只核到文献存在，未核到原文公式** |
| 时间 | 2026-11-10 22:12 |

**⇒ 本文档中「CDVW 1979 给 3.6×10⁻¹⁶」这个数是从二手综述（Pospelov-Ritz 2005 review）转录，标【推断】。**

---

## 8. Annals Phys. 318, 119 — Pospelov & Ritz 2005 综述

| 项 | 内容 |
|---|---|
| DOI | 10.1016/j.aop.2005.04.002 |
| arXiv | hep-ph/0504231 |
| PDF | ✅ 528174 字节，**62 页**，`pdftotext -layout` 成功，3230 行 |
| 时间 | 2026-11-10 22:13 |

**本条是唯一成功解析的 PDF。** 从中核到的原文：

- **式 (2.15)**：`θ̄ = θ + Arg Det M_q`
- **式 (2.24)**：`d_n ∼ e θ̄ m* / Λ_had² ∼ θ̄ · (6 × 10⁻¹⁷) e·cm`（数量级估计）
- **式 (2.25)**：`|θ̄| < 10⁻⁹`（用当时的实验上限）
- **式 (3.65)**：`d_n(θ̄) = (1 ± 0.5)·|⟨q̄q⟩|/(225 MeV)³ · θ̄ × **2.5×10⁻¹⁶** e·cm`
- **第 1693 行原文**："our result for d_n implies a bound **|θ̄| < 3 × 10⁻¹⁰**"

**⚠️ 注意**：式 (3.65) 给 2.5×10⁻¹⁶，而 1999 PRL 摘要给 2.4×10⁻¹⁶，2000 NPB 给 1.2×10⁻¹⁶。
**同一作者三处给三个值。** 这进一步说明系数不确定度至少 2 倍。

---

## 9. arXiv:2608.22587 — Blum et al. 格点 nEDM

| 项 | 内容 |
|---|---|
| 标题 | Calculation of neutron electric dipole moment from Lattice QCD |
| 作者 | Thomas Blum, Fangcheng He, T. Izubuchi, Luchang Jin, Hiroshi Ohki, S. Syritsyn |
| 提交 | 2026-08-23 |
| Comments | 12 pages, 8 figures. See also companion paper arXiv:2607.10606 |
| 核验方式 | ① Semantic Scholar `paper/arXiv:2608.22587` → 完整摘要<br>② `https://arxiv.org/abs/2608.22587` → HTTP 200，`citation_title` / `citation_author` 相符 |
| 摘要原文 | "we obtain **d_n = −0.0050(4)(8) θ̄ e·fm**. Comparison with the current experimental bound on nEDM implies constraint **\|θ̄\| ≲ 10⁻¹¹**" |
| 时间 | 2026-11-10 22:20 |

**⚠️ 未解矛盾**：论文说 10⁻¹¹，我用 PSI 2020 的 90% CL 上限 + 该系数算出 3.68×10⁻¹¹，差 3.7 倍。
**原因未确认**（可能他们用了更紧的实验上限，或用后验而非频率派上限）。

---

## 10. arXiv:2510.18951 — Benabou et al. 2025「Clearing up the Strong CP problem」

| 项 | 内容 |
|---|---|
| 提交 | 2025-10-21 |
| 第一作者 | Joshua N. Benabou |
| 核验方式 | `https://arxiv.org/abs/2510.18951` → HTTP 200，摘要抓到 |
| 摘要原文 | "when P or CP is realized as a **gauged discrete symmetry** — as can arise in quantum gravity — the vacuum necessarily preserves CP" |
| 时间 | 2026-11-10 22:22 |

---

## 11. arXiv:2603.05195 — Mir et al. 2026「Discrete θ Projection」

| 项 | 内容 |
|---|---|
| 提交 | 2026-03-05 |
| 第一作者 | Sameer Ahmad Mir |
| 核验方式 | `https://arxiv.org/abs/2603.05195` → HTTP 200 |
| 摘要原文 | "coupling QCD to a compact, local and gapped topological sector orbifolds the path integral ... the theory dynamically selects the branch closest to the CP-symmetric point, enforcing **\|θ̄\| ≤ π/N** without assuming any prior smallness" |
| 时间 | 2026-11-10 22:22 |

**可检验预言**：要满足 \|θ̄\| < 3.68×10⁻¹¹，需 **N > 8.5×10¹⁰**。

---

## 12. arXiv:2604.28035 — θ 依赖综述（教学向）

| 项 | 内容 |
|---|---|
| 提交 | 2026-04-30（v2） |
| 第一作者 | Claudio Bonanno |
| 核验方式 | `https://arxiv.org/abs/2604.28035` → HTTP 200 |
| 摘要要点 | "pedagogical introduction to the main theoretical aspects related to topology and θ-dependence in QCD ... (η′ physics, neutron EDM) and beyond (strong CP problem and the axion solution)" |
| 时间 | 2026-11-10 22:22 |

---

## 核验工具链（可复用）

```bash
# ① DOI → arXiv / 摘要（Semantic Scholar，注意 429 限流，需 sleep 10-30s）
curl -s "https://api.semanticscholar.org/graph/v1/paper/DOI:<DOI>?fields=title,year,externalIds,abstract,openAccessPdf"

# ② arXiv ID → 摘要（直接抓 abs 页，比 API 稳）
curl -sL -A "Mozilla/5.0" "https://arxiv.org/abs/<ID>" | grep -o 'citation_title" content="[^"]*"'

# ③ 标题 → DOI（Crossref，禁止手写 DOI）
curl -s -G "https://api.crossref.org/works" \
  --data-urlencode "query.bibliographic=<标题>" --data-urlencode "rows=5" \
  --data-urlencode "select=DOI,title,author,container-title,volume,page"

# ④ PDF 健康检查（三条全过才算拿到）
file x.pdf && pdftotext -layout x.pdf x.txt && wc -l x.txt
```

**已知不可用**：
- `cds.cern.ch` PDF → Anubis 反爬挑战页
- arXiv API `export.arxiv.org/api/query` 间歇返回 0 字节，需 `--retry 2 --retry-delay 5`
- Semantic Scholar 无 key 时限流严格（429）

---

*最后更新：2026-11-10 22:35（GMT+8）*
