install.packages("ggplot2")
install.packages("dplyr")
install.packages("tidyr")
library(ggplot2)
library(dplyr)
library(tidyr)

d <- read.table('identity.txt', sep='\t', h=T)
f <- read.table('numOfGaps.txt', sep='\t', h=F)

pdf ("conserved_area_identity.pdf", width=16, height=9)

head(d)

names(d) <- c('Pos', 'AA', 'value')
names(f) <- c('Pos', 'value')

f$AA = d$AA

head(d)
head(f)
f$value = (230- f$value)/230

d$cat = "Identity" 
f$cat = "Non-Gap"
m = rbind(d, f)

m$group <- as.numeric(cut(m$Pos, 4))

ggplot(data=m, aes(x=Pos , y=value, color= cat)) +
  xlab("Position")+ ylab("Identity")+ geom_point()+ geom_line(aes(color=cat)) +
  #scale_color_gradient(low="Orange", high = "Blue") + 
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1)) + 
  theme(legend.title = element_text(colour="Red", size=11, face="italic")) +
  facet_wrap(~group, ncol = 1, scales = "free_x")


dev.off()