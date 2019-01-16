install.packages("ggplot2")
install.packages("dplyr")
library("ggplot2")
library(dplyr)

#Task_1_2
data<- read.table('proopiomelanocortin_CpG.txt', h=F)
names(data) <- c('Positions', 'Ratio_Of_Obs_Exp_CpG')

pdf("task_1_2.pdf")

ggplot(data, aes(x = Positions, y= Ratio_Of_Obs_Exp_CpG)) +
  geom_line(colour="Orange", size = 0.8) + geom_line(colour="Blue", size = 0.2) +
  geom_line (aes(y=0.6), lty=2)

dev.off()

#Task_2_3
data<- read.table('identity.txt', sep='\t', h=F)
names(data) <- c('Positions', 'Identity')

pdf("task_2_3.pdf")

ggplot(data, aes(x = Positions, y= Identity)) +
  geom_point(colour="Orange", size = 1.0) + geom_point(colour="Blue", size = 0.4)

dev.off()

#Task_2_4
data<- read.table('basic.txt', sep='\t', h=F)
names(data) <- c('Positions', 'Conservation_Value')

pdf("task_2_4.pdf")

ggplot(data, aes(x = Positions, y= Conservation_Value)) +
  geom_point(colour="Orange", size = 1.0) + geom_point(colour="Blue", size = 0.4)

dev.off()

# I get some idea from this web-site while coloring the graph http://ggplot.yhathq.com/docs/geom_line.html
# It helped a lot for the syntax of dashed line type http://www.sthda.com/english/wiki/line-types-in-r-lty