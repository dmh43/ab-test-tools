n = 1000000/2
ps = c()
aucs = c()
for (i in 1:10) {
    y = ((rnorm(n, log(200), sd=log(100)/10)))
    x = ((rnorm(n, log(201), sd=log(100)/10)))
    res = wilcox.test(x, y)
    ps = c(ps, res[["p.value"]])
    aucs = c(aucs, res[["statistic"]][["W"]] / n / n)
}
hist(aucs)
hist(ps)

null_aucs = c()
for (i in 1:10) {
    y = ((rnorm(n, log(200), sd=log(100)/10)))
    x = ((rnorm(n, log(200), sd=log(100)/10)))
    res = wilcox.test(x, y)
    null_aucs = c(null_aucs, res[["statistic"]][["W"]] / n / n)
}
hist(null_aucs)
