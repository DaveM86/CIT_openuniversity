import math
import datetime as dt
import calendar
import numpy as np
import pandas as pd
import plotly.graph_objects as go


def addMonths(inpDt, mnths):
  tmpMnth = inpDt.month - 1 + mnths

  # Add floor((input month - 1 + k)/12) to input year component to get result year component
  resYr = inpDt.year + tmpMnth // 12

  # Result month component would be (input month - 1 + k)%12 + 1
  resMnth = tmpMnth % 12 + 1

  # Result day component would be minimum of input date component and max date of the result month (For example we cant have day component as 30 in February month)
  # Maximum date in a month can be found using the calendar module monthrange function as shown below
  resDay = min(inpDt.day, calendar.monthrange(resYr,resMnth)[1])

  # construct result datetime with the components derived above
  resDt = dt.datetime(resYr, resMnth, resDay, inpDt.hour, inpDt.minute, inpDt.second, inpDt.microsecond)

  return resDt





p = 180000
x = 601
r = 1+((1.64/100)/12)
n = 0


balance = []
dates = []
house_value = [200000]
value_owned = []


while n < 385:

	balance.append(p*(r**n)-(x*((1-(r**n))/(1-r))))
	dates.append(addMonths(dt.datetime(2021,11,16,3,20,6), n))
	house_value.append(house_value[-1] + house_value[-1]*((1.2/100)/12))
	value_owned.append(house_value[-2] - balance[-1])

	n += 1

dic_oustanding = dict(zip(dates, balance))

df_outstanding = pd.DataFrame(list(dic_oustanding.items()))

dic_value = dict(zip(dates, house_value))

df_value = pd.DataFrame(list(dic_value.items()))

dic_owned = dict(zip(dates, value_owned))

df_owned = pd.DataFrame(list(dic_owned.items()))

outstanding_trace = go.Scatter(x=df_outstanding[0], y=df_outstanding[1], name='Outstanding Balance')

value_trace = go.Scatter(x=df_value[0], y=df_value[1], name='House Value')

owned_trace = go.Scatter(x=df_owned[0],y=df_owned[1], name='Value Owned')

data = [outstanding_trace, value_trace, owned_trace]

layout = go.Layout(title='Burnbank Kingston', xaxis={'title':{'text':'Date'}}, yaxis={'title':{'text':'Value'}})

fig = go.Figure(data=data)

fig.show()