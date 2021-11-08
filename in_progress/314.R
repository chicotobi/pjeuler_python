rm(list=ls())
library(tidyverse)
p <- function(x) {8*x + 2*(250-x)*pi}
a <- function(x) {4*x^2 + 4*2*x*(250-x) + (250-x)^2*pi }

d <- data.frame(x=seq(0,250,0.001)) %>% mutate(p=p(x),a=a(x),ratio=a/p)

%>% ggplot(aes(x,ratio)) + geom_point()
