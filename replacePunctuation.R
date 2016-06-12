library(tm);
replacePunctuation <- content_transformer(function(x) {return (gsub("[[:punct:]]"," ", x))});

