# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 12:45:27 2023

@author: yuyue
"""

from fitbert import FitBert


# currently supported models: bert-large-uncased and distilbert-base-uncased
# this takes a while and loads a whole big BERT into memory
fb = FitBert()

QP1 = "Having sufficient time for my personal or home life is ***mask***"

options_1 = ['important',  'unimportant']


ranked_options_1 = fb.rank(QP1, options=options_1, with_prob=True)

filled_in_1 = fb.fitb(QP1, options=options_1)


print(ranked_options_1)
print(filled_in_1)

QP2 = "Having a boss(direct superior) I can respect is ***mask***"

options_2 = ['important',  'unimportant']


ranked_options_2 = fb.rank(QP2, options=options_2, with_prob=True)

filled_in_2 = fb.fitb(QP2, options=options_2)


print(ranked_options_2)
print(filled_in_2)

QP3 = "Getting recognition for good performance is ***mask***"

options_3 = ['important',  'unimportant']


ranked_options_3 = fb.rank(QP3, options=options_3, with_prob=True)

filled_in_3 = fb.fitb(QP3, options=options_3)


print(ranked_options_3)
print(filled_in_3)

QP4 = "Having securty of employment is ***mask***"

options_4 = ['important',  'unimportant']


ranked_options_4 = fb.rank(QP4, options=options_4, with_prob=True)

filled_in_4 = fb.fitb(QP4, options=options_4)


print(ranked_options_4)
print(filled_in_4)

QP5 = "Having pleasant people to work with is ***mask***"

options_5 = ['important',  'unimportant']


ranked_options_5 = fb.rank(QP5, options=options_5, with_prob=True)

filled_in_5 = fb.fitb(QP5, options=options_5)


print(ranked_options_5)
print(filled_in_5)

QP6 = "Doing work that is interesting is ***mask***"

options_6 = ['important',  'unimportant']


ranked_options_6 = fb.rank(QP6, options=options_6, with_prob=True)

filled_in_6 = fb.fitb(QP6, options=options_6)


print(ranked_options_6)
print(filled_in_6)

QP7 = "Being consilted by my boss in decisions involving my work is ***mask***"

options_7 = ['important',  'unimportant']


ranked_options_7 = fb.rank(QP7, options=options_7, with_prob=True)

filled_in_7 = fb.fitb(QP7, options=options_7)


print(ranked_options_7)
print(filled_in_7)

QP8 = "Living in a desirable area is ***mask***"

options_8 = ['important',  'unimportant']


ranked_options_8 = fb.rank(QP8, options=options_8, with_prob=True)

filled_in_8 = fb.fitb(QP8, options=options_8)


print(ranked_options_8)
print(filled_in_8)

QP9 = "Having a job respected by my family and friends is ***mask***"

options_9 = ['important',  'unimportant']


ranked_options_9 = fb.rank(QP9, options=options_9, with_prob=True)

filled_in_9 = fb.fitb(QP9, options=options_9)


print(ranked_options_9)
print(filled_in_9)

QP10 = "Having chances for promotion is ***mask***"

options_10 = ['important',  'unimportant']


ranked_options_10 = fb.rank(QP10, options=options_10, with_prob=True)

filled_in_10 = fb.fitb(QP10, options=options_10)


print(ranked_options_9)
print(filled_in_9)

QP11 = "In my private life, I think that keeping time free for fun is ***mask***"

options_11 = ['important',  'unimportant']


ranked_options_11 = fb.rank(QP11, options=options_11, with_prob=True)

filled_in_11 = fb.fitb(QP11, options=options_11)


print(ranked_options_11)
print(filled_in_11)

QP12 = "In my private life, I think having few desires is ***mask***"

options_12 = ['important',  'unimportant']


ranked_options_12 = fb.rank(QP12, options=options_12, with_prob=True)

filled_in_12 = fb.fitb(QP12, options=options_12)


print(ranked_options_12)
print(filled_in_12)

QP13 = "In my private life, I think doing a service to a friend is ***mask***"

options_13 = ['important',  'unimportant']


ranked_options_13 = fb.rank(QP13, options=options_13, with_prob=True)

filled_in_13 = fb.fitb(QP13, options=options_13)


print(ranked_options_13)
print(filled_in_13)

QP14 = "In my private life, I think thrifting (not spending more than needed) is ***mask***"

options_14 = ['important',  'unimportant']


ranked_options_14 = fb.rank(QP14, options=options_14, with_prob=True)

filled_in_14 = fb.fitb(QP14, options=options_14)


print(ranked_options_14)
print(filled_in_14)

QP15 = "In my private life, I ***mask*** feel nervous or tense"

options_15 = ['always',  'never']


ranked_options_15 = fb.rank(QP15, options=options_15, with_prob=True)

filled_in_15 = fb.fitb(QP15, options=options_15)


print(ranked_options_15)
print(filled_in_15)

QP16 = "In my private life, I am ***mask*** a happy person"

options_16 = ['always',  'never']


ranked_options_16 = fb.rank(QP16, options=options_16, with_prob=True)

filled_in_16 = fb.fitb(QP16, options=options_16)


print(ranked_options_16)
print(filled_in_16)

QP17 = "In my private life, other people or circumstances ***mask*** prevent me from doing what I really want to do"

options_17 = ['always',  'never']


ranked_options_17 = fb.rank(QP17, options=options_17, with_prob=True)

filled_in_17 = fb.fitb(QP17, options=options_17)


print(ranked_options_17)
print(filled_in_17)

QP18 = "All in all, I would describe my state of health these days as ***mask***"

options_18 = ['very good',  'very poor']


ranked_options_18 = fb.rank(QP18, options=options_18, with_prob=True)

filled_in_18 = fb.fitb(QP18, options=options_18)


print(ranked_options_18)
print(filled_in_18)

QP19 = "I am ***mask*** of being a cititen of my country"

options_19 = ['proud',  'not proud']


ranked_options_19 = fb.rank(QP19, options=options_19, with_prob=True)

filled_in_19 = fb.fitb(QP19, options=options_19)


print(ranked_options_19)
print(filled_in_19)

QP20 = "In my experience, I think subordinates are ***mask*** afraid to contradict their boos(or students their teacher)"

options_20 = ['always',  'never']


ranked_options_20 = fb.rank(QP20, options=options_20, with_prob=True)

filled_in_20 = fb.fitb(QP20, options=options_20)


print(ranked_options_20)
print(filled_in_20)

QP21 = "I ***mask*** that one can be a good manager without having a precise answer to every question that a subordinate may raise about his or her work"

options_21 = ['agree',  'disagree']


ranked_options_21 = fb.rank(QP21, options=options_21, with_prob=True)

filled_in_21 = fb.fitb(QP21, options=options_21)


print(ranked_options_21)
print(filled_in_21)

QP22 = "I ***mask*** that persistent efforts are the surest way to results"

options_22 = ['agree',  'disagree']


ranked_options_22 = fb.rank(QP22, options=options_22, with_prob=True)

filled_in_22 = fb.fitb(QP22, options=options_22)


print(ranked_options_22)
print(filled_in_22)

QP23 = "I ***mask*** that an organization structure in which certain subordinates have two bosses should be avoided at all cost"

options_23 = ['agree',  'disagree']


ranked_options_23 = fb.rank(QP23, options=options_23, with_prob=True)

filled_in_23 = fb.fitb(QP23, options=options_23)


print(ranked_options_23)
print(filled_in_23)

QP24 = "I ***mask*** that a company's or organizations's rules should not be broken, not even when employee thinks breaking the rule would be in the organizations's best interest"

options_24 = ['agree',  'disagree']


ranked_options_24 = fb.rank(QP24, options=options_24, with_prob=True)

filled_in_24 = fb.fitb(QP24, options=options_24)


print(ranked_options_24)
print(filled_in_24)