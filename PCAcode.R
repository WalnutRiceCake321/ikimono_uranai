#PCA
library(vegan) 
data<-read.csv("DCAw.csv",head=T,row.name=1)
png("plot1.png",width = 800, height = 800)
pca<-prcomp(data,scale=TRUE)#•W€‰»
summary(pca)
pca$rotation
plot(pca$rotation[,1],pca$rotation[,2],type="n")
text(pca$rotation[,1],pca$rotation[,2],colnames(data))
biplot(pca)
dev.off()
