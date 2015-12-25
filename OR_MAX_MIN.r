libarary(ggplot2)

ggplot(data, aes(x=or, weight=percent))+geom_bar(colour="gray", fill="gray")+ geom_vline(xintercept=1, linetype="dotted", color="black")