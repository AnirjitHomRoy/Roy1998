#Data
revenue <- c(14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50)
expenses <- c(12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96)

#Solution

  profit<- revenue-expenses
  profit<- round(profit/1000,0)
  tax<- round(0.3*profit,2)
  modprofit<- profit-tax
  profitmargin<- round((modprofit/revenue),2)*100
  mean_pat<-round(mean(modprofit),2)
  modprofit<- round(modprofit/1000,0)
  profitmargin<- round(profitmargin/1000,0)
  profit<- round(profit/1000,0)

rm(good.months)
profit
tax
modprofit
profitmargin

goodmonths<- modprofit>mean_pat
goodmonths
badmonths<- modprofit<mean_pat
badmonths
bestmonth<- modprofit==max(modprofit)
bestmonth
worstmonth<- modprofit==min(modprofit)
worstmonth





