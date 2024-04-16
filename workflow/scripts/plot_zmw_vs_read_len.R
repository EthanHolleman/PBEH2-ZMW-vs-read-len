library(ggplot2)
library(ggpubr)
library(RColorBrewer)

input.sam <- snakemake@input[[1]]

df <- read.table(input.sam, sep = "\t", header = TRUE)

plt <- ggplot(df, aes(y=read_length, x=zmw, color=sample)) + 
        geom_point(size=0.01) + 
        facet_wrap(~sample, ncol=1) + 
        scale_color_brewer(palette='Dark2') + 
        theme_pubr() +
        theme(legend.position='None') +
        ylim(0, 3000) +
        labs(x='ZMW number', y='Read length')


ggsave(snakemake@output[[1]], plt, width = 20, height = 8, dpi = 300)

