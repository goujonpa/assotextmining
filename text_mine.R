# Needed <- c("tm", "SnowballC", "RColorBrewer", "ggplot2", "wordcloud", "biclust", "cluster", "igraph", "fpc");
# install.packages(Needed, dependencies=TRUE);
# install.packages("Rcampdf", repos = "http://datacube.wu.ac.at/", type = "source");

# custom replace punctuation function
source("replacePunctuation.R");

# custom ignore words function
source("ignoredWords.R");

cname <- file.path("~", "workspace", "sc21", "corpus");  

# ===== DATA PREPROCESSING =====
library(tm);

# load corpus
docs <- Corpus(DirSource(cname));
# remove punctuation
docs <- tm_map(docs, replacePunctuation);
# ignore some words
# TO DO: do the same without ignoring the words !!!!!!!

docs <- tm_map(docs, ignoredWords);

# To remove email punctuation
#for (j in seq(docs))  {   
#    docs[[j]] <- gsub("\\|", " ", docs[[j]])   
#}

# remove numbers
docs <- tm_map(docs, removeNumbers);
# to lowercase
# note : I used the simple tolower at first but it messed up my corpus object
docs <- tm_map(docs, content_transformer(tolower));
# remove french stopwords
docs <- tm_map(docs, removeWords, stopwords("french"));

#Combining words that should stay together
#If you wish to preserve a concept is only apparent as a collection of two or more words, then you can combine them or reduce them to a meaningful acronym before you begin the analysis. Here, I am using examples that are particular to qualitative data analysis.

#for (j in seq(docs))
#{
#    docs[[j]] <- gsub("qualitative research", "QDA", docs[[j]])
#    docs[[j]] <- gsub("qualitative studies", "QDA", docs[[j]])
#    docs[[j]] <- gsub("qualitative analysis", "QDA", docs[[j]])
#    docs[[j]] <- gsub("research methods", "research_methods", docs[[j]])
#}

library(SnowballC);
# getStemLanguages() : allows to see the stem languages
docs <- tm_map(docs, stemDocument, language="french");

# strip useless whitespaces
docs <- tm_map(docs, stripWhitespace);

# tells R to consider the corpus as plain text documents
docs <- tm_map(docs, PlainTextDocument);

# ===== DATA STAGING =====

# create a term matrix from the doc
dtm = DocumentTermMatrix(docs);

# and its transpose 
tdm <- TermDocumentMatrix(docs);

# get the terms frequencies
freq <- colSums(as.matrix(dtm));
ord <- order(freq, decreasing=T);
wf <- data.frame(word=names(freq), freq=freq);

# focus on non sparse items
# 0.1 : 10% empty space max
dtms <- removeSparseTerms(dtm, 0.1);

# ===== Figures =====

library(ggplot2);

# get plot of the top 10 words
top10 = wf[ord[1:10],];
p1 <- ggplot(wf[ord[1:10],], aes(word, freq))
p1 <- p1 + geom_bar(stat="identity")
p1 <- p1 + theme(axis.text.x=element_text(angle=45, hjust=1))

# export top 100
absolute_top200 = wf[ord[1:200],];
write.table(absolute_top200, "plots/everything_top200.csv");

absolute_top1000 = wf[ord[1:1000],];
write.table(absolute_top1000, "plots/everything_top1000.csv");

# wordcloud
library(wordcloud);
# wordcloud(names(freq), freq, min.freq=20, scale=c(5, .1), colors=brewer.pal(6,
# "Dark2"))





