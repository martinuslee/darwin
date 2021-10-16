setRepositories(ind=1:7)

library(tidyverse)
setwd('/disk10/bijh/1.REF_Research/')
data <- read_csv('new_species.csv')
data <- data %>% mutate(
  Class = as.factor(Class),
  `Class Label`=as.factor(`Class Label`)
)
summary(data)
str(data)
table(data$`Class Label`)
write.csv(data,file="species_table.csv",quote=FALSE)
