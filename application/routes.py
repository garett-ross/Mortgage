from flask import Blueprint, render_template, request
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
        overpayment = float(request.form['overpayment'])
        years = float(request.form['years'])
        mortgage = Mortgage(loan_amount,rate,years, overpayment)
        repayments = mortgage.simulate_repayments()

        month = []
        monthly_payment = []
        principal_payment = []
        interest = []
        balance = []
        paid = []
        accrued_interest = []
        total_owed = []

        for i in range(len(repayments)):
            month.append(repayments[i][0])
            monthly_payment.append(repayments[i][1])
            principal_payment.append(repayments[i][2])
            interest.append(repayments[i][3])
            balance.append(repayments[i][4])
            paid.append(repayments[i][5])
            accrued_interest.append(repayments[i][6])
            total_owed.append(repayments[i][7])

        fig = make_subplots(rows=2, cols=1)
        fig.update_layout(margin={'t':10,'l':0,'b':0,'r':0},yaxis=dict(tickformat=".2f"))
        fig.add_trace(
            go.Scatter(x=month,y=balance,name='Balance', line=dict(dash='dash')), secondary_y=False
            , row=1, col=1)
        fig.add_trace(
            go.Scatter(x=month,y=paid,name='Cumulative Payments',line=dict(dash='dash',color='black')), secondary_y=False,
            row=1, col=1)
        fig.add_traces(data=[
            go.Scatter(x=month, y=principal_payment, name='Principal Payment'),
            go.Scatter(x=month, y=interest, name='Interest Payment')
        ],rows=2,cols=1)
        fig['layout']['xaxis']['title'] = 'Months'
        fig['layout']['xaxis2']['title'] = 'Months'
        fig['layout']['yaxis']['title'] = 'Value'
        fig['layout']['yaxis2']['title'] = 'Value'

        html = to_html(fig, full_html=False)


        total_cost = round(max(paid),2)
        total = f"Total Cost: {total_cost}"
        monthly = f"Monthly Payment: {round(monthly_payment[0],2)}"
        key_data = [total, monthly]

        return render_template('mortgage.html', content1=total,fig1=html, principal=loan_amount, rate=rate, overpayment=overpayment, years=years, ul=key_data)
    
    
    
    else:
        loan_amount = 300000
        rate = 5.0
        years = 25
        overpayment = 0.0
        mortgage = Mortgage(loan_amount,rate,years, overpayment)
        repayments = mortgage.simulate_repayments()

        month = []
        monthly_payment = []
        principal_payment = []
        interest = []
        balance = []
        paid = []
        interest_payment = []
        total_owed = []

        for i in range(len(repayments)):
            month.append(repayments[i][0])
            monthly_payment.append(repayments[i][1])
            principal_payment.append(repayments[i][2])
            interest.append(repayments[i][3])
            balance.append(repayments[i][4])
            paid.append(repayments[i][5])
            interest_payment.append(repayments[i][6])
            total_owed.append(repayments[i][7])

        fig = make_subplots(rows=2, cols=1)
        fig.update_layout(margin={'t':10,'l':0,'b':0,'r':0},yaxis=dict(tickformat=".2f"))
        fig.add_trace(
            go.Scatter(x=month,y=balance,name='Balance', line=dict(dash='dash')), secondary_y=False
            , row=1, col=1)
        fig.add_trace(
            go.Scatter(x=month,y=paid,name='Cumulative Payments',line=dict(dash='dash',color='black')), secondary_y=False,
            row=1, col=1)
        fig.add_traces(data=[
            go.Scatter(x=month, y=principal_payment, name='Principal Payment'),
            go.Scatter(x=month, y=interest, name='Interest Payment')
        ],rows=2,cols=1)
        fig['layout']['xaxis']['title'] = 'Months'
        fig['layout']['xaxis2']['title'] = 'Months'
        fig['layout']['yaxis']['title'] = 'Value'
        fig['layout']['yaxis2']['title'] = 'Value'

        html = to_html(fig, full_html=False)


        total_cost = round(max(paid),2)
        total = f"Total Cost: {total_cost}"
        monthly = f"Monthly Payment: {round(monthly_payment[0],2)}"
        key_data = [total, monthly]

        return render_template('mortgage.html', content1=total,fig1=html, principal=loan_amount, rate=rate, overpayment=overpayment, years=years, ul=key_data)
