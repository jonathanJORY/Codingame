"""Determiner si la suite est arithmetique ou geometrique, et donner le terme suivant"""
I = input
n, a, b, c, *D = map(int, [I()]+input().split())
I([int(a*(b/a)**n), a+(b-a)*n][c-b == b-a])