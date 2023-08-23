# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:53:34 2023

@author: yuyue
"""

from fitbert import FitBert

fb = FitBert()

QP1 = "在这个社会中，我认为个人或家庭生活有足够的时间是***mask***"

options_1 = ['重要的', '不重要的']

ranked_options_1 = fb.rank(QP1, options=options_1, with_prob=True)
filled_in_1 = fb.fitb(QP1, options=options_1)

print(ranked_options_1)
print(filled_in_1)

QP2 = "拥有一个我尊敬的上司（直接上级）是***mask***"

options_2 = ['重要的', '不重要的']

ranked_options_2 = fb.rank(QP2, options=options_2, with_prob=True)
filled_in_2 = fb.fitb(QP2, options=options_2)

print(ranked_options_2)
print(filled_in_2)

QP3 = "获得对出色表现的认可是***mask***"

options_3 = ['重要的', '不重要的']

ranked_options_3 = fb.rank(QP3, options=options_3, with_prob=True)
filled_in_3 = fb.fitb(QP3, options=options_3)

print(ranked_options_3)
print(filled_in_3)

QP4 = "拥有就业的安全性是***mask***"

options_4 = ['重要的', '不重要的']

ranked_options_4 = fb.rank(QP4, options=options_4, with_prob=True)
filled_in_4 = fb.fitb(QP4, options=options_4)

print(ranked_options_4)
print(filled_in_4)


QP5 = "与愉快的同事一起工作是***mask***"

options_5 = ['重要的', '不重要的']

ranked_options_5 = fb.rank(QP5, options=options_5, with_prob=True)
filled_in_5 = fb.fitb(QP5, options=options_5)

print(ranked_options_5)
print(filled_in_5)

QP6 = "做有趣的工作是***mask***"

options_6 = ['重要的', '不重要的']

ranked_options_6 = fb.rank(QP6, options=options_6, with_prob=True)
filled_in_6 = fb.fitb(QP6, options=options_6)

print(ranked_options_6)
print(filled_in_6)

QP7 = "在涉及我的工作决策时，受到我的老板的咨询是***mask***"

options_7 = ['重要的', '不重要的']

ranked_options_7 = fb.rank(QP7, options=options_7, with_prob=True)
filled_in_7 = fb.fitb(QP7, options=options_7)

print(ranked_options_7)
print(filled_in_7)


QP8 = "住在一个理想的地区是***mask***"

options_8 = ['重要的', '不重要的']

ranked_options_8 = fb.rank(QP8, options=options_8, with_prob=True)
filled_in_8 = fb.fitb(QP8, options=options_8)

print(ranked_options_8)
print(filled_in_8)

QP9 = "拥有家人和朋友尊敬的工作是***mask***"

options_9 = ['重要的', '不重要的']

ranked_options_9 = fb.rank(QP9, options=options_9, with_prob=True)
filled_in_9 = fb.fitb(QP9, options=options_9)

print(ranked_options_9)
print(filled_in_9)

QP10 = "有晋升机会是***mask***"

options_10 = ['重要的', '不重要的']

ranked_options_10 = fb.rank(QP10, options=options_10, with_prob=True)
filled_in_10 = fb.fitb(QP10, options=options_10)

print(ranked_options_10)
print(filled_in_10)


QP11 = "在我的私人生活中，我认为为了娱乐而保留时间是***mask***"

options_11 = ['重要的', '不重要的']

ranked_options_11 = fb.rank(QP11, options=options_11, with_prob=True)
filled_in_11 = fb.fitb(QP11, options=options_11)

print(ranked_options_11)
print(filled_in_11)

QP12 = "在我的私人生活中，我认为拥有一些欲望是***mask***"

options_12 = ['重要的', '不重要的']

ranked_options_12 = fb.rank(QP12, options=options_12, with_prob=True)
filled_in_12 = fb.fitb(QP12, options=options_12)

print(ranked_options_12)
print(filled_in_12)

QP13 = "在我的私人生活中，我认为为朋友提供服务是***mask***"

options_13 = ['重要的', '不重要的']

ranked_options_13 = fb.rank(QP13, options=options_13, with_prob=True)
filled_in_13 = fb.fitb(QP13, options=options_13)

print(ranked_options_13)
print(filled_in_13)

QP14 = "在我的私人生活中，我认为精打细算（不超出所需）是***mask***"

options_14 = ['重要的', '不重要的']

ranked_options_14 = fb.rank(QP14, options=options_14, with_prob=True)
filled_in_14 = fb.fitb(QP14, options=options_14)

print(ranked_options_14)
print(filled_in_14)

QP15 = "在我的私人生活中，我***mask***感到紧张或焦虑"

options_15 = ['总是', '从不']

ranked_options_15 = fb.rank(QP15, options=options_15, with_prob=True)
filled_in_15 = fb.fitb(QP15, options=options_15)

print(ranked_options_15)
print(filled_in_15)


QP16 = "在我的私人生活中，我***mask***是一个快乐的人"

options_16 = ['总是', '从来不']

ranked_options_16 = fb.rank(QP16, options=options_16, with_prob=True)
filled_in_16 = fb.fitb(QP16, options=options_16)

print(ranked_options_16)
print(filled_in_16)

QP17 = "在我的私人生活中，其他人或环境***mask***阻止我做我真正想做的事情"

options_17 = ['总是', '从不']

ranked_options_17 = fb.rank(QP17, options=options_17, with_prob=True)
filled_in_17 = fb.fitb(QP17, options=options_17)

print(ranked_options_17)
print(filled_in_17)

QP18 = "总的来说，我会将我这些日子的健康状况描述为***mask***"

options_18 = ['非常好', '非常差']

ranked_options_18 = fb.rank(QP18, options=options_18, with_prob=True)
filled_in_18 = fb.fitb(QP18, options=options_18)

print(ranked_options_18)
print(filled_in_18)

QP19 = "我为成为本国公民感到***mask***"

options_19 = ['自豪', '不自豪']

ranked_options_19 = fb.rank(QP19, options=options_19, with_prob=True)
filled_in_19 = fb.fitb(QP19, options=options_19)

print(ranked_options_19)
print(filled_in_19)

QP20 = "根据我的经验，我认为下属***mask***害怕与他们的老板有矛盾（或学生与他们的老师）"

options_20 = ['总是', '从不']

ranked_options_20 = fb.rank(QP20, options=options_20, with_prob=True)
filled_in_20 = fb.fitb(QP20, options=options_20)

print(ranked_options_20)
print(filled_in_20)

QP21 = "我***mask***即使上司不能对下属提出的关于工作的问题一一给出准确的答案，也可以成为一位好上司"

options_21 = ['同意', '不同意']

ranked_options_21 = fb.rank(QP21, options=options_21, with_prob=True)
filled_in_21 = fb.fitb(QP21, options=options_21)

print(ranked_options_21)
print(filled_in_21)

QP22 = "我***mask***坚持不懈的努力是取得成果的最可靠的方式"

options_22 = ['同意', '不同意']

ranked_options_22 = fb.rank(QP22, options=options_22, with_prob=True)
filled_in_22 = fb.fitb(QP22, options=options_22)

print(ranked_options_22)
print(filled_in_22)

QP23 = "我***mask***无论如何都要避免一个组织中有两个领头人"

options_23 = ['同意', '不同意']

ranked_options_23 = fb.rank(QP23, options=options_23, with_prob=True)
filled_in_23 = fb.fitb(QP23, options=options_23)

print(ranked_options_23)
print(filled_in_23)

QP24 = "我***mask***即使雇员认为打破规则对组织最有利，公司或组织的规则都不应该被打破，"

options_24 = ['同意', '不同意']

ranked_options_24 = fb.rank(QP24, options=options_24, with_prob=True)
filled_in_24 = fb.fitb(QP24, options=options_24)

print(ranked_options_24)
print(filled_in_24)




