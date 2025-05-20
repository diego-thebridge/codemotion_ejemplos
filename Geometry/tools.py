from langchain.agents import tool
import random
import json


@tool
def get_circle_area(radius:float) -> float:
    """ Use this tool to calculate the area of a circle. The input must be a number 
        with the value of the radius"""
    radius_number = float(radius)
    return float(3.1416*radius_number*radius_number)

@tool
def get_square_area(edge:float) -> float:
    """Use this tool to calculate the area of a square. The input must be a number 
       with the value of the edge"""
    edge_number = float(edge)
    return float(edge_number*edge_number)

