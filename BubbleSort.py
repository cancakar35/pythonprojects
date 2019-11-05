#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Can Cakar" # instagram.com/cancakar35

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
