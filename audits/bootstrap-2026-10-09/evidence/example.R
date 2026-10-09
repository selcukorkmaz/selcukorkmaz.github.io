library(boot)
prog  <- c(21, 17, 15, 14, 13, 7, 6, 2, 2, -3)
usual <- c(11, 10, 9, 5, 2, 1, 0, -1, -9, -9)
d <- data.frame(fall = c(prog, usual), arm = rep(c("programme", "usual care"), each = 10))

# The difference in means, and its estimated variance (for the bootstrap-t), in one resample
stat <- function(data, i) {
  x <- data[i, ]
  p <- x$fall[x$arm == "programme"]; u <- x$fall[x$arm == "usual care"]
  c(mean(p) - mean(u), var(p) / length(p) + var(u) / length(u))
}
set.seed(2026)
b <- boot(d, stat, R = 9999, strata = factor(d$arm))   # resample within each arm
sd(b$t[, 1])                                            # bootstrap SE: 3.11 (ideal 3.16)
boot.ci(b, type = c("perc", "stud"))                    # percentile 1.5 to 13.6; bootstrap-t 0.59 to 14.41
t.test(prog, usual, var.equal = TRUE)$conf.int          # 0.51 to 14.49

cat("\nRuntime: ",R.version.string,"; boot ",as.character(packageVersion("boot")),"\n")
