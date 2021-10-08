setRepositories(ind=1:7)

library(tidyverse)
library(doParallel)
library(foreach)

#args = commandArgs(trailingOnly=TRUE)
#dir <- args[1]

dir <- "/disk10/bijh/1.REF_Research/6.BWA/0.index/"
file_list <- list.files(path=dir, pattern = "*fa$", full.names = TRUE)

cl <- makeCluster(40)
registerDoParallel(cl)

innerLoop <- 10
outLoop <- length(file_list)/innerLoop
parallelList <- vector(mode = "list", length = outLoop)
index <- 1
for( i in 1:outLoop){
  commends <- c()
  for( j in 1:innerLoop){
    commends <- append(commends, str_c("bwa index ", file_list[index]))
    index <- index + 1
  }
  parallelList[[i]] <- commends
}

system.time(for(i in 1:outLoop){
  foreach(j = 1:innerLoop)%dopar%{
    system(parallelList[[i]][j])
  }
})
