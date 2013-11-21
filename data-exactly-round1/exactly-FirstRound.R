rm(list=ls(all=TRUE))
library(lme4)
library(MASS)
library(binom)
#require(car)
#library(SASmixed)
#library(coda)
#library(languageR)
`%ni%` <- Negate(`%in%`)
se <- function (x) { sd(x)/sqrt(length(x))}

# p.values.lmer <- function(x) {
  # summary.model <- summary(x)
  # data.lmer <- data.frame(model.matrix(x))
  # names(data.lmer) <- names(fixef(x))
  # names(data.lmer) <- gsub(pattern=":", x=names(data.lmer), replacement=".", fixed=T)
  # names(data.lmer) <- ifelse(names(data.lmer)=="(Intercept)", "Intercept", names(data.lmer))
  # string.call <- strsplit(x=as.character(x@call), split=" + (", fixed=T)
  # var.dep <- unlist(strsplit(x=unlist(string.call)[2], " ~ ", fixed=T))[1]
  # vars.fixef <- names(data.lmer)
  # formula.ranef <- paste("+ (", string.call[[2]][-1], sep="")
  # formula.ranef <- paste(formula.ranef, collapse=" ")
  # formula.full <- as.formula(paste(var.dep, "~ -1 +", paste(vars.fixef, collapse=" + "), 
                  # formula.ranef))
  # data.ranef <- data.frame(x@frame[, 
                # which(names(x@frame) %in% names(ranef(x)))])
  # names(data.ranef) <- names(ranef(x))
  # data.lmer <- data.frame(x@frame[, 1], data.lmer, data.ranef)
  # names(data.lmer)[1] <- var.dep
  # out.full <- lmer(formula.full, data=data.lmer, REML=F)
  # p.value.LRT <- vector(length=length(vars.fixef))
  # for(i in 1:length(vars.fixef)) {
    # formula.reduced <- as.formula(paste(var.dep, "~ -1 +", paste(vars.fixef[-i], 
                       # collapse=" + "), formula.ranef))
    # out.reduced <- lmer(formula.reduced, data=data.lmer, REML=F)
    # print(paste("Reduced by:", vars.fixef[i]))
    # print(out.LRT <- data.frame(anova(out.full, out.reduced)))
    # p.value.LRT[i] <- round(out.LRT[2, 7], 3)
  # }
  # summary.model@coefs <- cbind(summary.model@coefs, p.value.LRT)
  # summary.model@methTitle <- c("\n", summary.model@methTitle, 
                           # "\n(p-values from comparing nested models fit by maximum likelihood)")
  # print(summary.model)
# }


#### LOAD ####

data=read.csv(file.choose(), header=T,quote='')
data <- na.omit(data)
head(data)
str(data)


	# data$Group=factor(data$Group); data$Sentence
	# data.TC$Prediction <- rep(0, length(data.TC$Picture_Rep))
	# data.TC$Prediction[data.TC$Quantifier %in% c("bare", "between","some") & data.TC$Condition %in% c("Central")] <- 1
	# data.TC$Prediction[data.TC$Quantifier %in% c("bare", "between") & data.TC$Condition %in% c("Superior")] <- 2
	# data.TC$Prediction[data.TC$Quantifier %in% c("some") & data.TC$Condition %in% c("Total")] <- 2
	# data.TC$Accuracy <- data.TC$Picture_Rep == data.TC$Prediction | data.TC$Prediction == 2
	
	# data.TC$Statut[data.TC$Quantifier %in% c("bare", "between") & data.TC$Condition %in% c("Superior")] <- "target"
	# data.TC$Statut[data.TC$Quantifier %in% c("bare", "between") & data.TC$Condition %in% c("Inferior","Central")] <- "control"
	# data.TC$Statut[data.TC$Quantifier %in% c("some") & data.TC$Condition %in% c("Total")] <- "target"
	# data.TC$Statut[data.TC$Quantifier %in% c("some") & data.TC$Condition %in% c("Null","Central")] <- "control"
	# data.TC$Statut <- factor(data.TC$Statut)


######################################
#### DATA TREATMENT: Filteing RT? ####
######################################

plot(data$Response_time, ylim=c(0,20000), col=data$Subject)

attach(data)
LIMBASSE2 <- tapply(data$Response_time, data$Subject, quantile, .015)
filterB2<-(data$Response_time > LIMBASSE2[data$Subject])
LIMHAUTE2 <- tapply(data$Response_time, data$Subject, quantile, .985)
filterH2<-(data$Response_time < LIMHAUTE2[data$Subject])
filter <- filterH2 & filterB2  
data<-subset(data,filter)
#before<-dim(data)[1]
#after<-dim(data)[1]
#rejected<-(1-(after/before))*100;rejected
plot(data$Response_time, ylim=c(0,10000), col=data$Subject)
detach(data)

###########################
#### RESPONSE ANALYSIS ####
###########################

str(data)
rep<- aggregate(data$Response, list(Block=data$Block, Group=data$Group, Numeral=data$Numeral, Sentence=data$Sentence, Distance=data$Distance, Condition=data$Condition, Subject=data$Subject, Value=data$Expected_value), mean)
tapply(rep$x,list(rep$Sentence,rep$Condition, rep$Block),mean)
tapply(rep$x,list(rep$Sentence,rep$Value, rep$Block),mean)
tapply(rep$x,list(rep$Sentence,rep$Value),mean)
tapply(rep$x,list(rep$Sentence,rep$Distance, rep$Block),mean)
tapply(rep$x,list(rep$Sentence,rep$Condition, rep$Group),mean)

# Response time (apply filter above first)
rep<- aggregate(data$Response_time, list(Block=data$Block, Group=data$Group, Numeral=data$Numeral, Sentence=data$Sentence, Distance=data$Distance, Condition=data$Condition, Subject=data$Subject, Value=data$Expected_value), mean)
tapply(rep$x,list(rep$Sentence,rep$Condition, rep$Block),mean)
tapply(rep$x,list(rep$Sentence,rep$Value, rep$Block),mean)
tapply(rep$x,list(rep$Sentence,rep$Value),mean)
tapply(rep$x,list(rep$Sentence,rep$Distance, rep$Block),mean)
tapply(rep$x,list(rep$Sentence,rep$Condition, rep$Group),mean)

