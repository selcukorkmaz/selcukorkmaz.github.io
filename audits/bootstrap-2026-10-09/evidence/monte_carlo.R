library(boot)
prog  <- c(21, 17, 15, 14, 13, 7, 6, 2, 2, -3); usual <- c(11, 10, 9, 5, 2, 1, 0, -1, -9, -9)
D <- 7.5; se0 <- sqrt(var(prog)/10+var(usual)/10)
L <- c(prog-mean(prog), -(usual-mean(usual))); acc <- sum(L^3)/(6*sum(L^2)^1.5)
set.seed(12)
one <- function(B){ a <- matrix(sample(prog,10*B,TRUE),10); b <- matrix(sample(usual,10*B,TRUE),10)
  d <- colMeans(a)-colMeans(b); v <- (colSums(a*a)-10*colMeans(a)^2)/90 + (colSums(b*b)-10*colMeans(b)^2)/90
  perc <- boot:::norm.inter(d, c(.025,.975))[,2]
  z0 <- qnorm(sum(d < D)/B); z <- qnorm(c(.025,.975)); al <- pnorm(z0+(z0+z)/(1-acc*(z0+z)))
  bca <- boot:::norm.inter(d, al)[,2]
  tt <- (d - D)/sqrt(v); st <- D - se0*rev(boot:::norm.inter(tt, c(.025,.975))[,2])
  c(perc, bca, st, sd(d)) }
for (B in c(999, 9999, 99999)) { reps <- c(`999`=4000, `9999`=2000, `99999`=400)[as.character(B)]
  r <- replicate(reps, one(B)); q <- function(x) paste(sprintf("%.3f",quantile(x,c(.025,.975),type=1)), collapse=" to ")
  cat(B, reps, "| perc", q(r[1,]), ";", q(r[2,]), "| bca", q(r[3,]), ";", q(r[4,]), "| stud", q(r[5,]), ";", q(r[6,]), "| SE", q(r[7,]), "\n") }
