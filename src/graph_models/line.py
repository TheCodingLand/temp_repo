from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel


class Series(BaseModel):
    name: str
    data: List[int]


class Chart(BaseModel):
    height: int
    type: str


class ForecastDataPoints(BaseModel):
    count: int


class Stroke(BaseModel):
    width: int
    curve: str


class Xaxis(BaseModel):
    type: str
    categories: List[str]
    tickAmount: int
    labels: Dict[str, Any]


class Style(BaseModel):
    fontSize: str
    color: str


class Title(BaseModel):
    text: str
    align: str
    style: Style


class Gradient(BaseModel):
    shade: str
    gradientToColors: List[str]
    shadeIntensity: int
    type: str
    opacityFrom: int
    opacityTo: int
    stops: List[int]


class Fill(BaseModel):
    type: str
    gradient: Gradient


class Yaxis(BaseModel):
    min: int
    max: int


class Model(BaseModel):
    series: List[Series]
    chart: Chart
    forecastDataPoints: ForecastDataPoints
    stroke: Stroke
    xaxis: Xaxis
    title: Title
    fill: Fill
    yaxis: Yaxis

if __name__ == "__main__":

    m = Model(series=[
            Series(data=[10,15,8,25],name="Executions"),
            Series(data=[15,25,12,20], name="total duration")
            ],
            chart=Chart(height=250,type='line')
            
            )