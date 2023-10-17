#install and open packages
install.packages('car')
library(car)

install.packages('agricolae')
library(agricolae)

install.packages('multcompView')
library(multcompView)

# Assuming data is your DataFrame and 'Seed_size' is the column you want to compare among different regions.
mod <- lm(Seed_size ~ Region, data = data)

# Conduct ANOVA with Type II SS
anova_res <- Anova(mod, type="II")

# Print the results
print(summary(anova_res))

# If the ANOVA is significant, we can conduct the LSD test
if(anova_res$`Pr(>F)`[1] < 0.05){
  print("ANOVA is significant")
  tukey_result <- TukeyHSD(aov(mod))
  # extract the comparison matrix
  comparisons <- tukey_result$Region[,4]
  # this gives you the letter groupings
  print(multcompLetters(comparisons)$Letters)
} else {
  print("ANOVA is not significant.")
}
