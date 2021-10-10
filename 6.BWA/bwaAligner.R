setRepositories(ind=1:7)

library(tidyverse)
library(doParallel)
library(foreach)
#library(argparse)

setwd('/disk10/bijh/1.REF_Research/6.BWA/')
#args = commandArgs(trailingOnly=TRUE)
#dir <- args[1]

dir <- "/disk10/bijh/1.REF_Research/6.BWA/0.index"
file_list <- list.files(path=dir, pattern = "*fa$", full.names = TRUE)
base_list <- list.files(path=dir, pattern = "*fa$",full.names = FALSE)
faName <- strsplit(base_list,"[.]")
SAM_list <- sapply(faName, function(x){x[1]}, simplify = T)

sample_list <- list.files(
            path = "/disk10/bijh/1.REF_Research/3.SAMPLE/Coturnix_japonica",
            pattern = "sampled5e-05%*",
            full.names = TRUE
            )

cl <- makeCluster(60)
registerDoParallel(cl)

innerLoop <- 31
outLoop <- length(file_list)/innerLoop
parallelList <- vector(mode = "list", length = outLoop)
index <- 1
for( i in 1:outLoop){
  commends <- c()
  for( j in 1:innerLoop){
    commends <- append(commends, str_c(
      "bwa mem ", file_list[index], " ",
      sample_list[1], " ", sample_list[2], " > ./1.SAM/",
      SAM_list[index], ".sam"
      )
    )
    index <- index + 1
  }
  parallelList[[i]] <- commends
}

system.time(for(i in 1:outLoop){
  foreach(j = 1:innerLoop)%dopar%{
    system(parallelList[[i]][j])
  }
})
