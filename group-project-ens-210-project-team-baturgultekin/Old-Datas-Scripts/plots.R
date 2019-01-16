install.packages("ggplot2")
install.packages("dplyr")
install.packages("tidyr")
library(ggplot2)
library(dplyr)
library(tidyr)

d <- read.table('identity.txt', sep='\t', h=T)

pdf("conserved_area_identity.pdf", width=16, height=9)

head(d)

names(d) <- c('Pos', 'AA', 'Cons_Grad')

head(d)

d$group <- as.numeric(cut(d$Pos, 3))

ggplot(data=d, aes(x=Pos , y=Cons_Grad, color= Cons_Grad)) +
  xlab("Position")+ ylab("Identity")+ geom_point()+ geom_line(aes(color=Cons_Grad)) +
  scale_color_gradient(low="Orange", high = "Blue") + 
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1)) + 
  theme(legend.title = element_text(colour="Orange", size=11, face="italic")) +
  facet_wrap(~group, ncol = 1, scales = "free_x")


dev.off()

