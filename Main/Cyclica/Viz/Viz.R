library(tidyr)
library(dplyr)
library(scales)
library(ggplot2)

df_with4 <- read.csv("normalized4.csv", header = T)
head(df_with4)
dim(df_with4)

myPlot <- ggplot(df_with4, aes(x = factor(y_Ligand), fill = factor(y_Ligand))) + 
  geom_bar() + 
  labs(x = "Binding Status", y = "Frequency",
       title = "Bar Chart of Binding Status",
       subtitle = "Total observations: 497166") +
  scale_fill_discrete(name = "Binding Status", labels = c("Not Binding", "Binding")) + 
  scale_y_continuous(labels = comma) +
  theme(legend.position = "bottom", axis.text.x = element_blank(),
        axis.ticks.x = element_blank(),
        plot.title = element_text(size = 20, face = "bold", hjust = 0.5),
        plot.subtitle = element_text(size = 10, hjust = 0.2))
myPlot


df_with4_dup <- read.csv("normalized4_dup.csv", header = T)
dim(df_with4_dup)
myPlot_dup <- ggplot(df_with4_dup, aes(x = factor(y_Ligand), fill = factor(y_Ligand))) + 
  geom_bar() + labs(x = "Binding Status", y = "Frequency",
                    title = "Bar Chart of Binding Status",
                    subtitle = "Total observations: 945770") +
  scale_fill_discrete(name = "Binding Status", labels = c("Not Binding", "Binding")) + 
  scale_y_continuous(labels = comma) +
  theme(legend.position = "bottom", axis.text.x = element_blank(),
        axis.ticks.x = element_blank(),
        plot.title = element_text(size = 20, face = "bold", hjust = 0.5),
        plot.subtitle = element_text(size = 10, hjust = 0.2))
myPlot_dup
