library(ggplot2)
library(ggpubr)
library(RColorBrewer)

input.sam <- snakemake@input[[1]]

df <- read.table(input.sam, sep = "\t", header = TRUE)

plt <- ggplot(df, aes(y=read_length, x=zmw, color=sample)) + 
        geom_point()


ggsave(snakemake@output[[1]], plt)

