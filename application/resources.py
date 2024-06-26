from decimal import Decimal, getcontext

# Set decimal precision globally
getcontext().prec = 50

class Mortgage:
    def __init__(self, principal, annual_rate, years, overpayment):
        if principal <= 0 or annual_rate <= 0 or years <= 0:
            raise ValueError("Principal, annual rate, and years must be greater than zero.")
        self.principal = Decimal(principal)
        self.annual_rate = Decimal(annual_rate)
        self.years = Decimal(years)
        self.monthly_rate = self.annual_rate / Decimal(12 * 100)
        self.total_payments = self.years * Decimal(12)
        self.overpayment = overpayment


    def calculate_monthly_payment(self):
        numerator = self.principal * self.monthly_rate
        denominator = Decimal(1) - (Decimal(1) + self.monthly_rate) ** -self.total_payments
        monthly =  numerator / denominator
        extra = monthly * (Decimal(self.overpayment)/100)
        return monthly + extra
    
    def simulate_repayments(self):
        monthly_payment = self.calculate_monthly_payment()
        balance = self.principal
        accrued_interest = 0
        paid = monthly_payment
        repayment_schedule = []
        #add balance plus interest

        for month in range(1, int(self.total_payments) + 1):
            interest = balance * self.monthly_rate
            balance += interest
            principal_payment = monthly_payment - interest
            interest_payment = monthly_payment - principal_payment
            balance -= (principal_payment + interest_payment)
            accrued_interest += interest - interest_payment
            paid += monthly_payment
            total_owed = balance + accrued_interest

            if balance < 0:
                principal_payment += balance  # Adjust the last payment to bring balance to zero
                balance = Decimal(0)
            
            repayment_schedule.append((month, float(monthly_payment), float(principal_payment), float(interest), float(balance), float(paid), float(accrued_interest), float(total_owed)))

            if balance == 0:
                break

        return repayment_schedule

