# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kjDZgs2UUih_kkvzt2QodOffpGJm05c9
"""

height = float(input("請輸入你的身高(公尺)"))
weight = float(input("清輸入你的體重(公斤)"))

BMI = weight/(height**2)

print(f"您的BMI是:{BMI:.2f}")