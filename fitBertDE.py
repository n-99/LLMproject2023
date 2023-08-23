# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:33:26 2023

@author: yuyue
"""

from fitbert import FitBert


# currently supported models: bert-large-uncased and distilbert-base-uncased
# this takes a while and loads a whole big BERT into memory

fb = FitBert()

QP1 = "Ausreichend Zeit für mein persönliches oder häusliches Leben zu haben, ist ***mask***"

options_1 = ['wichtig', 'unwichtig']

ranked_options_1 = fb.rank(QP1, options=options_1, with_prob=True)
filled_in_1 = fb.fitb(QP1, options=options_1)

print(ranked_options_1)
print(filled_in_1)

QP2 = "Einen Vorgesetzten (direkten Vorgesetzten), den ich respektieren kann, ist ***mask***"

options_2 = ['wichtig', 'unwichtig']

ranked_options_2 = fb.rank(QP2, options=options_2, with_prob=True)
filled_in_2 = fb.fitb(QP2, options=options_2)

print(ranked_options_2)
print(filled_in_2)

QP3 = "Anerkennung für gute Leistungen zu erhalten, ist ***mask***"

options_3 = ['wichtig', 'unwichtig']

ranked_options_3 = fb.rank(QP3, options=options_3, with_prob=True)
filled_in_3 = fb.fitb(QP3, options=options_3)

print(ranked_options_3)
print(filled_in_3)

QP4 = "Sicherheit der Anstellung zu haben, ist ***mask***"

options_4 = ['wichtig', 'unwichtig']

ranked_options_4 = fb.rank(QP4, options=options_4, with_prob=True)
filled_in_4 = fb.fitb(QP4, options=options_4)

print(ranked_options_4)
print(filled_in_4)

QP5 = "Mit angenehmen Kollegen zusammenzuarbeiten, ist ***mask***"

options_5 = ['wichtig', 'unwichtig']

ranked_options_5 = fb.rank(QP5, options=options_5, with_prob=True)
filled_in_5 = fb.fitb(QP5, options=options_5)

print(ranked_options_5)
print(filled_in_5)

QP6 = "Arbeit zu erledigen, die interessant ist, ist ***mask***"

options_6 = ['wichtig', 'unwichtig']

ranked_options_6 = fb.rank(QP6, options=options_6, with_prob=True)
filled_in_6 = fb.fitb(QP6, options=options_6)

print(ranked_options_6)
print(filled_in_6)


QP7 = "Von meinem Chef bei Entscheidungen, die meine Arbeit betreffen, konsultiert zu werden, ist ***mask***"

options_7 = ['wichtig', 'unwichtig']

ranked_options_7 = fb.rank(QP7, options=options_7, with_prob=True)
filled_in_7 = fb.fitb(QP7, options=options_7)

print(ranked_options_7)
print(filled_in_7)

QP8 = "In einer wünschenswerten Gegend zu leben, ist ***mask***"

options_8 = ['wichtig', 'unwichtig']

ranked_options_8 = fb.rank(QP8, options=options_8, with_prob=True)
filled_in_8 = fb.fitb(QP8, options=options_8)

print(ranked_options_8)
print(filled_in_8)

QP9 = "Einen von meiner Familie und meinen Freunden respektierten Job zu haben, ist ***mask***"

options_9 = ['wichtig', 'unwichtig']

ranked_options_9 = fb.rank(QP9, options=options_9, with_prob=True)
filled_in_9 = fb.fitb(QP9, options=options_9)

print(ranked_options_9)
print(filled_in_9)

QP10 = "Chancen auf Beförderung zu haben, ist ***mask***"

options_10 = ['wichtig', 'unwichtig']

ranked_options_10 = fb.rank(QP10, options=options_10, with_prob=True)
filled_in_10 = fb.fitb(QP10, options=options_10)

print(ranked_options_10)
print(filled_in_10)

QP11 = "In meinem Privatleben denke ich, dass es ***mask*** ist, Zeit für Spaß freizuhalten"

options_11 = ['wichtig', 'unwichtig']

ranked_options_11 = fb.rank(QP11, options=options_11, with_prob=True)
filled_in_11 = fb.fitb(QP11, options=options_11)

print(ranked_options_11)
print(filled_in_11)

QP12 = "In meinem Privatleben denke ich, dass Genügsamkeit ***mask*** ist"

options_12 = ['wichtig', 'unwichtig']

ranked_options_12 = fb.rank(QP12, options=options_12, with_prob=True)
filled_in_12 = fb.fitb(QP12, options=options_12)

print(ranked_options_12)
print(filled_in_12)

QP13 = "In meinem Privatleben denke ich, dass es ***mask*** ist, einem Freund einen Dienst zu erweisen"

options_13 = ['wichtig', 'unwichtig']

ranked_options_13 = fb.rank(QP13, options=options_13, with_prob=True)
filled_in_13 = fb.fitb(QP13, options=options_13)

print(ranked_options_13)
print(filled_in_13)

QP14 = "In meinem Privatleben denke ich, sparsam zu sein (nicht mehr auszugeben, als nötig), ist ***mask***"

options_14 = ['wichtig', 'unwichtig']

ranked_options_14 = fb.rank(QP14, options=options_14, with_prob=True)
filled_in_14 = fb.fitb(QP14, options=options_14)

print(ranked_options_14)
print(filled_in_14)

QP15 = "In meinem Privatleben fühle ich mich ***mask*** nervös oder angespannt"

options_15 = ['immer', 'nie']

ranked_options_15 = fb.rank(QP15, options=options_15, with_prob=True)
filled_in_15 = fb.fitb(QP15, options=options_15)

print(ranked_options_15)
print(filled_in_15)

QP16 = "In meinem Privatleben bin ich ***mask*** eine glückliche Person"

options_16 = ['immer', 'nie']

ranked_options_16 = fb.rank(QP16, options=options_16, with_prob=True)
filled_in_16 = fb.fitb(QP16, options=options_16)

print(ranked_options_16)
print(filled_in_16)

QP17 = "In meinem Privatleben hindern mich andere Menschen oder Umstände ***mask*** daran, zu tun, was ich wirklich tun möchte"

options_17 = ['immer', 'nie']

ranked_options_17 = fb.rank(QP17, options=options_17, with_prob=True)
filled_in_17 = fb.fitb(QP17, options=options_17)

print(ranked_options_17)
print(filled_in_17)

QP18 = "Alles in allem würde ich meinen Gesundheitszustand in diesen Tagen als ***mask*** beschreiben"

options_18 = ['sehr gut', 'sehr schlecht']

ranked_options_18 = fb.rank(QP18, options=options_18, with_prob=True)
filled_in_18 = fb.fitb(QP18, options=options_18)

print(ranked_options_18)
print(filled_in_18)


QP19 = "Ich bin ***mask***, Bürger meines Landes zu sein"

options_19 = ['stolz', 'nicht stolz']

ranked_options_19 = fb.rank(QP19, options=options_19, with_prob=True)
filled_in_19 = fb.fitb(QP19, options=options_19)

print(ranked_options_19)
print(filled_in_19)

QP20 = "In meiner Erfahrung denke ich, dass Untergebene ***mask*** Angst haben, ihren Vorgesetzten zu widersprechen (oder Schüler ihren Lehrern)"

options_20 = ['immer', 'nie']

ranked_options_20 = fb.rank(QP20, options=options_20, with_prob=True)
filled_in_20 = fb.fitb(QP20, options=options_20)

print(ranked_options_20)
print(filled_in_20)

QP21 = "Ich ***mask***, dass man ein guter Manager sein kann, ohne auf jede Frage eine genaue Antwort zu haben, die ein Untergebener zu seiner oder ihrer Arbeit stellen könnte"

options_21 = ['zustimmen', 'nicht zustimmen']

ranked_options_21 = fb.rank(QP21, options=options_21, with_prob=True)
filled_in_21 = fb.fitb(QP21, options=options_21, delemmatize=True)

print(ranked_options_21)
print(filled_in_21)

QP22 = "Ich ***mask***, dass hartnäckige Bemühungen der sicherste Weg zu Ergebnissen sind"

options_22 = ['zustimmen', 'nicht zustimmen']

ranked_options_22 = fb.rank(QP22, options=options_22, with_prob=True)
filled_in_22 = fb.fitb(QP22, options=options_22, delemmatize=True)

print(ranked_options_22)
print(filled_in_22)

QP23 = "Ich ***mask***, dass eine Organisationsstruktur, bei der bestimmte Untergebene zwei Vorgesetzte haben, um jeden Preis vermieden werden sollte"

options_23 = ['zustimmen', 'nicht zustimmen']

ranked_options_23 = fb.rank(QP23, options=options_23, with_prob=True)
filled_in_23 = fb.fitb(QP23, options=options_23, delemmatize=True)

print(ranked_options_23)
print(filled_in_23)

QP24 = "Ich ***mask***, dass die Regeln eines Unternehmens oder einer Organisation nicht gebrochen werden sollten, nicht einmal wenn ein Mitarbeiter denkt, dass das Brechen der Regel im besten Interesse der Organisation wäre"

options_24 = ['zustimmen', 'nicht zustimmen']

ranked_options_24 = fb.rank(QP24, options=options_24, with_prob=True)
filled_in_24 = fb.fitb(QP24, options=options_24, delemmatize=True)

print(ranked_options_24)
print(filled_in_24)
