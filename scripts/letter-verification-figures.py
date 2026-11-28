#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

FP="/tmp/NotoSansCJKsc.otf"
def f(sz): return FontProperties(fname=FP, size=sz)
C_BG="#0d1117"; C_FG="#e6edf3"; C_MUTE="#8b949e"
C_BLUE="#4fc3f7"; C_GREEN="#3fb950"; C_ORANGE="#f0883e"; C_RED="#f85149"
C_PURPLE="#bc8cff"; C_YEL="#e3b341"
OUT="papers/figures/"

def newfig(w,h):
    fig=plt.figure(figsize=(w,h),facecolor=C_BG)
    ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,100); ax.set_ylim(0,100)
    ax.axis("off"); fig.patch.set_facecolor(C_BG); ax.set_facecolor(C_BG)
    return fig,ax

def box(ax,x,y,w,h,title,lines,fc,ec,fs=9.0):
    p=FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.6",facecolor=fc,edgecolor=ec,lw=1.6)
    ax.add_patch(p)
    ax.text(x+w/2,y+h-4,title,ha="center",va="center",color=ec,fontproperties=f(11),fontweight="bold")
    yy=y+h-11.5
    for ln in lines:
        ax.text(x+w/2,yy,ln,ha="center",va="center",color=C_FG,fontproperties=f(fs))
        yy-=6.0

# ---------- 图1：资料与出处 证据等级 ----------
fig,ax=newfig(12.5,7.2)
ax.text(50,96,"公开信新增·资料与出处：按证据等级分层",ha="center",color=C_FG,fontproperties=f(16),fontweight="bold")
ax.text(50,90,"引一篇真实论文 ≠ 该论文支持我们的结论；出处属实与论证成立要分开看",
        ha="center",color=C_MUTE,fontproperties=f(10.3))
levels=[
 (2,"L1 已实验/已观测",["动态Casimir: 真空->真实光子","Breit-Wheeler阈值 1.022 MeV","m_mu/m_e=206.7682830 已测","强子谱已测"],C_GREEN,5.9),
 (22,"L2 强理论+间接",["Hawking/Unruh/Schwinger","Landauer kT ln2","BW 1934理论/SLAC多光子"],C_BLUE,5.9),
 (42,"L3 真实论文/机制",["JHEP10(2023)172 层级涌现","Z~(Lambda_QG/m0)^gamma","arXiv:2611.34924 背景独立","给机制 != 给精确值"],C_PURPLE,5.9),
 (62,"L4 东方经典",["易: 太极两仪/穷则变/未济","十二因缘: 流转/还灭门","楞严: 世界/众生/业果三相续","全部仅[结构呼应]"],C_ORANGE,5.9),
 (82,"L5 冻结案",["28.5GHz归属","18769=137^2","Omega六尺度/熵账","口径漂移","本信一条未翻"],C_RED,5.9),
]
for x,title,lines,col,fs in levels:
    box(ax,x,16,18,68,title,lines,"#15233a",col,fs)
ax.text(50,8,"L1/L2 是硬锚点；L3 只作机制背书；L4 仅结构呼应、非物理背书；L5 登记不翻案",
        ha="center",color=C_YEL,fontproperties=f(9.8))
ax.text(50,3,"全部数字由随附脚本可复算_公开信附录.py 逐项打印，正文不再手打",
        ha="center",color=C_MUTE,fontproperties=f(9))
plt.savefig(OUT+"evidence-tiers-20261127.png",dpi=150)

# ---------- 图2：三级台阶 + 五条路线 ----------
fig,ax=newfig(12.5,7.6)
ax.text(50,97,"公开信新增·理论路径：三级台阶 与 五条路线",ha="center",color=C_FG,fontproperties=f(16),fontweight="bold")
ax.text(50,91,"把『0->粒子』黑箱拆开，每级标清交出的数；找出路=把叙事拆成可证伪台阶",
        ha="center",color=C_MUTE,fontproperties=f(10.2))
# 上排：三级台阶
steps=[
 (3,62,30,"台阶① 0->光",["对标 动态Casimir[已实验]","交: 光子产生率/频谱","地位: 机制存在性"],C_GREEN),
 (35,62,30,"台阶② 光->物质",["对标 Breit-Wheeler 1.022MeV","交: 供能机制/可测信号","地位: 全理论命门"],C_RED),
 (67,62,30,"台阶③ 物质->归零",["对标 Landauer/信息消解","交: 信息量变化/能量去向","地位: [推断]非熵倒减"],C_ORANGE),
]
for x,y,w,title,lines,col in steps:
    box(ax,x,y,w,26,title,lines,"#15233a",col,8.8)
for x1,x2 in [(33,35),(65,67)]:
    ax.add_patch(FancyArrowPatch((x1,y+13),(x2,y+13),arrowstyle="-|>",mutation_scale=18,color=C_MUTE,lw=1.4))
ax.text(50,58,"台阶①只贡献『机制存在性』，不是台阶②的低频版；两者能标差约 11 级",
        ha="center",color=C_YEL,fontproperties=f(9.5))
# 下排：五条路线
routes=[
 (2,12,18,"甲 叙事骨架",["0<=>1<=>Omega","交不出数","动机别丢"],C_MUTE),
 (21,12,18,"乙 低能新物理",["须可测信号","LEP/CMS已封","休眠"],C_RED),
 (40,12,18,"丙 普朗克",["门: l<=1.2132pm","3a活/3b死","半活"],C_BLUE),
 (59,12,18,"丙' QCD质量",["尺度约1fm","交强子谱比值","唯一已测可比值"],C_GREEN),
 (78,12,20,"还灭门 归藏",["信息结构消解","交信息量+代价","[推断]绕开熵账"],C_PURPLE),
]
for x,y,w,title,lines,col in routes:
    box(ax,x,y,w,40,title,lines,"#15233a",col,8.4)
ax.text(50,9,"收敛一问: 本原有没有 l <= 386 fm 的表述? 有->交出进丙-2; 没有->承认是叙事骨架",
        ha="center",color=C_YEL,fontproperties=f(9.6))
ax.text(50,4,"丙'代价必须写全: 唯一可比值 + 放弃统一全部质量(强子/轻子分治)",
        ha="center",color=C_MUTE,fontproperties=f(8.8))
plt.savefig(OUT+"theory-ladder-routes-20261127.png",dpi=150)

# ---------- 图3：能标鸿沟 + 复算看板 ----------
fig,ax=newfig(12,7.2)
ax.text(50,96,"公开信新增·可验证复算：能标鸿沟与 25 项自检",ha="center",color=C_FG,fontproperties=f(16),fontweight="bold")
ax.text(50,90,"所有数字由脚本自建常量逐项打印，断言失败即报错；正文不再手打",
        ha="center",color=C_MUTE,fontproperties=f(10.3))
# 能标阶梯（对数）
bars=[
 (8,"1 bit擦除 300K",0.017919,"eV",C_BLUE),
 (32,"5GHz光子",2.07e-5,"eV",C_GREEN),
 (56,"2m_ec^2阈值",1.021998e6,"eV",C_RED),
]
import math
base=1e-6; top=1e7
lo=math.log10(base); hi=math.log10(top)
def ypos(v):
    return 18 + (math.log10(v)-lo)/(hi-lo)*58
for x,name,val,unit,col in bars:
    yy=ypos(val)
    ax.bar(x-4,yy-16,8,bottom=16,color=col,alpha=0.85)
    ax.text(x,yy+1.5,f"{val:.3g} {unit}",ha="center",color=col,fontproperties=f(9.2),fontweight="bold")
    ax.text(x,11,name,ha="center",color=C_FG,fontproperties=f(8.8))
    ax.text(x,7,f"log10={math.log10(val):.2f}",ha="center",color=C_MUTE,fontproperties=f(8.5))
ax.text(50,84,"1 bit 擦除 < 5GHz光子 < 光->物质阈值：跨越约 8 个数量级（5.7e7 倍）",
        ha="center",color=C_YEL,fontproperties=f(10))
# 右侧复算看板
box(ax,62,26,34,50,"脚本自检 25/25",[
 "A 三波长与 pi=3.1415927","B Landauer+能标鸿沟","C Casimir离阈值11级","D 28.5GHz判死测试","E h/ℏ 差2pi","F 轻子比206.768/QCD"],"#15233a",C_GREEN,8.2)
ax.text(50,3,"尺子双向: 初版脚本两处单位错均自查修正登记，不计对账——量别人也量自己",
        ha="center",color=C_MUTE,fontproperties=f(9))
plt.savefig(OUT+"energy-gap-recompute-board-20261127.png",dpi=150)
print("done")
