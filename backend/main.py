#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : main.py
@Time    : 2025/12/23 16:20
@Author  : jijunye
@Desc    : 
"""
from fastapi import FastAPI
from api import abs, bond, stock

app = FastAPI()

app.include_router(abs.router, prefix="/api")
app.include_router(bond.router, prefix="/api")
app.include_router(stock.router, prefix="/api")