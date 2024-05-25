from flask import Blueprint, render_template, request, url_for
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.io import to_html
from .resources import *

bp = Blueprint('routes',__name__,url_prefix='/')


@bp.route('/', methods=['GET','POST'])
def home():
    #need to set values to input form values
    if request.method == 'POST':
        loan_amount = float(request.form['principal'])
        rate = float(request.form['annual_rate'])
        years = float(request.form['years'])
        mortgage = Mortgage(loan_amount,rate,years)
        repayments = mortgage.simulate_repayments()

        month = []
        monthly_payment = []
        principal_payment = []
        interest = []
        balance = []
        paid = []

        for i in range(len(repayments)):
            month.append(repayments[i][0])
            monthly_payment.append(repayments[i][1])
            principal_payment.append(repayments[i][2])
            interest.append(repayments[i][3])
            balance.append(repayments[i][4])
            paid.append(repayments[i][5])

        fig = make_subplots(specs=[[{'secondary_y':True}]])
        fig.add_trace(
            go.Scatter(x=month,y=balance,name='Balance', line=dict(dash='dash')), secondary_y=True
            )
        fig.add_trace(
            go.Scatter(x=month,y=paid,name='Cumulative Payments',line=dict(dash='dash',color='black')), secondary_y=True,
            )
        fig.add_traces(data=[
            go.Scatter(x=month, y=principal_payment, name='Principal Payment'),
            go.Scatter(x=month, y=interest, name='Interest')
        ],rows=1,cols=1)

        html = to_html(fig, full_html=False)


        total_cost = round(max(paid),2)
        total = f"The total cost is {total_cost}"

        return render_template('mortgage.html', content1=total,fig1=html)
    
    
    
    else:
        loan_amount = 300000
        rate = 5.0
        years = 25
        mortgage = Mortgage(loan_amount,rate,years)
        repayments = mortgage.simulate_repayments()

        month = []
        monthly_payment = []
        principal_payment = []
        interest = []
        balance = []
        paid = []

        for i in range(len(repayments)):
            month.append(repayments[i][0])
            monthly_payment.append(repayments[i][1])
            principal_payment.append(repayments[i][2])
            interest.append(repayments[i][3])
            balance.append(repayments[i][4])
            paid.append(repayments[i][5])

        fig = make_subplots(specs=[[{'secondary_y':True}]])
        fig.add_trace(
            go.Scatter(x=month,y=balance,name='Balance', line=dict(dash='dash')), secondary_y=True
            )
        fig.add_trace(
            go.Scatter(x=month,y=paid,name='Cumulative Payments',line=dict(dash='dash',color='black')), secondary_y=True,
            )
        fig.add_traces(data=[
            go.Scatter(x=month, y=principal_payment, name='Principal Payment'),
            go.Scatter(x=month, y=interest, name='Interest')
        ],rows=1,cols=1)

        html = to_html(fig, full_html=False)


        total_cost = round(max(paid),2)
        total = f"The total cost is {total_cost}"

        return render_template('mortgage.html', content1=total,fig1=html)


@bp.route('/mortgage')
def mortgage():
    #set starting values
    principal = 300000
    interest = 1.01
    period = list(range(0,100))
    value = [principal]
    payments = 1200
    payment_list = [payments]
    for i in range(0,99):
        if principal > 0:
            i = principal * interest - payments
            principal = i
            payments += payments
            payment_list.append(payments)
            value.append(i)
        else:
            pass
    fig = go.Figure(data=[
        go.Scatter(x=period, y=value, name='Loan'),
        #go.Scatter(x=period, y=payment_list, name='Payments')
    ])
    html = to_html(fig, full_html=False)
    return html

@bp.route('/mortgage2')
def mortgage2():
    mortgage = Mortgage(300000,3.5,30)
    repayments = mortgage.simulate_repayments()

    month = []
    monthly_payment = []
    principal_payment = []
    interest = []
    balance = []
    paid = []

    for i in range(len(repayments)):
        month.append(repayments[i][0])
        monthly_payment.append(repayments[i][1])
        principal_payment.append(repayments[i][2])
        interest.append(repayments[i][3])
        balance.append(repayments[i][4])
        paid.append(repayments[i][5])

    fig = make_subplots(specs=[[{'secondary_y':True}]])
    fig.add_trace(
        go.Scatter(x=month,y=balance,name='Balance', line=dict(dash='dash')), secondary_y=True
        )
    fig.add_trace(
        go.Scatter(x=month,y=paid,name='Cumulative Payments',line=dict(dash='dash',color='black')), secondary_y=True,
        )
    fig.add_traces(data=[
        go.Scatter(x=month, y=principal_payment, name='Principal Payment'),
        go.Scatter(x=month, y=interest, name='Interest')
    ],rows=1,cols=1)

    html = to_html(fig)


    return html