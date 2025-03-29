from django.shortcuts import render
from django.http import JsonResponse
import math
import re

def index(request):
    return render(request, 'index.html')

def calculate(request):
    if request.method == 'POST':
        try:
            import json
            data = json.loads(request.body)
            expression = data.get('expression', '')

            # Replace '√' with 'math.sqrt' and handle square root syntax
            expression = re.sub(r'√\((.*?)\)', r'math.sqrt(\1)', expression)
            expression = re.sub(r'√(\d+)', r'math.sqrt(\1)', expression)

            # Replace '^' with '**' for exponentiation
            expression = expression.replace('^', '**')

            # Handle 'e' for Euler's number
            # Replace standalone 'e' with 'math.e'
            expression = re.sub(r'(?<![\w.])e(?![\w.])', 'math.e', expression)

            # Handle cases like '2e' -> '2*math.e'
            expression = re.sub(r'(\d+)e', r'\1*math.e', expression)

            # Handle cases like 'e2' -> 'math.e*2'
            expression = re.sub(r'e(\d+)', r'math.e*\1', expression)

            # Handle implicit multiplication between parentheses, e.g., (2+3)(2-3) -> (2+3)*(2-3)
            expression = re.sub(r'\)\(', r')*(', expression)

            # Validate the expression to allow only numbers, operators, and parentheses
            if not re.match(r'^[\d+\-*/().%mathsqrt*e ]+$', expression):
                return JsonResponse({'result': 'Error'})

            # Evaluate the mathematical expression safely
            result = eval(expression, {"__builtins__": None}, {"math": math})

            return JsonResponse({'result': result})
        except Exception:
            return JsonResponse({'result': 'Error'})