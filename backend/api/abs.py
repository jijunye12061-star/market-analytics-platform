#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : abs.py
@Time    : 2025/12/23 16:21
@Author  : jijunye
@Desc    : 
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/report")
async def get_report():
    # 生成日期序列
    start_date = datetime(2025, 11, 17)
    dates = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(5)]

    # 模拟收益率数据（参考你的图片）
    data = {
        "title": "ABS市场周报",
        "period": "2025.11.17-2025.11.21",
        "dates": dates,
        "series": [
            {
                "name": "国债1年期",
                "data": [1.85, 1.83, 1.82, 1.81, 1.84]
            },
            {
                "name": "国债3年期",
                "data": [1.95, 1.93, 1.92, 1.91, 1.94]
            },
            {
                "name": "国债5年期",
                "data": [2.10, 2.08, 2.07, 2.06, 2.09]
            },
            {
                "name": "国债10年期",
                "data": [2.35, 2.33, 2.32, 2.31, 2.34]
            },
            {
                "name": "国开债3年期",
                "data": [2.05, 2.03, 2.02, 2.01, 2.04]
            },
            {
                "name": "国开债5年期",
                "data": [2.25, 2.23, 2.22, 2.21, 2.24]
            }
        ],
        "summary": "上周国债收益率主体震荡，短端和长端均有所下行。上周五全期限国债收益率曲线，曲线与周初相比，后市观望情绪较浓。"
    }

    return data

# 运行：uvicorn backend:app --reload --port 8000