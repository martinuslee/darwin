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
summary(data$`Class Label`)
#write.csv(data,file="species_table.csv",quote=FALSE)
Equidae
fishs <- data[which(data$`Class Label` == 'Fish'),]
Laurasiatheria <- data[which(data$`Class Label` == 'Laurasiatheria'),]
Birds <- data[which(data$`Class Label` == 'Birds'),]
Rodents <- data[which(data$`Class Label` == 'Rodents etc.'),]
Reptiles <- data[which(data$`Class Label` == 'Reptiles'),]
OtherMammals  <- data[which(data$`Class Label` == 'Other mammals'),]

view(Laurasiatheria)

# Fish Laurasiatheria Birds Rodents Primates Reptiles Other
# Danio_rerio Sus_scrofa Gallus_gallus Mus_musculus Homo_sapiens Chelydra_serpentina 



